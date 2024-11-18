import os
import tempfile
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from audio_recorder_streamlit import audio_recorder
from streamlit_util import page_header, translate_role
from gemini_util import get_llm_response, img_caption, load_gemini
from audio_util import convert_audio_to_text, convert_text_to_audio

selected: str = ""
OPTIONS: list[str] = ["ChatBot", "Analyzer", "Playground"]
ICONS: list[str] = ["chat-dots-fill", "image-fill", "robot"]

# Language options and mappings
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Urdu": "ur",
    "French": "fr",
    "Tamil": "ta",
    "Bengali": "bn",
    "Chinese": "zh-cn"
}

# Main function
def main():
    # Setting page configuration
    st.set_page_config(
        page_title="UnravelAI",
        page_icon="💠",
        layout="centered"
    )

    # Sidebar menu
    with st.sidebar:
        # Add text input for user to enter their name
        user_name = st.text_input("Enter your name", "")
        if user_name:
            st.session_state.user_name = user_name

        language = st.selectbox("Select Language", list(LANGUAGES.keys()))
        lang_code = LANGUAGES[language]
        st.markdown("<br>", unsafe_allow_html=True)

        selected = option_menu(
            menu_title="Unravel Services",
            options=OPTIONS,
            menu_icon="robot",
            icons=ICONS,
            default_index=0
        )
    # Check if the user_name is stored in session state
    user_name_display = st.session_state.get("user_name", "User") 
    if selected == OPTIONS[0]:
        # Chat history container
        page_header("💠UnravelAI", 2.0, 600)
        st.markdown("<br>", unsafe_allow_html=True)
        page_header(f"Hello {user_name_display}, Time to Unravel!", 1.8, 500)
        # Bottom input layout with record icon beside the input box
        with st.container():
            col1, col2 = st.columns([8, 1])  
            with col1:
                user_input = st.chat_input("Type or record to unravel ...")
            with col2:
                audio_data = audio_recorder(text="", icon_size="2x", key="multilingual_recorder")

        chat_container = st.container()
        
        # print("Check")
        # Handle text input
        if user_input:
            with chat_container:
                st.chat_message("user").markdown(user_input)
                response_text = get_llm_response(user_input, lang_code)
                st.chat_message("assistant").markdown(response_text)
                convert_text_to_audio(response_text, lang_code)
        # Handle audio input
        elif audio_data is not None:
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
                temp_audio_file.write(audio_data)
                temp_audio_file_path = temp_audio_file.name

            text = convert_audio_to_text(temp_audio_file_path, lang_code)
            os.remove(temp_audio_file_path)  # Remove temporary audio file

            # Display user text and get model response
            if text:
                # print("In voice")
                with chat_container:
                    st.chat_message("user").markdown(text)
                    response_text = get_llm_response(text, lang_code)
                    st.chat_message("assistant").markdown(response_text)
                    convert_text_to_audio(response_text, lang_code)

    # Image Captioning page
    if selected == OPTIONS[1]:
        page_header("📸 Unravel Images", 2.0, 600)
        st.markdown("<br>", unsafe_allow_html=True)
        image_upload = st.file_uploader("Upload the image to unravel data.", type=["jpg", "jpeg", "png"])
        
        if image_upload:
            image = Image.open(image_upload)
            resized_image = image.copy()
            resized_image.thumbnail((600, 400))  # Resize without modifying original

            if st.button("Unravel..."):
                with st.spinner('Unravelling information ...'):
                    caption = img_caption(image)

                col1, col2 = st.columns(2)
                with col1:
                    st.text("Info Decoded")
                    st.info(caption)
                with col2:
                    st.text("Image")
                    st.image(resized_image)
    
    if selected == OPTIONS[2]:
        gemini_response: str = ""
        page_header("✨ Playground", 2.0, 600)
        model = load_gemini("gemini-1.5-flash")

        if "chat_session" not in st.session_state:
            st.session_state.chat_session = model.start_chat(history=[])

        # Display chat history
        for message in st.session_state.chat_session.history:
            if message.role == "user":
                # Show only the original user input
                user_text = message.parts[0].text.split("Question:", 1)[-1].strip()
                with st.chat_message("user"):
                    st.markdown(user_text)
            else:
                # Show assistant responses
                with st.chat_message(translate_role(message.role)):
                    st.markdown(message.parts[0].text)

        user_prompt = st.chat_input("Type to unravel ...")
        if user_prompt:
            st.chat_message("user").markdown(user_prompt)

            # Creating language-specific prompt
            language_prompt = (
                f"Please answer this question in {language} language. "
                f"If the question is unclear, respond with 'I did not understand, please try again' in {language}. "
                f"Question: {user_prompt}"
            )

            response_placeholder = st.empty()

            with st.spinner('Unravelling response ...'):
                 gemini_response = st.session_state.chat_session.send_message(
                    user_prompt).text
            with response_placeholder.container():
                st.chat_message("assistant").markdown(gemini_response)

if __name__ == "__main__":
    main()
