from dotenv import load_dotenv
import os
load_dotenv()

print(os.environ["GROQ_API_KEY"])

# Here i am using customized model

#from groq import Groq

# client = Groq()

# response = client.chat.completions.create(
#     model="meta-llama/llama-4-scout-17b-16e-instruct",
#     messages=[
#         {
#             "role": "user",
#             "content": "tell me joke,i can't stop laugh"
#         }
#     ],
#     temperature=0.7,
#     max_tokens=100,
# )

# print(response.choices[0].message.content)

## Here i am used standard library(LANGCHAIN FOR BETTER)
#1. Take User Question
user_question=input("Enter Your Question: ")

#2. Convert to Prompt
from langchain.prompts import PromptTemplate

text = """You are a Career Coach in AI Field. Answer Best Advice to candidate. Dont give cliche answers
Below is user question:
{question}

"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=text
)


#3. Make LLM Call
from langchain_groq import ChatGroq



llm = ChatGroq(
    model="llama-3.1-8b-instant"

)

#Create chain
chain=prompt | llm

#4. Response
result=chain.invoke({"question":user_question})
print(result.content)