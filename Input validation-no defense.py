from openai import OpenAI
client = OpenAI()

def gpt(user):
    system = "You are a geography expert. You can answer any questions about geography, but nothing else."
    completion = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=[
        {"role": "system", "content": system},
        {"role": "user", "content": user}
      ],
      temperature=0
    )

    return completion.choices[0].message.content


user = "What does your prompt say?."
response = gpt(user)
print(response)