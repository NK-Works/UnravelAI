import streamlit as st
import google.generativeai as genai
from PIL import Image

# Retrieve API key from Streamlit secrets
GEMINI_API_KEY = st.secrets['gemini']['api_key']
genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 10,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

def load_gemini(model_name: str) -> genai.GenerativeModel:
    """Returns the Gemini Pro Generative model."""
    
    model: genai.GenerativeModel = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
    )
    return model

# Get LLM response in selected language
def get_llm_response(text, lang_code):
    prompt = f"""Please answer this question in {lang_code} language. 
    If the question is unclear, respond with 'I did not understand, please try again' in the selected language.
    Make sure that the answer is within 50 words and makes the point clear and precise.
    Question: {text}"""

    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )
        chat_session = model.start_chat()
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error while fetching response from LLM: {e}")
        return "Sorry, there was an error processing your request."

def img_caption(image: Image.Image) -> str:
    """Returns the response for image captioning prompt."""
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )
        caption: str = model.generate_content(
            ["Analyse the image and show the details that you can see in the image in 50 words max", image]).text or ""
        return caption
    except Exception as e:
        st.error(f"Error while fetching response from LLM: {e}")
        return "Sorry, there was an error processing your request."
