# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# from langchain.chains import ConversationChain

# load_dotenv()

# chatgpt = OpenAI(model="gpt-3.5-turbo")
# conversation = ConversationChain(llm=chatgpt)

# def chatbot(query) -> str:
#     answer = conversation.predict(input = query)
#     return answer


# if __name__ == '__main__':
#     #testing function
#     print(chatbot("only give me code, give me code to create aline graph usign echarts"))


import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

def generate_echarts_code(chart_name):
    # Ensure your API key is correctly configured in your environment variables or set directly here
    # openai.api_key = 'your-openai-api-key'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a coding assistant specialized in generating ECharts code embedded in html"},
            {"role": "user", "content": f"Generate ECharts code for a {chart_name} chart."}
        ]
    )

    # Extracting the message content from the response
    if response.choices:
        generated_code = response.choices[0].message['content']
        print("Generated ECharts Code:\n", generated_code)
    else:
        print("No code generated.")

# Example usage
chart_name = "bar"  # You can change this to any type of chart: line, pie, scatter, etc.
generate_echarts_code(chart_name)