A purpose-built tool to make a task for a friend quicker and easier. It provides 3 functions: Extracting URLs from a Photobucket RSS feed, downloading every image in a list, and generating a PDF from a directory of images.
It requires Python (tested on 2.7, probably works on 2.6 and earlier too), and [ReportLab Toolkit](http://www.reportlab.com/software/opensource/rl-toolkit/download/) to generate PDFs.

Usage
=====

    Usage:
        python main.py action options

    Actions:
        --scrape url
            Scrapes an ImageShack RSS feed for image URLs and outputs file with list
            --download list
            Downloads images from URLs in list file and names them according to list
            --makepdf directory
            Makes PDF from images in directory
        
        Options:
            -s
            Sorts list
            -r
            Reverses list
            -l
            Makes landscape PDF

License
=======

    Copyright (c) 2011 Andrew Faulds

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
