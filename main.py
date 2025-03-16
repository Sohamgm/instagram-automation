print("Instagram bot is running!")
import os

api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from Railway

if api_key:
    print("API key loaded successfully!")
else:
    print("Error: API key not found. Check Railway environment variables.")
  
