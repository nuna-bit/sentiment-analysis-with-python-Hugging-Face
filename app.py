import gradio as gr
from textblob import TextBlob

def analyze_sentiment(text):
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

demo.launch()
