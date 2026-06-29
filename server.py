from flask import Flask, render_template, request, jsonify
import chatbot  # This imports the chatbot.py file you just shared!

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    try:
        user_data = request.get_json() or {}
        user_message = user_data.get("message", "")
        
        if not user_message.strip():
            return jsonify({"response": "Please type something!"})
        
        # 1. Run the preprocessing text function from your file
        processed_tokens = chatbot.preprocess_text(user_message)
        
        # 2. MATCH YOUR TUPLE: Safely unpack BOTH intent and bot_reply
        intent, bot_reply = chatbot.match_intent(processed_tokens)
        
        # 3. Return only the response string back to index.html
        return jsonify({"response": bot_reply})
        
    except Exception as e:
        print(f"Backend Server Error: {e}")
        return jsonify({"response": f"Server processing error: {str(e)}"})

if __name__ == "__main__":
    print("Starting local development web server on port 8080...")
    app.run(debug=True, port=8080)
