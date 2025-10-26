####Imports

%%capture
!pip install "git+https://github.com/google-deepmind/ai-foundations.git@main"

# Packages used.
import random # For sampling from probability distributions.
from collections import Counter, defaultdict # For counting n-grams.

import textwrap # For automatically addding linebreaks to long texts.
import pandas as pd # For construction and visualizing tables.

# Custom functions for providing feedback on your solutions.
from ai_foundations.feedback.course_1 import ngrams

####Dataset loading and tokenization

africa_galore = pd.read_json(
    "https://storage.googleapis.com/dm-educational/assets/ai_foundations/africa_galore.json"
)
dataset = africa_galore["description"]
print(f"The dataset consists of {dataset.shape[0]} paragraphs.")

####
for paragraph in dataset[:10]:
    # textwrap automatically adds linebreaks to make long texts more readable.
    formatted_paragraph = textwrap.fill(paragraph)
    print(f"{formatted_paragraph}\n")
  
####Tokenization

def space_tokenize(text: str) -> list[str]:
    """Splits a string into a list of words (tokens).

    Splits text on space.

    Args:
        text: The input text.

    Returns:
        A list of tokens. Returns empty list if text is empty or all spaces.
    """
    tokens = text.split(" ")
    return tokens

# Tokenize an example text with the `space_tokenize` function.
space_tokenize("Kanga, a colorful printed cloth is more than just a fabric.")

####Counting n-grams

def get_ngram_counts(dataset: list[str], n: int) -> dict[str, Counter]:
    """Computes the n-gram counts from a dataset.

    This function takes a list of text strings (paragraphs or sentences) as
    input, constructs n-grams from each text, and creates a dictionary where:

    * Keys represent n-1 token long contexts `context`.
    * Values are a Counter object `counts` such that `counts[next_token]` is the
      count of `next_token` following `context`.

    Args:
        dataset: The list of text strings in the dataset.
        n: The size of the n-grams to generate (e.g., 2 for bigrams, 3 for
            trigrams).

    Returns:
        A dictionary where keys are (n-1)-token contexts and values are Counter
        objects storing the counts of each next token for that context.

    """

    # Define the dictionary as a defaultdict that is automatically initialized
    # with an empty Counter object. This allows you to access and set the value
    # of ngram_counts[context][next_token] without initializing
    # ngram_counts[context] or ngram_counts[next_token] first.
    # Reference
    # https://docs.python.org/3/library/collections.html#collections.Counter and
    # https://docs.python.org/3/library/collections.html#collections.defaultdict
    # for more information on how to use defaultdict and Counter types.
    ngram_counts = defaultdict(Counter)

    for paragraph in dataset:
        # Add your code here.
        # i should loop over all tokens one by one to extract contexes depending on
    # the n ( n-1 for contexts)
     tokens= space_tokenize(paragraph)
     for i in range(len(tokens) - n+1): 
      contex = " ".join(tokens[i:i+n-1])
      next_token=tokens[i+n-1]
      ngram_counts[contex][next_token]+=1
    return dict(ngram_counts)


# Example usage of the function.
example_data = [
    "This is an example sentence.",
    "Another example sentence.",
    "Split a sentence."
]
ngram_counts = get_ngram_counts(example_data, 2)

# Print the bigram counts dictionary for the dataset consisting of the
# three example sentences.
print("Bigram counts dictionary:\n")
print("{")
for context, counter in ngram_counts.items():
    print(f"  '{context}': {counter},")
print("}")
