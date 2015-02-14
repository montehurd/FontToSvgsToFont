Editing fonts can be hard and editing them with FontForge is an absolute UX nightmare.

The purpose of this repo is to make it easy to convert a ttf font into a folder of svgs which can be edited/added/removed and then re-imported into the font.

Because Svgs don't have awareness of font specific settings such as glyph character mapping, the svgs extracted from the font are named in such a way to preserve this info. A file called font.json is also made to preserve some of the non-glyph settings from the font. In this way the extraction step is made reversible.

Two scripts automate the Font to Svg and Svg to Font conversion:

    makeSvgsFromFont.py


This converts a ttf font into a folder of svgs naming the svg files according to a naming convention which preserves respective glyph position, naming and character mapping. A "font.json" file is also created to store font specific settings.


    makeFontFromSvgs.py


This rebuilds the font from the folder of svgs and font.json and also creates an html file referencing the rebuilt font for easier proofing. Note: you may need to close and re-open your browser to see changes made to the html file.


Both scripts require FontForge. They have only been tested on Ubuntu.

Usage:

-Install FontForge.


-Rename your ttf font file to "font.ttf" and place it in same directory as the script files.


-Open terminal, change to the directory containing the scripts.

    
-Run the command:


    fontforge -script makeSvgsFromFont.py

    
This will extract a svg for each glyph in "./font.ttf" to "./svgs/" folder.


It will also extract font settings to "./font.json" file.
    

Svg's are named according to following convention:


    UNICODE_CHAR GLYPH_NAME.svg


Example: "e950 MY_GLYPH 150.svg"


This svg will be mapped to the font character e950 with glyph name "MY_GLYPH".


Once you make changes to the svgs, font.ttf can be rebuild with this command:


    fontforge -script makeFontFromSvgs.py
