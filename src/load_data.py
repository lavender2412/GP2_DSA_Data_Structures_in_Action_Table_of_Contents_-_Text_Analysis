import os
import re
import gdown

def download_and_clean_toc(file_id: str, output: str = "table_of_contents_corrected.txt"):
    if not os.path.exists(output):
        gdown.download(id=file_id, output=output, quiet=False)

    with open(output, encoding="utf-8") as file:
        contents = file.read()

    cleaned_contents = []
    for line in contents.splitlines():
        strip = line.strip()
        replace_period = re.sub(r'\.{2,}', "", strip)
        split = replace_period.split("  ")
        if len(split) > 2:
            cleaned_contents.append(split)
    return cleaned_contents
