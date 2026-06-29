import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize the local lemmatizer and stop words list
LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words('english'))

def preprocess_text(text):
    # Step 1: Tokenize
    tokens = word_tokenize(text)
    
    # Step 2: Remove punctuation and lowercase
    no_punctuation = [token.lower() for token in tokens if token not in string.punctuation]
    
    # Step 3: Remove stop words
    no_stopwords = [token for token in no_punctuation if token not in STOP_WORDS]
    
    # Step 4: Lemmatize each word to its base form
    final_tokens = [LEMMATIZER.lemmatize(token) for token in no_stopwords]
    return final_tokens

if __name__ == "__main__":
    print("Chatbot Initialized (Lemmatization Active)!")
    user_input = input("You: ")
    tokens = preprocess_text(user_input)
    print(f"Final Preprocessed Tokens: {tokens}")
