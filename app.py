import gradio as gr
from textblob import TextBlob
import nltk

# These downloads are required for TextBlob to function in a fresh container
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

def analyze_sentiment(text):
    if not text.strip():
        return "Please enter some text."
        
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    return f"Sentiment: {sentiment} (Polarity: {round(polarity, 2)})"

# Create the user interface
demo = gr.Interface(
    fn=analyze_sentiment, 
    inputs="text", 
    outputs="text",
    title="Simple TextBlob Sentiment Analyzer",
    description="Enter text to check its sentiment using TextBlob!"
)

# On Hugging Face, the app must listen on 0.0.0.0 and port 7860
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
