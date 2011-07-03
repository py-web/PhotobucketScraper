#!/usr/bin/env python

from xml.etree import ElementTree
from urllib2 import urlopen
from os import mkdir, path
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from sys import argv

def getlinks(fp):
    links = []

    tree = ElementTree.parse(fp)
    root = tree.getroot()
    for channel in root:
        for item in channel:
            if item.tag == "item":
                itemname = None
                itemurl = None
                for itempart in item:
                    if itempart.tag == "enclosure":
                        itemurl = itempart.attrib["url"]
                    elif itempart.tag == "title":
                        itemname = itempart.text
                if itemname and itemurl:
                    links.append((itemname, itemurl))
                    
    return links
    
def download(url):
    return urlopen(url)

def scrape(url, directory):
    mkdir(directory)
    print("Created directory (%s)" % directory)
    print("Downloading RSS feed...")
    rss = download(url)
    print("Done!")
    print("Scraping RSS feed...")
    links = getlinks(rss)
    print("Done!")
    
    files = []
    for i in links:
        print("Downloading %s from %s..." % i)
        data = download(i[1]).read()
        print("Writing %s to file..." % i[0])
        fname = path.join(directory, i[0])
        files.append(fname)
        with open(fname, "wb") as fp:
            fp.write(data)
        print("Done!")
    print("Scraping done!")
    
    return files
    
def pdf(url, name):
    files = scrape(url, name)
    print("Creating PDF...")
    pdf = Canvas("%s.pdf" % name)
    for i in files:
        print("Creating PDF page for %s..." % i)
        pdf.drawImage(i, 0, 0, *A4)
        pdf.showPage()
        print("Done!")
    print("Saving PDF...")
    pdf.save()
    print("Done!")
    
if len(argv) == 3:
    pdf(argv[1], argv[2])
else:
    print("Usage:")
    print("    python main.py rssurl name")
    print("Produces a folder containing images and a pdf of that name containing all images.")
    print()
    print("E.g. python main.py http://feedmg.photobucket.com/albums/v653/Rougey2/WITCH%20issue%203/feed.rss issue3")
