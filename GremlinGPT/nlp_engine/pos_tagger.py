# GremlinGPT/nlp_engine/pos_tagger.py

#!/usr/bin/env python3

# ─────────────────────────────────────────────────────────────
# ⚠️ GremlinGPT Fair Use Only | Commercial Use Requires License
# Built under the GremlinGPT Dual License v1.0
# © 2025 StatikFintechLLC / AscendAI Project
# Contact: ascend.gremlin@gmail.com
# ─────────────────────────────────────────────────────────────

# GremlinGPT v1.0.3 :: Module Integrity Directive
# This script is a component of the GremlinGPT system, under Alpha expansion.

import os
import nltk
from nltk import pos_tag, word_tokenize
from datetime import datetime
from loguru import logger

from memory.vector_store.embedder import embed_text, package_embedding, inject_watermark

WATERMARK = "source:GremlinGPT"
ORIGIN = "pos_tagger"

# Ensure punkt is available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", download_dir="/usr/local/share/nltk_data")
nltk.download("averaged_perceptron_tagger", quiet=True)

# Ensure global nltk data path is registered
NLTK_PATHS = ["/usr/local/share/nltk_data", ".data/nltk_data"]
for path in NLTK_PATHS:
    nltk.data.path.append(path)


MODEL = CFG["nlp"].get("tokenizer_model", "bert-base-uncased")


def get_pos_tags(text):
    """
    Performs part-of-speech tagging on input text.
    Logs metadata and embeds summary in vector memory.
    """
    try:
        tokens = word_tokenize(text)
        tags = pos_tag(tokens)

        # Structured trace metadata
        summary = f"POS tagging: {len(tokens)} tokens | Example: {tags[:3]}"
        vector = embed_text(summary)

        package_embedding(
            text=summary,
            vector=vector,
            meta={
                "origin": ORIGIN,
                "timestamp": datetime.utcnow().isoformat(),
                "token_count": len(tokens),
                "watermark": WATERMARK,
            },
        )

        inject_watermark(origin=ORIGIN)

        return tags

    except Exception as e:
        logger.error(f"[POS_TAGGER] Failed to tag input: {e}")
        return []
