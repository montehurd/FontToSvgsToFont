#!/usr/local/bin/fontforge

# Created by Monte Hurd on 11/06/14.
# Copyright (c) 2014 Monte Hurd. Provided under MIT-style license; please copy and modify!
#
# Extracts svg for each glyph in "./font.ttf" to "./svgs/" folder.
# Also extracts font settings to "./font.json" file.
#
# The svgs can then be edited (or added/removed) and the 
# "makeFontFromSvgs.py" script can be run to rebuild the
# font from the svgs.
#
# See "makeFontFromSvgs.py" for svg file naming convention.
#
# Invoke with command:
#    fontforge -script makeSvgsFromFont.py
#

import fontforge
import json
import os
import sys
import fileinput

# Ensure the svgs folder exists.
svgFolder = "./svgs/"
try:
    os.makedirs(svgFolder)
except OSError:
    if os.path.exists(svgFolder):
        pass
    else:
        raise

# Open the font file.
font = fontforge.open("font.ttf")
print font.fontname

# Export font glyphs to svgs.
print "\nExporting svgs:"
for g in font.glyphs():
  if g.unicode != -1:
    svgPath = "%s%04X %s.svg" % (svgFolder, g.unicode, g.glyphname)
    print "\t%s" % (svgPath)
    g.export(svgPath)
    for line in fileinput.input(svgPath, inplace=1):
        print line.replace("<svg viewBox", '<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="2048" viewBox'),

# Export font settings to json.
fontInfo = {
    "fontname": font.fontname,
    "fullname": font.fullname,
    "familyname": font.familyname,
    "weight": font.weight,
    "version": font.version,
    "encoding": font.encoding,
    "copyright": font.copyright,
    "em": font.em,
    "ascent": font.ascent,
    "descent": font.descent
}

# Write json data.
file = open("./font.json", "w")
file.write(json.dumps(fontInfo, indent=4, sort_keys=True))

# Done!
font.close()
print "Finished exporting.\n"

