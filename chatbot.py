import string
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

LEMMATIZER = WordNetLemmatizer()
STOP_WORDS = set(stopwords.words('english'))

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
        "responses": ["I am a local NLP chatbot. I can greet you, say goodbye, or offer help!"]
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
    print("   Local NLP Chatbot Active! Type 'exit' to quit.")
    print("==============================================")
    
    while True:
        user_input = input("You: ")
        
        # Immediate local fallback to break the loop safely
        if user_input.strip().lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break
            
        tokens = preprocess_text(user_input)
        intent, response = match_intent(tokens)
        
        print(f"Bot: {response}")
        print("-" * 30)
        
        # Break the loop if the matched intent was a goodbye
        if intent == "goodbye":
            break
