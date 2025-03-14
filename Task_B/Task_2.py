import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.express as px

# Set up the Streamlit page
st.set_page_config(page_title="Fake News Detector", layout='wide')
st.title("Fake News Detector")
st.write("Enter a news headline or article below to check if it's likely to be real or fake.")

# Load different fake news detection models with caching
@st.cache_resource
def load_model(model_name):
    if model_name == "roberta-base-openai-detector":
        return pipeline("text-classification", model="roberta-base-openai-detector")
    elif model_name == "distilbert-base-uncased":
        return pipeline("text-classification", model="distilbert-base-uncased")
    else:
        return pipeline("text-classification", model="roberta-base-openai-detector")  # Default model

# Sidebar for model selection and user feedback
with st.sidebar:
    st.header("Settings")
    model_name = st.selectbox(
        "Choose a Model",
        options=["roberta-base-openai-detector", "distilbert-base-uncased"],
        index=0,
        help="Select a pre-trained model for fake news detection."
    )
    st.header("User Feedback")
    feedback = st.radio(
        "Was the prediction accurate?",
        options=["Yes", "No"],
        index=None,
        help="Help us improve the model by providing feedback."
    )
    if feedback:
        st.write("Thank you for your feedback!")

# Load the selected model
fake_news_model = load_model(model_name)

# Initialize session state for storing historical results
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=["Text", "Prediction", "Confidence"])

# Text area for user input
user_text = st.text_area(
    "Enter your news text here",
    height=150,
    placeholder="Example:\nScientists discover a new species of dinosaur in Antarctica.",
)

if user_text:
    # Perform fake news detection
    result = fake_news_model(user_text)[0]
    label = result['label']
    score = result['score']

    # Map label to "Real" or "Fake"
    if label == "Real":
        prediction = "Real"
        fake_score = 1 - score
    else:
        prediction = "Fake"
        fake_score = score
        score = 1 - score

    # Display the prediction and confidence scores
    st.write(f"**Prediction:** {prediction}")
    st.write(f"**Confidence (Real):** {score:.2f}")
    st.write(f"**Confidence (Fake):** {fake_score:.2f}")

    # Visualize confidence with a progress bar and bar chart
    st.write("**Confidence Visualization:**")
    col1, col2 = st.columns(2)
    with col1:
        st.progress(score if prediction == "Real" else fake_score)
    with col2:
        confidence_data = pd.DataFrame({
            "Label": ["Real", "Fake"],
            "Confidence": [score, fake_score]
        })
        fig = px.bar(confidence_data, x="Label", y="Confidence", color="Label", text="Confidence")
        st.plotly_chart(fig, use_container_width=True)

    # Provide an explanation
    if prediction == "Real":
        st.success("This content is likely to be real news.")
    else:
        st.error("This content is likely to be fake news.")
    