import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.vector_utils import query_vector_with_summary
import json
load_dotenv()
model_engine = "gpt-3.5-turbo-1106"
promptFile = open('prompt.txt', 'r')
prompt = promptFile.read()
client = OpenAI(api_key = os.getenv('OPEN_AI_API_KEY'))

GPT_messages = [
    {"role": "system", "content": prompt}
]

# def get_response(userInput):

#     GPT_messages.append({"role": "user", "content": userInput})
#     response = openai.ChatCompletion.create(
#         model=model_engine,
#         messages=GPT_messages,
#         temperature=0.5,
#         tools=GPT_tools,
#         tool_choice="auto", 
#     )
#     GPT_response = response['choices'][0]['message']['content']  # Navigate through 'choices', then 'message', to extract 'content'
#     GPT_messages.append({"role": "assistant", "content": GPT_response})

#     return GPT_response

GPT_tools = [
    {
        "type": "function",
        "function": {
            "name": "vector_search",
            "description": "Queries a vector database, returns most similar text to provide context",
            "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string","description": "this is your question that similar text containing valuble information will be found for.",},
                        },
                    },
        },
    },
]
def get_response_wFunction(userInput):
    GPT_messages.append({"role": "user", "content": userInput})
    response = client.chat.completions.create(
        model=model_engine,
        messages=GPT_messages,
        temperature=0.5,
        tools=GPT_tools,
        tool_choice="auto", 
    )

    GPT_response = response.choices[0].message
    tool_calls = GPT_response.tool_calls
    if tool_calls:
        available_functions = {
            "vector_search": query_vector_with_summary,
        }
        GPT_messages.append(GPT_response) 
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(query=function_args.get("query"),)
            print("\n\n\n FUCNTION RESPONSE ",function_response,"\n\n\n func respons")
            GPT_messages.append(
            {
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })  

        # get a new response from the model where it can see the function response
        second_response = client.chat.completions.create(
            model=model_engine,
            messages=GPT_messages,
            temperature=0.5,
            tools=GPT_tools,
            tool_choice="auto", 
        )
        print("\n\n\n gpt messages",GPT_messages,"\n\n gpt messages")
        return second_response.choices[0].message.content
        
    return GPT_response.content
