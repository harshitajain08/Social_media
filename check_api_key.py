import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Ensure the API key is available
if not openai_api_key:
    print("API key is missing. Please check your .env file.")
    exit(1)

# Set the OpenAI API key
openai.api_key = openai_api_key

def is_api_key_valid():
    try:
        # Create a client instance
        client = openai.Client()

        # Attempt to list available models to check if the key is valid
        models = client.models.list()
        print("API Key is valid.")
        return True
    except openai.error.AuthenticationError as e:  # Catch authentication errors specifically
        print(f"Authentication error: {e}")
        return False
    except openai.error.OpenAIError as e:  # Catch any other OpenAI errors
        print(f"An OpenAI API error occurred: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    is_api_key_valid()