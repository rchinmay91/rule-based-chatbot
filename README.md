# Local NLP Chatbot

A simple, rule-based conversational chatbot built entirely using **Python** and the **Natural Language Toolkit (NLTK)** library. This application processes text inputs locally without using external cloud infrastructure, tokens, or API keys.

## Features
- **Tokenization:** Breaks down user text strings into discrete word tokens.
- **Punctuation Removal:** Filters out structural punctuation marks to streamline text processing.
- **Stop Words Filtering:** Automatically drops common filler words (e.g., "the", "is", "at") to highlight core vocabulary.
- **Lemmatization:** Restores remaining words to their base vocabulary form for cleaner keyword classification.
- **Intent Matching Pipeline:** Maps input keywords to local responses covering greetings, help instructions, creator trivia, chronological updates, and weather summaries.

## Requirements
- Python 3.x
- NLTK Library

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd <your-repo-folder-name>
   ```

2. **Install NLTK:**
   ```bash
   pip install nltk
   ```

3. **Run the script:**
   ```bash
   python chatbot.py
   ```

## Local Intents Supported
- `greeting` (e.g., "Hi", "Hello")
- `goodbye` (e.g., "Bye", "Exit")
- `help` (e.g., "Support", "Info")
- `creator` (e.g., "Who made you?")
- `year` (e.g., "What year is it?")
- `weather` (e.g., "Is it raining?")
