#!/usr/bin/env python

from xml.etree import ElementTree
from urllib2 import urlopen
from os import mkdir, path, listdir
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4, portrait, landscape
from sys import argv
from urlparse import urlparse

def getlinks(fp):
    links = []

    tree = ElementTree.parse(fp)
    root = tree.getroot()
    for channel in root:
        for item in channel:
            if item.tag == "item":
                for itempart in item:
                    if itempart.tag == "enclosure":
                        links.append(itempart.attrib["url"])
                        break
                    
    return links
    
def download(url):
    return urlopen(url)

def scrape(url):
    print("Downloading RSS feed...")
    rss = download(url)
    print("Done!")
    print("Scraping RSS feed...")
    links = getlinks(rss)
    print("Done!")
    return links
    
def downloadall(links, outdir):
    mkdir(outdir)
    print("Created directory \"out\"")
    for n, i in enumerate(links):
        print("Downloading %s..." % i)
        data = download(i).read()
        print("Writing %s to file..." % i)
        fname = path.split(urlparse(i).path)[1]
        fname = ("%03d" % n) + path.splitext(fname)[1]
        fname = path.join(outdir, fname)
        with open(fname, "wb") as fp:
            fp.write(data)
        print("Done!")
    
def pdf(files, outfile, useportrait=True):
    print("Creating PDF...")
    pdf = Canvas(outfile)
    pagesize = portrait(A4) if useportrait else landscape(A4)
    for i in files:
        print("Creating PDF page for %s..." % i)
        pdf.setPageSize(pagesize)
        pdf.drawImage(i, 0, 0, *pagesize)
        pdf.showPage()
        print("Done!")
    print("Saving PDF...")
    pdf.save()
    print("Done!")
    
def usage():
    print("""
Usage:
    python main.py action options

Actions:
        --scrape url outfile
        Scrapes an ImageShack RSS feed for image URLs and outputs file with list
        --download list outdir
        Downloads images from URLs in list file and names them according to list
        --makepdf directory outfile
        Makes PDF from images in directory
    
    Options:
        -s
        Sorts list
        -r
        Reverses list
        -l
        Makes landscape PDF when making PDF""")
    
if len(argv) > 1:
    if argv[1] == "--scrape":
        result = scrape(argv[2])
        if "-s" in argv: result.sort()
        if "-r" in argv: result = result[::-1]
        with open(argv[3], "w") as fp:
            for i in result:
                fp.write(i+"\n")
    elif argv[1] == "--download":
        with open(argv[2], "r") as fp:
            urls = fp.readlines()
        urls = [i.rstrip("\n") for i in urls]
        if "-s" in argv: urls.sort()
        if "-r" in argv: urls = urls[::-1]
        downloadall(urls, argv[3])
    elif argv[1] == "--makepdf":
        files = [path.join(argv[2], i) for i in listdir(argv[2])]
        if "-s" in argv: files.sort()
        if "-r" in argv: files = files[::-1]
        pdf(files, argv[3], "-l" not in argv)
    else:
        usage()
else:
    usage()
