# Create SVG file from TXT

This code reads one or more txt files in order to create svg files. The text files should contain the svg code inside.

It reads recursively in the sub folders as well. 

I searched of how to put this together this days ago because of a problem I had to solve at work. Doing it manually would take so long, so after some search, I put this code together.


## Running the tests

To test the application you must have python 3 installed at your machine because the module scandir is in a different location on version 2.

Before running the code, I created a file structure to test. The structure is the following:

create_svg_from_txt.py

├── create_svg_from_txt.py
├── README.md
└── test
    ├── file1.svg
    ├── file1.txt
    ├── test2
    │   ├── file2.svg
    │   └── file2.txt
    └── test3

In the files file1.txt and file2.txt I added a simple svg code like the following:

<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="100%" height="100%" version="1.1" xmlns="http://www.w3.org/2000/svg"><rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:1;stroke:rgb(0,0,0)"/></svg>

I used the code below to run the code.

`python3 create_svg_from_txt.py`

Then, I checked if what I was expecting happened. And it did. So the code worked for what I needed to do.