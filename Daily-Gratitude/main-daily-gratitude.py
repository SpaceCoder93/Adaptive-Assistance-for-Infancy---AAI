from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv('.env')
openai_api_key = os.getenv('OPENAI_APIKEY')
for i in range(10):
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    answer = llm.invoke("""Give me a list of 10 daily gratitudes and quotes for a new mother suffereing from post partum depression. Don't give any reference or pretext.""")
    print(answer)