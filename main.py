import os
import openai

print("Instagram bot is running!")

api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from Railway

if api_key:
    print("✅ API key loaded successfully!")
    openai.api_key = api_key

    # Test OpenAI API with a simple request
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Say Hello!"}]
        )
        print("OpenAI Response:", response["choices"][0]["message"]["content"])
    except Exception as e:
        print("❌ OpenAI API Error:", e)

else:
    print("❌ Error: API key not found. Check Railway environment variables.")
