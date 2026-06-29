import nltk
from nltk.tokenize import word_tokenize

print("Downloading NLTK resources...")

nltk.download("punkt")
nltk.download("punkt_tab")   # <-- Add this line
nltk.download("stopwords")
nltk.download("wordnet")

print("All resources downloaded successfully!")

print(word_tokenize("Hello, welcome to NLP!"))


exit()
