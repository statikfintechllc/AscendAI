import os
import nltk

def setup_nltk_data():
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "data", "nltk_data")
    )
    fallback_dirs = ["/usr/local/share/nltk_data", base_dir]

    for path in fallback_dirs:
        nltk.data.path.append(path)

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt", download_dir=base_dir)

    return base_dir
