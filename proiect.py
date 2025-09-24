!pip install langchain cohere langchain-community

from langchain_community.llms import Cohere
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from google.colab import drive
import os

drive.mount('/content/drive') #  Mount Google Drive to access the document

file_path = "/content/drive/MyDrive/Text/crow.txt"  
with open(file_path, "r") as file:
    text = file.read() # Load the text document from Google Drive

os.environ["COHERE_API_KEY"] = " ....."  # Cohere API key

prompt_template = """
Summarize the following text in two bullet points:   
{text}
"""            #Create a prompt template

llm = Cohere()
prompt = PromptTemplate(input_variables=["text"], template=prompt_template)

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run({"text": text})

print("Summarized Output in Bullet Points:")
print(result)    # Display
