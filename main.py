import os
import argparse
from dotenv import load_dotenv # type: ignore
from google import genai # type: ignore
from google.genai import types # type: ignore
from prompts import *
from functions.call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError(
        "API_KEY not found. Please ensure it is defined in your .env file "
            "and that the file is in the root directory."
    )

client = genai.Client(api_key=api_key)

# read user imput after  "uv run main.py "xxxxxxx" " and add into args.user_prompt 
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# create a new list of types.Content and set args.user_prompt as message 
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    print("Hello from CLI aiagent written in python!")

    # generate content from model and put in into response
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt)
    )
    # check for usage tokens and put then in x and y
    if response.usage_metadata is None:
        raise RuntimeError(
            "API Request failed or returned no usage metadata. "
            "Check your connection or safety filter settings."
        )
    
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    # check if --verbose flag is included then prompt, tokens and response
    if args.verbose: 
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    
    # print response if not function calls were made Ai Agent
    if not response.function_calls:
        print(f" Response: {response.text}")
        return
    
    # list to hold successfully validated function results
    function_results = []
    
    # iterate over the function call requested by the model
    for function_call in response.function_calls:
        function_call_result = call_function(function_call, verbose=args.verbose)

        # ensure parts list is not empty
        if not function_call_result.parts:
            raise RuntimeError(f"Error: Function call result for {function_call.name} has no parts.")
         
        first_part = function_call_result.parts[0]

        if first_part.function_response is None:
            raise RuntimeError(f"Error: Part for {function_call.name} is missing 'function_response'.")
        if first_part.function_response.response is None:
            raise RuntimeError(f"Error: Function response for {function_call.name} is missing 'response' data.")
        
        function_results.append(first_part)

        if args.verbose:
            print(f"-> {first_part.function_response.response}")

    # print function call with name and args
    #for function_call in response.function_calls:
    #    print(f"Calling function: {function_call.name}({function_call.args})")

if __name__ == "__main__":
    main()
