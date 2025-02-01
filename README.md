# Linguify - Language Translation App
Linguify is a simple and intuitive language translation app built with Streamlit and LangChain. The app uses the Ollama model for real-time translation between various languages.

## Features
- **Wide Language Support:** Translate between a wide range of languages, including English, Hindi, Spanish, Mandarin, Arabic, and more.
- **Real-Time Translation:** Enter a sentence, and instantly see the translated version in the selected output language.
- **User-Friendly Interface:** Clean and simple interface for easy navigation and translation.
- **Powered by LangChain:** Utilizes LangChain's integration with the Ollama model for accurate translations.

## Installation
To run Linguify locally, follow these steps:

Clone the repository:

```bash

git clone https://github.com/your-username/linguify.git
cd linguify

```
Install the necessary dependencies:
```bash
pip install -r requirements.txt
Create a .env file and add your necessary environment variables (e.g., API keys, if applicable).
```
Run the app:

```bash
streamlit run app.py
```
## How to Use
- Select the input language and output language from the dropdown menus.
- Enter a sentence in the input text area.
- Click the Translate button to see the translated text in the output area.
- Libraries and Tools Used
- Streamlit: Framework for building the web app.
- LangChain: Used for chaining models and generating prompts for translation.
- Ollama (llama3.2 model): The language model used for performing translations.
