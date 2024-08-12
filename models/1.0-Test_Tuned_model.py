"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("API_KEY")


model = genai.GenerativeModel("tunedModels/wallmart-test-model-4j0kh9gb3l6r")
response = model.generate_content("Should we restock Wine Glass? Its current stock is 535 units, and its RestockUrgency is 10.00.")
print(response.text)
