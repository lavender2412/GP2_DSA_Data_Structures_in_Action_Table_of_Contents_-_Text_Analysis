import re
import string
import math
import collections
import itertools
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from google.colab import drive
drive.mount('/content/drive')

import os

os.makedirs("data", exist_ok=True)
os.makedirs("src", exist_ok=True)
os.makedirs("outputs/figures", exist_ok=True)

import os
from urllib import request

path = "/content"
title = "wuthering_heights.txt"
url = "https://www.gutenberg.org/cache/epub/768/pg768.txt"

filename = os.path.join(path, title)

if os.path.isfile(filename) and os.stat(filename).st_size != 0:
    print(f"{title} already exists locally.")
    with open(filename, "r", encoding="utf-8") as f:
        raw_text = f.read()
else:
    print(f"{title} not found locally. Downloading from Project Gutenberg...")
    response = request.urlopen(url)
    raw_text = response.read().decode("utf-8-sig")
    print(f"Saving {title} locally.")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(raw_text)

print(f"Loaded {len(raw_text)} characters of text.")


file_path = "data/Wuthering Heights.txt"


assert os.path.exists(file_path), "File missing!"


with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()


num_chars = len(text)
num_lines = text.count('\n')
print(f"Characters: {num_chars:,}")
print(f"Lines: {num_lines:,}")


print("\n--- SAMPLE ---")
print('\n'.join(text.splitlines()[:15]))


with open(file_path, "r", encoding="latin-1") as f:
    text = f.read()
with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("="*60)
print("WUTHERING HEIGHTS - Initial Text Information")
print("="*60)
print(f"Total characters: {len(raw_text):,}")
print(f"Total lines: {len(raw_text.splitlines()):,}")
print(f"File size: {len(raw_text.encode('utf-8')) / 1024:.2f} KB")
print("="*60)

#!pip install wordcloud pandas matplotlib 
# added these packages in the requirements.txt file

import os
from pathlib import Path

def extract_book_text_from_chapter1(text):
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK WUTHERING HEIGHTS ***"
    start_pos = text.find(start_marker)

    if start_pos != -1:
        start_pos = start_pos + len(start_marker)
    else:
        start_pos = 0

    chapter_markers = [
        "CHAPTER I.",
        "CHAPTER I\n",
        "CHAPTER 1",
        "Chapter 1",
        "Chapter I"
    ]

    chapter_start = -1
    for marker in chapter_markers:
        pos = text.find(marker, start_pos)
        if pos != -1:
            chapter_start = pos
            break

    if chapter_start != -1:
        start_pos = chapter_start

    end_markers = [
        "*** END OF THE PROJECT GUTENBERG EBOOK WUTHERING HEIGHTS ***",
        "*** END OF THIS PROJECT GUTENBERG EBOOK",
        "End of the Project Gutenberg EBook",
    ]

    end_pos = len(text)
    for marker in end_markers:
        pos = text.find(marker)
        if pos != -1:
            end_pos = pos
            break

    clean_text = text[start_pos:end_pos].strip()

    return clean_text


book_text = extract_book_text_from_chapter1(raw_text)

print("="*60)
print("TEXT CLEANING RESULTS")
print("="*60)
print(f"Original length: {len(raw_text):,} characters")
print(f"Cleaned length:  {len(book_text):,} characters")
print(f"Removed:         {len(raw_text) - len(book_text):,} characters")
print("="*60)

print("\n--- FIRST 500 CHARACTERS ---\n")
print(book_text[:500])
print("\n[...]\n")

print("\n--- LAST 300 CHARACTERS ---\n")
print(book_text[-300:])
print("\n")



assert len(book_text) > 0, "Text is empty!"
assert len(book_text) > 100000, "Text seems too short"
assert "Gutenberg" not in book_text[:1000], "Header not removed!"
assert "Gutenberg" not in book_text[-1000:], "Footer not removed!"
assert len(book_text.split()) >= 50000, "Word count below requirement!"

print("✓ All Step 1 validations passed!")