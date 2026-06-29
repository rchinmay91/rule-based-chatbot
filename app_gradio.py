import gradio as gr
import chatbot  # Imports your core logic cleanly

def chatbot_interface(user_message, history):
    if not user_message.strip():
        return "Please type something!"
    
    # 1. Run text preprocessing
    processed_tokens = chatbot.preprocess_text(user_message)
    
    # 2. Extract intent and reply
    intent, bot_reply = chatbot.match_intent(processed_tokens)
    
    # 3. Return the string reply
    return bot_reply

# Launch Gradio interface safely
if __name__ == "__main__":
    print("Launching local Gradio web server...")
    
    # We remove theme="soft" from here to prevent the TypeError
    demo = gr.ChatInterface(
        fn=chatbot_interface,
        title="🤖 Local NLP Chatbot (Gradio Interface)",
        description="Type a message to interact with your offline rule-based NLTK agent."
    )
    
    # We apply the soft theme inside the launch wrapper instead
    demo.launch(server_name="127.0.0.1", server_port=8080, theme="soft")
