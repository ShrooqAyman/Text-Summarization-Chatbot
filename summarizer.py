import requests
from dotenv import load_dotenv
from langdetect import detect
from config import AR_MODEL_API_URL, EN_MODEL_API_URL, HEADERS, LANGUAGE_NOT_SUPPORTED_MESSAGE


def switch_model(text:str)->str:
    """
    Detects the language of the input text and returns the appropriate API URL.

    Args:
        text (str): The input text provided by the user.

    Returns:
        str | None: The API URL for the model or None if language not supported.
    """
    lang = detect(text)
    if lang == 'ar':
        return AR_MODEL_API_URL
    elif lang == 'en':
        return EN_MODEL_API_URL
    else:
        return None


def summarize_text(text:str, history:list)->str:
    """
    Generates a summary for the input text using Hugging Face Inference API.

    Args:
        text (str): The text to be summarized.
        history (list): Chat history.

    Returns:
        str: The summarized text, or an error message if the API call fails.
    """
    model_url = switch_model(text)
    if model_url is None:
        return  LANGUAGE_NOT_SUPPORTED_MESSAGE
    payload = {"inputs": text}
    try:
        response = requests.post(model_url, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

    if isinstance(result, dict) and "error" in result:
        return f"API error: {result['error']}"

    if isinstance(result, list) and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        return "Unexpected response format."
    
