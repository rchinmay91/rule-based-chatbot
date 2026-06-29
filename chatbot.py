import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load the local list of English stop words
STOP_WORDS = set(stopwords.words('english'))

def preprocess_text(text):
    # Step 1: Tokenize
    tokens = word_tokenize(text)
    
    # Step 2: Remove punctuation and lowercase the words
    no_punctuation = [token.lower() for token in tokens if token not in string.punctuation]
    
    # Step 3: Remove stop words
    cleaned_tokens = [token for token in no_punctuation if token not in STOP_WORDS]
    return cleaned_tokens

if __name__ == "__main__":
    print("Chatbot Initialized (Stop Words Removal Active)!")
    user_input = input("You: ")
    tokens = preprocess_text(user_input)
    print(f"Processed Tokens: {tokens}")
