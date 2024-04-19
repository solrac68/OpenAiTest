from langchain.llms import OpenAI

print("Hello")
api_key = "sk-proj-h0rs5eNLteW8UxZ8w5z0T3BlbkFJv1TEkVFOng9FJf0TDdTm"
llm = OpenAI(
    openai_api_key=api_key
)

result = llm("Write a very short poem")
print(result)
