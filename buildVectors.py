import pandas as pd
import tiktoken
# consider https://pypi.org/project/embeddings-util/
from PyPDF2 import PdfReader 
import os
from utils.embeddings_utils import get_embedding
embedding_model = "text-embedding-3-small"
embedding_encoding = "cl100k_base"
max_tokens = 8000  # the maximum for text-embedding-3-small is 8191

# Get text from all files in exampleData folder
for filename in os.listdir('exampleData'):
    filepath = os.path.join('exampleData', filename)
    df = PdfReader(filepath)
    for page in df.pages:
        print(page.extract_text())

# TODO
        # after seperating text from pdf now build into vectors