%%capture
!pip install "git+https://github.com/google-deepmind/ai-foundations.git@main"

# Packages used.
import random # For sampling from probability distributions.
from collections import Counter, defaultdict # For counting n-grams.

import textwrap # For automatically addding linebreaks to long texts.
import pandas as pd # For construction and visualizing tables.

# Custom functions for providing feedback on your solutions.
from ai_foundations.feedback.course_1 import ngrams
