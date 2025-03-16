import os
import openai

print("Instagram bot is running!")

# Load the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: API key not found. Check Railway environment variables.")
    exit(1)

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)

# Example prompt for AI-generated content
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Change to "gpt-4" if needed
        messages=[{"role": "system", "content": "You are an AI assistant."},
                  {"role": "user", "content": "Generate a creative Instagram post idea."}]
    )

    # Print the response
    post_content = response.choices[0].message.content
    print("Generated Instagram Post:", post_content)

except openai.OpenAIError as e:
    print(f"❌ OpenAI API Error: {e}")

