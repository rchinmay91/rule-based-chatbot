import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words('english'))

# Predefined intents, keywords (must be lowercase/lemmatized), and responses
INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greet"],
        "responses": ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "leave", "exit"],
        "responses": ["Goodbye! Have a great day!", "See you later!"]
    },
    "help": {
        "keywords": ["help", "info", "support"],
        "responses": ["I am a local NLP chatbot. I can greet you, say goodbye, or answer basic questions!"]
    }
}

def preprocess_text(text):
    tokens = word_tokenize(text)
    no_punctuation = [token.lower() for token in tokens if token not in string.punctuation]
    no_stopwords = [token for token in no_punctuation if token not in STOP_WORDS]
    final_tokens = [LEMMATIZER.lemmatize(token) for token in no_stopwords]
    return final_tokens

def match_intent(tokens):
    # Check each token against our intent keywords
    for token in tokens:
        for intent, data in INTENTS.items():
            if token in data["keywords"]:
                # Return the first matching response found
                import random
                return random.choice(data["responses"])
    
    return "I'm sorry, I didn't quite understand that. Could you rephrase?"

if __name__ == "__main__":
    print("Chatbot Initialized (Intent Matching Active)!")
    user_input = input("You: ")
    tokens = preprocess_text(user_input)
    response = match_intent(tokens)
    print(f"Bot: {response}")
