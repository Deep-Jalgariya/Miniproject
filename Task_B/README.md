# Fake News Detector

## Overview
This is a **Streamlit-based web application** for detecting fake news using **pre-trained NLP models**. Users can input a news headline or article, and the application will predict whether the content is likely to be real or fake.

## Features
- Uses **Hugging Face's transformers** to load text classification models.
- Supports multiple models: `roberta-base-openai-detector` and `distilbert-base-uncased`.
- Provides **confidence scores** for predictions.
- Includes **interactive visualizations** with Plotly.
- Allows users to give **feedback** on prediction accuracy.


## Installation
### Prerequisites
Ensure you have Python installed (>=3.7). Then, install the required dependencies:
```bash
pip install streamlit transformers pandas plotly
```

## Usage
Run the Streamlit app with:
```bash
streamlit run Task_2.py
```

## Application Workflow
1. **User Input**: Enter a news headline or article.
2. **Model Selection**: Choose between `roberta-base-openai-detector` and `distilbert-base-uncased`.
3. **Prediction**: The selected model analyzes the text and returns a prediction with confidence scores.
4. **Visualization**: The confidence levels are displayed using a progress bar and bar chart.
5. **User Feedback**: Users can confirm or reject the prediction to improve future models.