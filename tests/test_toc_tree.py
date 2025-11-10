import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.toc_tree import Node
from src.load_data import download_and_clean_toc

def test_toc_building():
    FILE_ID = "17TUKK5KNXvE3tr3STzHNK_QL4WpwcU_Z"
    cleaned_contents = download_and_clean_toc(FILE_ID)

    book = Node(book="Data Science and Predictive Analytics", section=None, title=None, page=None)
    book.insert_many(cleaned_contents)

    assert book.total > 0
    assert book.tree_height() > 0
    assert book.tree_depth("Parkinson’s Disease") >= 0

    print("✅ All tests passed.")

if __name__ == "__main__":
    test_toc_building()
