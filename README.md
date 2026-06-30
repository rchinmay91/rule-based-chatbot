# Local NLP Chatbot

A simple, rule-based conversational chatbot built entirely using **Python** and the **

Natural Language Toolkit (NLTK)

** library. This application processes text inputs locally without using external cloud infrastructure, tokens, or API keys.

## Features

- **Tokenization:** Breaks down user text strings into discrete word tokens.
- **Punctuation Removal:** Filters out structural punctuation marks to streamline text processing.
- **Stop Words Filtering:** Automatically drops common filler words (e.g., "the", "is", "at") to highlight core vocabulary.
- **Lemmatization:** Restores remaining words to their base vocabulary form for cleaner keyword classification.
- **Intent Matching Pipeline:** Maps input keywords to local responses covering greetings, help instructions, creator trivia, chronological updates, and weather summaries.

## Pipeline Architecture

The following flowchart illustrates how user input passes through the local NLP preprocessing steps to trigger the correct intent response:

```text
[ User Input Text ]
        │
        ▼
┌─────────────────────────┐
│     Tokenization        │ ──► Splits text into individual words
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│   Punctuation Removal   │ ──► Strips characters like ?, !, ., ,
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│  Stop Words Filtering   │ ──► Removes filler words (e.g., "is", "the")
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│      Lemmatization      │ ──► Reductions to base form (e.g., "running" -> "run")
└─────────────────────────┘
        │
        ▼
┌─────────────────────────┐
│ Intent Keyword Matching │ ──► Compares processed tokens against intent dictionaries
└─────────────────────────┘
        │
        ▼
[ Hardcoded Local Reply ]
```

## Requirements

- Python 3.x
- NLTK Library

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd rule-based-chatbot
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

## License

This project is licensed under the MIT License:

```text
MIT License

Copyright (c) 2026 rchinmay91

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
