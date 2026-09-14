#!/bin/sh
# Fetch the original-language resources this repo deliberately does not vendor.
#
# Everything under original-languages/ is built from openly licensed sources
# that can be redistributed. The resources below are all open too, but are left
# out of the repo for one of three reasons, noted per entry: the publisher asks
# to be the single point of distribution, the data is far larger than this repo
# should carry, or the licence is not compatible with the rest of the tree.
#
# Usage:  ./fetch-more.sh [target-directory]      (default: ./external)
set -eu

TARGET="${1:-external}"
mkdir -p "$TARGET"
cd "$TARGET"

clone() {
    name="$(basename "$1")"
    if [ -d "$name" ]; then
        echo "  already present: $name"
    else
        echo "  cloning $1"
        git clone --depth 1 "https://github.com/$1.git" "$name"
    fi
}

echo "STEPBible (CC BY 4.0)"
echo "  TAHOT/TAGNT word-by-word Hebrew and Greek, the Tyndale brief lexicons,"
echo "  full LSJ entries for biblical words, proper names, and TVTMS, which maps"
echo "  between versification traditions. Not vendored: the data asks that"
echo "  STEPBible remain the single point of distribution."
clone STEPBible/STEPBible-Data

echo
echo "MACULA (CC BY 4.0)"
echo "  Syntax trees, semantic roles, UBS MARBLE word senses and participant"
echo "  reference for both testaments. Not vendored: size."
clone Clear-Bible/macula-hebrew
clone Clear-Bible/macula-greek

echo
echo "ETCBC BHSA (data CC BY-NC 4.0, tooling MIT)"
echo "  The richest syntactic database of the Hebrew Bible, in Text-Fabric form."
echo "  Not vendored: the non-commercial clause does not match the rest of this"
echo "  tree, so keep it separate and check the terms before redistributing."
clone ETCBC/bhsa

echo
echo "unfoldingWord (CC BY-SA 4.0)"
echo "  Lexically tagged, morphologically parsed Hebrew OT and Greek NT in USFM,"
echo "  with alignment data. Hosted on Door43 rather than GitHub."
for repo in hbo_uhb el-x-koine_ugnt; do
    if [ -d "$repo" ]; then
        echo "  already present: $repo"
    else
        echo "  cloning $repo"
        git clone --depth 1 "https://git.door43.org/unfoldingWord/$repo.git" || \
            echo "  (skipped: git.door43.org unreachable from here)"
    fi
done

echo
echo "Septuagint"
echo "  Swete's edition (1930), Greek text and annotations CC BY-SA 4.0."
clone eliranwong/LXX-Swete-1930

echo
echo "Abbott-Smith, Manual Greek Lexicon of the New Testament (public domain)"
echo "  TEI XML. Not vendored: the checkout is dominated by a large scan PDF."
clone translatable-exegetical-tools/Abbott-Smith

echo
echo "Sefaria (per-text licences; Miqra according to the Masorah is CC BY-SA)"
echo "  Hebrew Tanakh with the Jewish commentary tradition. The text itself is"
echo "  a ~26 GB public bucket; this clone is only the index and tooling."
clone Sefaria/Sefaria-Export

echo
echo "Done. Fetched into: $(pwd)"
