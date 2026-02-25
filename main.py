import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types



load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError(
        "MY_API_KEY not found. Please ensure it is defined in your .env file "
            "and that the file is in the root directory."
    )

client = genai.Client(api_key=api_key)

# read user imput after  "uv run main.py "xxxxxxx" " and add into args.user_prompt 
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

# create a new list of types.Content and set args.user_prompt as message 
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    print("Hello from CLI aiagent written in python!")


    # generate content from model and put in into response
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
    )
    # check for usage tokens and put then in x and y
    if response.usage_metadata is None:
        raise RuntimeError(
            "API Request failed or returned no usage metadata. "
            "Check your connection or safety filter settings."
        )
    x = response.usage_metadata.prompt_token_count
    y = response.usage_metadata.candidates_token_count

    # print to CLI prompt, tokens and response
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {x}")
    print(f"Response tokens: {y}")
    print(f" Response: {response.text}")

if __name__ == "__main__":
    main()
