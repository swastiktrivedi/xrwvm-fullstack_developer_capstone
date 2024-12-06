import requests
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Load environment variables
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_request(endpoint, **kwargs):
    params = "&".join([f"{key}={value}" for key, value in kwargs.items()]) if kwargs else ""
    request_url = f"{backend_url}{endpoint}?{params}" if params else f"{backend_url}{endpoint}"
    logger.info(f"GET from {request_url}")
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise error for non-2xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred during GET request: {e}")
        return {"error": str(e)}

def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise error for non-2xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred during sentiment analysis: {e}")
        return {"error": str(e)}

def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()  # Raise error for non-2xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred during POST request: {e}")
        return {"error": str(e)}
