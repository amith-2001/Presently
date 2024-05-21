
import openai
import os
from dotenv import load_dotenv
from head_extractor import head_returner
# load_dotenv()
# openai.api_key = os.environ['OPENAI_API_KEY']


# Initialize the session history
session_history = []


def generate_echarts_code(df_data):
    # Ensure your API key is correctly configured in your environment variables or set directly here
    openai.api_key = 'sk-proj-n7yvH7N0VzPQJZAZrc0kT3BlbkFJIPCZ3vyPrsAwSFJ1rhB8'

    # Append the user's request to the session history
    session_history.append({"role": "user", "content": f"Generate ECharts code for {df_data}."})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                     {"role": "system",
                      "content": "You are a coding assistant specialized in generating ECharts JavaScript code for given df.head() data.Give only the code starting from <!DOCTYPE>"}
                 ] + session_history  # Include the session history in the request
    )

    # Append the model's response to the session history
    if response.choices:
        generated_code = response.choices[0].message['content']
        print("Generated ECharts Code:\n", generated_code)
        session_history.append({"role": "assistant", "content": generated_code})
    else:
        print("No code generated.")


# Example usage
generate_echarts_code(head_returner())  # First request
# generate_echarts_code("pie")  # Subsequent request that remembers the first