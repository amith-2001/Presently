from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.chains import ConversationChain

load_dotenv()

chatgpt = OpenAI()
conversation = ConversationChain(llm=chatgpt)

def chatbot(query) -> str:
    answer = conversation.predict(input = query)
    return answer


if __name__ == '__main__':
    #testing function
    print(chatbot("what is ai?"))
