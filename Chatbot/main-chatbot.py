from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import json

def lambda_handler(event, context):
    load_dotenv('.env')
    openai_api_key = os.getenv('OPENAI_APIKEY')
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    prompt_template = PromptTemplate(
        input_variables=['question', 'age'],
        template="""
            You are an expert in the field of postnatal care.
            I am a mom.
            The baby is {age}.
            Can you help me with: {question}.
        """
    )
    chain_input = {
        "question": event['question'],
        "age": event['age']
    }
    chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = chain.invoke(chain_input)
    answer = answer['text']
    answer = str(answer)
    answer = answer.replace("\n", "")
    return {
        'statusCode': 200,
        'body': json.dumps(answer)
    }