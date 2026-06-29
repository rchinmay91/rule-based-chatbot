import string
import nltk
from nltk.tokenize import word_tokenize

def tokenize_and_clean(text):
    # Step 1: Tokenize the text
    tokens = word_tokenize(text)
    
    # Step 2: Remove punctuation
    cleaned_tokens = [token for token in tokens if token not in string.punctuation]
    return cleaned_tokens

if __name__ == "__main__":
    print("Chatbot Initialized (Punctuation Removal Active)!")
    user_input = input("You: ")
    tokens = tokenize_and_clean(user_input)
    print(f"Cleaned Tokens: {tokens}")
