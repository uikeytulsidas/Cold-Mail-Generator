# import os
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.llms import Groq  # or Groq via wrapper

# # Initialize your LLM (example with OpenAI)
# llm = Groq(api_key=os.getenv("GROQ_API_KEY"), temperature=0.7)

# # Create a prompt template
# prompt = PromptTemplate(
#     input_variables=["name", "role", "company", "product"],
#     template="Write a concise, personalized cold email for {name}, who is a {role} at {company}. Highlight the product: {product}."
# )

# # Create the chain
# email_chain = LLMChain(llm=llm, prompt=prompt)

# # Function to generate email
# def generate_cold_email_lc(name, role, company, product):
#     result = email_chain.run(name=name, role=role, company=company, product=product)
#     return result
