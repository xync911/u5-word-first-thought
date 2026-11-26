"""Copy entry.txt to the output directory for the make.fun entry.

The entry is exactly one word: the first word that comes to
mind, at most 24 characters, no topic, no explanation, no second
draft.
Serendipity: the happy accident of finding something wonderful
while looking for something else. It is the first thought because
it is the best kind of surprise — unplanned and welcome.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
