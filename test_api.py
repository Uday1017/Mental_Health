import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
print(f"Using API key: {api_key}")

# Configure Gemini
genai.configure(api_key=api_key)

# Test the API
try:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content('Say hello!')
    print("Response:", response.text)
    print("API test successful!")
except Exception as e:
    print(f"Error testing API: {e}") 