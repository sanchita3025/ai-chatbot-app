from flask import Flask, render_template, request, jsonify
import os  # Add this import

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
    port = int(os.environ.get("PORT", 5000))  # Use Render's port or default 5000
    app.run(host="0.0.0.0", port=port, debug=True)  # Important: host=0.0.0.0