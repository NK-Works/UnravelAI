# 💠 UnravelAI

UnravelAI is an innovative multi-functional AI platform that provides services such as a chatbot for conversational AI, image captioning, and more. With support for multiple languages, users can interact with the system either via text or voice, allowing for a seamless experience.

## 🚀 Features

- **Chatbot**: Engage with an AI-powered chatbot for answering questions and generating responses based on user input.
- **Image Analysis**: Upload images and receive proper analysis describing the content of the images.
- **Voice Interaction**: Record voice input, which is then transcribed and processed to generate responses.
- **Multilingual Support**: Supports various languages, including English, Hindi, Urdu, French, and more.
- **User-Friendly Interface**: Built with a modern UI using **Streamlit**, making it easy for users to interact with the AI.

## 🛠️ Technologies Used

- **Python**: Backend logic and AI models.
- **Streamlit**: For the frontend UI.
- **Audio Recorder Streamlit**: Used for voice input functionality.
- **Pillow (PIL)**: Image handling and captioning.
- **Gemini API**: AI language model for generating responses.
- **Other Python Libraries**:
  - `os` for file handling
  - `tempfile` for creating temporary files
  - `streamlit_option_menu` for the sidebar menu
  - `streamlit_util` for utility functions like headers and other custom components

## 📦 Installation

To run the project locally, follow these steps:

### Prerequisites

1. Python 3.x
2. Streamlit
3. Other required dependencies

Check out [requirements.txt](requirements.txt) for more details.

### Steps

### 1. Clone the repository

```bash
git clone https://github.com/username/UnravelAI.git
cd UnravelAI
```

### 2. Install the required dependencies:

- Ensure you have Python 3.8 or above. Install dependencies using `pip`.

  ```bash
  pip install -r requirements.txt
  ```

### 3. Set up your environment:

- You'll need an API key from Google’s generative AI services. Set it up in your environment.

  ```bash
  export API_KEY='your_api_key_here'
  ```

### 4. Run the application:

- Start the Streamlit app.

  ```bash
  streamlit run main.py
  ```

## 📈 License

This project is licensed under the [MIT](https://opensource.org/license/mit/) License. Check the [LICENSE](LICENSE) file for more details.
