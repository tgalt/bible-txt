"""Beta code to Unicode Greek, for the unaccented Robinson-family texts.

The parsed Textus Receptus and Byzantine files published by ByzTxt encode
Greek as ASCII "beta code" with no accents or breathings. Two schemes are in
use and they disagree on three letters, so each is given explicitly rather
than guessed at:

  ``UTR``  the parsed Textus Receptus (``*.UTR``): q=theta, c=chi, y=psi,
           and a distinct ``v`` for final sigma.
  ``BP5``  Robinson's Byzantine ``*.BP5`` files: q=theta, x=chi, y=psi, with
           ``s`` for both medial and final sigma (resolved positionally).

``|`` marks an iota subscript and is folded into the preceding vowel.
"""

_COMMON = {
    "a": "α", "b": "β", "g": "γ", "d": "δ", "e": "ε", "z": "ζ", "h": "η",
    "i": "ι", "k": "κ", "l": "λ", "m": "μ", "n": "ν", "o": "ο", "p": "π",
    "r": "ρ", "t": "τ", "u": "υ", "f": "φ", "w": "ω", "q": "θ", "y": "ψ",
}

SCHEMES = {
    "UTR": dict(_COMMON, **{"c": "χ", "x": "ξ", "s": "σ", "v": "ς"}),
    "BP5": dict(_COMMON, **{"x": "χ", "c": "ξ", "s": "σ"}),
}

# Vowels that carry an iota subscript, in their bare (unaccented) form.
SUBSCRIPT = {"α": "ᾳ", "η": "ῃ", "ω": "ῳ"}


def convert(text, scheme="UTR"):
    """Convert one beta-code string to Unicode Greek."""
    table = SCHEMES[scheme]
    out = []
    for ch in text:
        low = ch.lower()
        if ch == "|":
            # Iota subscript binds to the vowel just written.
            if out and out[-1] in SUBSCRIPT:
                out[-1] = SUBSCRIPT[out[-1]]
            continue
        mapped = table.get(low)
        if mapped is None:
            out.append(ch)
            continue
        out.append(mapped.upper() if ch.isupper() else mapped)

    # Schemes without a dedicated final sigma need it resolved by position.
    if "v" not in table:
        for i, ch in enumerate(out):
            if ch == "σ":
                nxt = out[i + 1] if i + 1 < len(out) else ""
                if not nxt.isalpha():
                    out[i] = "ς"
    return "".join(out)
