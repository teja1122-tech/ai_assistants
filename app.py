from openai import OpenAI
from flask import Flask, render_template, request

client = OpenAI(api_key="your api key ")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


def answer_question(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI that answers questions clearly."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content


def summarize_text(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI that summarizes text clearly and concisely."},
            {"role": "user", "content": f"Summarize this:\n\n{user_input}"}
        ]
    )
    return response.choices[0].message.content


def generate_creative(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a creative AI that generates stories, poems, and ideas."},
            {"role": "user", "content": f"Create something based on this request:\n\n{user_input}"}
        ]
    )
    return response.choices[0].message.content


@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    task = request.form["task"]

    if task == "answer":
        output = answer_question(user_input)
    elif task == "summarize":
        output = summarize_text(user_input)
    elif task == "creative":
        output = generate_creative(user_input)
    else:
        output = "Invalid task selected."

    return render_template("index.html", output=output)


# ✅ Only ONE main block — MUST be at bottom
if __name__ == "__main__":
    app.run(debug=True)
