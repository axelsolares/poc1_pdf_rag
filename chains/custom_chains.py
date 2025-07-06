import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

from utils.load_prompt_text import load_prompt_text

llm = ChatOpenAI(temperature=0, model_name=os.getenv("MODEL"))


def get_financial_chain(retriever) -> RunnableSequence:
    prompt_text = load_prompt_text("financial_assistant")
    prompt = PromptTemplate(
            input_variables=["context"],
            template=prompt_text
    )

    return (
        {"context": retriever} 
        | prompt 
        | llm 
        | StrOutputParser()
    )