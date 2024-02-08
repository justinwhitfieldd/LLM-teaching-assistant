#TODO
import pandas as pd
import tiktoken
# consider https://pypi.org/project/embeddings-util/
import sys
from utils.embeddings_utils import get_embedding
embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 8000  # the maximum for text-embedding-3-small is 8191

# load & inspect dataset
# replace read_pdf with https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
df = pd.read_pdf('exampleData/01-CSE4283-Orientation-SE-Recap.pdf', index_col=0)
df["combined"] = (
    "Title: " + df.Summary.str.strip() + "; Content: " + df.Text.str.strip()
)
df.head(2)