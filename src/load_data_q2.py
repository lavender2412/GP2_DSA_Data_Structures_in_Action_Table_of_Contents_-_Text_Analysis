import requests
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from collections import Counter, deque
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

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


file_path = os.path.join(path, title)

assert os.path.exists(file_path), "File missing!"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

num_chars = len(text)
num_lines = text.count('\n')
print(f"Characters: {num_chars:,}")
print(f"Lines: {num_lines:,}")

print("\n--- SAMPLE ---")
print('\n'.join(text.splitlines()[:15]))

print("="*60)
print("WUTHERING HEIGHTS - Initial Text Information")
print("="*60)
print(f"Total characters: {len(raw_text):,}")
print(f"Total lines: {len(raw_text.splitlines()):,}")
print(f"File size: {len(raw_text.encode('utf-8')) / 1024:.2f} KB")
print("="*60)

import os

possible_paths = [
    "content/wuthering_heights.txt",
    "/content/wuthering_heights.txt",
    "./wuthering_heights.txt"
]

filepath = None
for path in possible_paths:
    if os.path.exists(path):
        filepath = path
        break

if filepath is None:
    raise FileNotFoundError("wuthering_heights.txt not found in expected locations.")

min_size = 5000
encoding = "utf-8"

size = os.path.getsize(filepath)
if size == 0:
    raise ValueError(f"File is empty: {filepath}")

try:
    with open(filepath, "r", encoding=encoding) as f:
        text = f.read()
except UnicodeDecodeError:
    raise ValueError(f"Encoding error using {encoding}")

if len(text) < min_size:
    raise ValueError(f"File too small ({len(text)} chars).")

sample = text[:200]
if not any(c.isalpha() for c in sample):
    raise ValueError("File does not contain readable text.")

print(f"Step 1 validated successfully — {len(text):,} characters loaded from {filepath}")
