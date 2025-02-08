from flask import Flask, render_template, json, request
import random

app = Flask(__name__)

# Load messages
def load_messages():
    with open("messages.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route("/")
def home():
    messages = load_messages()
    return render_template("index.html", messages=messages)

@app.route("/<day>")
def valentine_day(day):
    messages = load_messages()
    print(messages)
    print(day)
    if day in messages:
        return render_template(f"{day}.html", message=messages[day])
    return "Page not found", 404

@app.route("/love-calculator", methods=["POST"])
def love_calculator():
    name1 = request.form.get("name1", "").strip().lower()
    name2 = request.form.get("name2", "").strip().lower()

    if name1 != "princess" or name2 != "jadu":
        error_msg = "😜 Naughty Naughty! The only true love is between Princess & Jadu! Try again!"
        return render_template("index.html", error=error_msg)

    love_score = random.randint(80, 100)  # Making sure love is always high!
    return render_template("index.html", love_score=love_score)


if __name__ == "__main__":
    app.run(debug=True)
