from fastapi import FastAPI
from openai import OpenAI

client = OpenAI()
app = FastAPI()


@app.get("/create_title/{interests}")
async def read_interests(interests: str):
    
    interest_list = interests.split('-')

    prompt = "Write 1 interesting title (interrogative sentence) related to " + \
      ", ".join(interest_list) + " that can attract people to engage in discussions based on it."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = completion.choices[0].message.content
    text = text[1:len(text)-1]

    return {"title": text}
