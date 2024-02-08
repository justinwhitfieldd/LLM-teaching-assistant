import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPEN_AI_API_KEY')
model_engine = "gpt-3.5-turbo-1106"
promptFile = open('prompt.txt', 'r')
prompt = promptFile.read()

GPT_messages = [
    {"role": "system", "content": prompt}
]

def get_response(userInput):

    GPT_messages.append({"role": "user", "content": userInput})
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=GPT_messages,
        temperature=0.5,
        #functions=GPT_functions,
        #function_call="auto", 
    )
    GPT_response = response['choices'][0]['message']['content']  # Navigate through 'choices', then 'message', to extract 'content'
    GPT_messages.append({"role": "assistant", "content": GPT_response})

    return GPT_response

#test
print(get_response("How are you?"))