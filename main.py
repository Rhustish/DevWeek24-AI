from langchain_community.llms import HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"]


def operate(question):

    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate.from_template(template)
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

    llm = HuggingFaceEndpoint(
        repo_id=repo_id, temperature=0.5, token=HUGGINGFACEHUB_API_TOKEN
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm, output_key="text" , verbose=False)
    return llm_chain.invoke(question)

