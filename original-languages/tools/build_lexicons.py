#!/usr/bin/env python3
"""Build the lexicon tables.

Produces four tab-separated tables, one row per entry, definitions flattened
to a single line so the files stay greppable:

  strongs-hebrew.tsv  Strong's Hebrew dictionary (1890), with KJV renderings
  strongs-greek.tsv   Strong's Greek dictionary (1890), with KJV renderings
  bdb.tsv             Brown-Driver-Briggs, keyed to Strong's where BDB maps
  dodson-greek.tsv    Dodson's Greek lexicon, brief and full glosses

Usage: build_lexicons.py <path-to-src-checkouts> <output-dir>
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"


def parse(path):
    """Parse an XML file, stripping namespaces so tags can be named plainly."""
    tree = ET.parse(path)
    for el in tree.iter():
        if isinstance(el.tag, str) and el.tag.startswith("{"):
            el.tag = el.tag.split("}", 1)[1]
        for key in [k for k in el.attrib if k.startswith("{") and "XML/1998" not in k]:
            el.attrib[key.split("}", 1)[1]] = el.attrib.pop(key)
    return tree


def flatten(el):
    """Collapse an element's whole subtree to one whitespace-normalised line."""
    return re.sub(r"\s+", " ", "".join(el.itertext())).strip()


def pad(code):
    """Normalise ``H1`` / ``G26`` to the zero-padded ``H0001`` / ``G0026`` form
    used by the corpus word tables, so the two join directly."""
    m = re.match(r"^([HG])0*(\d+)([a-z]?)$", code or "")
    return f"{m.group(1)}{int(m.group(2)):04d}{m.group(3)}" if m else (code or "")


def write_tsv(path, header, rows):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\t".join(header) + "\n")
        for row in rows:
            fh.write("\t".join(str(c).replace("\t", " ") for c in row) + "\n")
    return len(rows)


def strongs_hebrew(src, out):
    tree = parse(os.path.join(src, "HebrewLexicon", "HebrewStrong.xml"))
    rows = []
    for entry in tree.iter("entry"):
        w = entry.find("w")
        rows.append((
            pad(entry.get("id", "")),
            w.text or "" if w is not None else "",
            w.get("xlit", "") if w is not None else "",
            w.get("pron", "") if w is not None else "",
            w.get("pos", "") if w is not None else "",
            w.get(XML_LANG, "") if w is not None else "",
            flatten(entry.find("source")) if entry.find("source") is not None else "",
            flatten(entry.find("meaning")) if entry.find("meaning") is not None else "",
            flatten(entry.find("usage")) if entry.find("usage") is not None else "",
        ))
    rows.sort(key=lambda r: int(re.sub(r"\D", "", r[0]) or 0))
    return write_tsv(os.path.join(out, "strongs-hebrew.tsv"),
                     ["strongs", "word", "transliteration", "pronunciation",
                      "part_of_speech", "language", "derivation", "definition",
                      "kjv_usage"], rows)


def strongs_greek(src, out):
    text = open(os.path.join(src, "strongs", "greek",
                             "strongs-greek-dictionary.js"),
                encoding="utf-8").read()
    body = text[text.index("{", text.index("=")):text.rindex("}") + 1]
    data = json.loads(body)
    rows = []
    for key, e in data.items():
        rows.append((
            pad(key),
            e.get("lemma", ""),
            e.get("translit", ""),
            re.sub(r"\s+", " ", e.get("derivation", "")).strip(),
            re.sub(r"\s+", " ", e.get("strongs_def", "")).strip(),
            re.sub(r"\s+", " ", e.get("kjv_def", "")).strip(),
        ))
    rows.sort(key=lambda r: int(re.sub(r"\D", "", r[0]) or 0))
    return write_tsv(os.path.join(out, "strongs-greek.tsv"),
                     ["strongs", "word", "transliteration", "derivation",
                      "definition", "kjv_usage"], rows)


def bdb(src, out):
    # LexicalIndex maps each BDB entry id to a Strong's number where one exists.
    index = parse(os.path.join(src, "HebrewLexicon", "LexicalIndex.xml"))
    to_strongs = {}
    for entry in index.iter("entry"):
        xref = entry.find("xref")
        if xref is None:
            continue
        bdb_id, strong = xref.get("bdb"), xref.get("strong")
        if not (bdb_id and strong):
            continue
        # A handful of entries are keyed to an inseparable particle (b, c, d,
        # k, l, m, s, i) rather than a number; those pass through unchanged.
        code = "H{:04d}".format(int(strong)) if strong.isdigit() else strong
        to_strongs.setdefault(bdb_id, code)

    tree = parse(os.path.join(src, "HebrewLexicon", "BrownDriverBriggs.xml"))
    rows = []
    for entry in tree.iter("entry"):
        bdb_id = entry.get("id", "")
        head = entry.find("w")
        body = flatten(entry)
        # The <status> marker is editorial bookkeeping, not part of the entry.
        status = entry.find("status")
        if status is not None:
            body = body.replace(flatten(status), "").strip()
        rows.append((bdb_id, to_strongs.get(bdb_id, ""),
                     (head.text or "").strip() if head is not None else "",
                     entry.get("type", ""), body))
    return write_tsv(os.path.join(out, "bdb.tsv"),
                     ["bdb_id", "strongs", "headword", "type", "entry"], rows)


def dodson(src, out):
    tree = parse(os.path.join(src, "Dodson-Greek-Lexicon", "dodson.xml"))
    rows = []
    for entry in tree.iter("entry"):
        n = entry.get("n", "")
        number = n.split("|")[-1].strip() if "|" in n else ""
        orth = entry.find("orth")
        defs = {d.get("role"): flatten(d) for d in entry.findall("def")}
        rows.append((
            "G{:04d}".format(int(number)) if number.isdigit() else "",
            flatten(orth) if orth is not None else "",
            defs.get("brief", ""),
            defs.get("full", ""),
        ))
    rows.sort(key=lambda r: (r[0] == "", r[0]))
    return write_tsv(os.path.join(out, "dodson-greek.tsv"),
                     ["strongs", "word", "brief_definition",
                      "full_definition"], rows)


def main(src, out):
    os.makedirs(out, exist_ok=True)
    for label, n in [
            ("strongs-hebrew.tsv", strongs_hebrew(src, out)),
            ("strongs-greek.tsv", strongs_greek(src, out)),
            ("bdb.tsv", bdb(src, out)),
            ("dodson-greek.tsv", dodson(src, out)),
    ]:
        print(f"{label:22s} {n:>7,} entries")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
