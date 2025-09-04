from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are an exper in answering questions about a pizza restaurant.
Here are some relevant reviews:  {reviews}
Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model


while True:

    question = input("What would you like to answer? q for quite\n")
    if question == "q":
        break
    result = chain.invoke({
        "reviews": [],
        "question": "What is the best pizza place in town?",
    })

    print(result)