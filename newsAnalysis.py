import nltk
import ssl
from pprint import pprint

# nltk.download('punkt_tab')

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download([
    "names",
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
])

text = "For some quick analysis, use the NLTK library. It's pretty easy."
pprint(nltk.word_tokenize(text), width=79, compact=True)

