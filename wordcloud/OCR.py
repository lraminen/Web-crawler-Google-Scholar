import ConfigParser
import glob
import string
import shutil
import re
import os
import sys
import logging
from pprint import pprint, pformat
from argparse import ArgumentParser
import yaml
from PyPDF2 import PdfFileReader

def pdf2text(filename):
    text=[]
    pdf=PdfFileReader(file(filename,'rb'))
    pages=pdf.getNumPages()
    for num in range(pages):
        text.append(pdf.getPage(num).extractText())
    return text

def get_keywords(file):
    config=ConfigParser.ConfigParser()
    config.read(file)
    return config.items('Main')

def match(text,keywords):
    output=[]
    for x in keywords:
        if string.find(text,keyword):
            output[keyword]+=1
        else:
            output[keyword]='None found'
    return output
    
        
               


filename=r'C:\Users\leela\gscholar\OCR\asthma.pdf'
text = pdf2text(filename)
searchtext = '\n'.join(pagetext).lower()
keywords=get_keywords(r'C:\Users\leela\gscholar\OCR\keywords.txt')
print(match(text,keywords))
    
