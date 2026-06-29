import string
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words('english'))

# Expanded Local Intents Dictionary
INTENTS = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "greet"],
        "responses": ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "leave", "exit", "quit"],
        "responses": ["Goodbye! Have a great day!", "See you later!"]
    },
    "help": {
        "keywords": ["help", "info", "support"],
        "responses": ["I am a local NLP chatbot. I can talk about my creator, the year, or the weather!"]
    },
    "creator": {
        "keywords": ["creator", "built", "made", "developer", "programmer"],
        "responses": ["I was built by a brilliant developer using local Python and NLTK logic!", "You made me!"]
    },
    "year": {
        "keywords": ["year", "date", "today"],
        "responses": ["The current calendar year is 2026.", "We are living in the year 2026!"]
    },
    "weather": {
        "keywords": ["weather", "rain", "sun", "sunny", "cloudy"],
        "responses": ["Since I run entirely locally without external APIs, I can't check live data, but I hope it's sunny outside!", "I don't have internet access to check live forecasts, but stay cozy!"]
    }
}

def preprocess_text(text):
    tokens = word_tokenize(text)
    no_punctuation = [token.lower() for token in tokens if token not in string.punctuation]
    no_stopwords = [token for token in no_punctuation if token not in STOP_WORDS]
    final_tokens = [LEMMATIZER.lemmatize(token) for token in no_stopwords]
    return final_tokens

def match_intent(tokens):
    for token in tokens:
        for intent, data in INTENTS.items():
            if token in data["keywords"]:
                return intent, random.choice(data["responses"])
    return None, "I'm sorry, I didn't quite understand that. Could you rephrase?"

if __name__ == "__main__":
    print("==============================================")
    print("   Improved Chatbot Active! Type 'exit' to quit.")
    print("==============================================")
    
    while True:
        user_input = input("You: ")
        
        if user_input.strip().lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break
            
        tokens = preprocess_text(user_input)
        intent, response = match_intent(tokens)
        
        print(f"Bot: {response}")
        print("-" * 30)
        
        if intent == "goodbye":
            break
