# Text Summarization Chatbot

This is a web app chatbot that summarizes long texts in English and Arabic using Hugging Face transformer models.  
It automatically detects the language and uses the appropriate summarization model.

## Features

- Supports English and Arabic text summarization  
- Automatic language detection  
- User-friendly chat interface built with Gradio  
- Handles unsupported languages gracefully  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ShrooqAyman/Text-Summarization-Chatbot.git
cd Text-Summarization-Chatbot
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Create a .env file in the project root and add your Hugging Face API token:
```bash
HF_TOKEN=your_huggingface_api_token
```
## Usage
Run the app:
```bash
python app.py
```
This will launch the web interface locally. Open the URL in your browser and start summarizing!

## Project Structure
* app.py — main Gradio app interface

* summarizer.py — core summarization logic and API calls

* config.py — static configs and constants

* .env — environment variables (not committed)

## License
This project is licensed under the MIT License.
