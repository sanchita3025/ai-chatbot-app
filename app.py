from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]

    if user_message.lower() == "hi":
        reply = "Hello! How can I help you?"
    elif user_message.lower() == "bye":
        reply = "Goodbye! Have a nice day."
    else:
        reply = "I am still learning."

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)