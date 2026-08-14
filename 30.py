# from dotenv import load_dotenv
# import os

# load_dotenv()

# groq_key = os.getenv("GROQ_API_KEY")
# mistral_key = os.getenv("MISTRAL_API_KEY")

# if groq_key and mistral_key:
#     print("API keys loaded successfully!")
# else:
#     print("API keys are missing.")
# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant"
# )

# prompt = "Introduce yourself in 3 sentences."

# response = llm.invoke(prompt)

# print(response.content)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.2,
#     max_tokens=50
# )

# prompt = "Introduce yourself in 3 sentences."

# response = llm.invoke(prompt)

# print(response.content)
# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI

# load_dotenv()

# llm = ChatMistralAI(
#     model="mistral-small-2603"
# )

# prompt = "Explain what is Artificial Intelligence in simple words."

# response = llm.invoke(prompt)

# print(response.content)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_mistralai import ChatMistralAI

# load_dotenv()

# groq = ChatGroq(
#     model="llama-3.1-8b-instant"
# )

# mistral = ChatMistralAI(
#     model="mistral-small-2603"
# )

# question = "What are the advantages of using LangChain?"

# groq_response = groq.invoke(question)
# mistral_response = mistral.invoke(question)

# print("===== Groq Response =====")
# print(groq_response.content)

# print("\n===== Mistral Response =====")
# print(mistral_response.content)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# prompt = "Write a short creative story about a robot learning to cook."

# temperatures = [0.1, 0.7, 1.2]

# for temp in temperatures:
#     llm = ChatGroq(
#         model="llama-3.1-8b-instant",
#         temperature=temp
#     )

#     response = llm.invoke(prompt)

#     print(f"\n===== Temperature: {temp} =====")
#     print(response.content)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant"
# )

# print("Chatbot started!")
# print("Type 'exit' to stop.")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         print("Chatbot stopped.")
#         break

#     response = llm.invoke(user_input)

#     print("Bot:", response.content)
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant"
# )

# def explain_topic(topic):
#     prompt = f"""
# Explain the topic: {topic}

# Give the answer in the following format:

# Definition:
# Write a short definition.

# Key Points:
# 1. Point one
# 2. Point two
# 3. Point three

# Real-Life Example:
# Give one real-life example.
# """

#     response = llm.invoke(prompt)
#     return response.content


# print(explain_topic("Machine Learning"))
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_mistralai import ChatMistralAI
# import os

# load_dotenv()

# groq_key = os.getenv("GROQ_API_KEY")
# mistral_key = os.getenv("MISTRAL_API_KEY")

# if not groq_key and not mistral_key:
#     print("Error: No API keys found in .env")
#     exit()

# print("================================")
# print("   Multi-Model AI Assistant")
# print("================================")
# print("Choose: groq or mistral")
# print("Type 'quit' to exit.")

# while True:
#     choice = input("\nChoose model: ").lower()

#     if choice == "quit":
#         print("Program ended.")
#         break

#     if choice not in ["groq", "mistral"]:
#         print("Invalid choice. Choose groq or mistral.")
#         continue

#     question = input("Enter your question: ")

#     if question.lower() == "quit":
#         print("Program ended.")
#         break

#     try:
#         if choice == "groq":
#             if not groq_key:
#                 print("Groq API key is missing.")
#                 continue

#             model = ChatGroq(
#                 model="llama-3.1-8b-instant"
#             )

#         else:
#             if not mistral_key:
#                 print("Mistral API key is missing.")
#                 continue

#             model = ChatMistralAI(
#                 model="mistral-small-2603"
#             )

#         response = model.invoke(question)

#         print("\nAI Response:")
#         print(response.content)

#     except Exception as e:
#         print("\nError:", e)