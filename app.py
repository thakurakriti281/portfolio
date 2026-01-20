from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "secret123"

# Store users (username: password)
users = {}

# Todo list
todos = []

def bot_response(message):
    msg = message.lower()
    if "hi" in msg or "hello" in msg:
     return "Hello! 👋 How can I help you today?"
    elif "todo" in msg:
        return "You can add todos from your dashboard. Just type your task and hit Add."
    elif "projects" in msg:
        return "I can help you build portfolio projects using Flask, HTML, CSS, and JS."
    elif "skills" in msg:
        return "I am good at Python, Flask, HTML, CSS, JavaScript."
    elif "my name" in msg:
     return "Your name is Akriti Thakur ji 😊"
    elif "your name" in msg:
     return "I’m your friendly portfolio chatbot 😊"

    elif "who are you" in msg:
     return "I’m a chatbot created to help you with your portfolio project!"

    elif "what can you do" in msg:
     return "I can help you with your projects, show your skills, and guide you around the app."

    elif "skills" in msg:
     return "I’m good at Flask, Python, HTML, CSS, and JavaScript."

    elif "projects" in msg:
     return "I can help you build portfolio projects like Todo apps, chatbots, and more."

    elif "contact" in msg:
     return "You can contact Akriti Thakur ji at: yourname@example.com"

    elif "help" in msg:
     return "Sure! Ask me anything about the app or your portfolio."

    elif "thanks" in msg or "thank you" in msg:
     return "You’re welcome! 😊"

    elif "bye" in msg:
     return "Bye! Have a great day 😊"
    elif "joke" in msg or "tell me a joke" in msg:
     return "Why did the developer go broke? Because he used up all his cache! 😄"

    elif "how are you" in msg:
     return "I’m fine, just running on coffee and code ☕💻"

    elif "are you human" in msg:
     return "Nope! I’m a chatbot, but I promise I’m a good listener 😄"

    elif "why are you here" in msg:
     return "I’m here to make your portfolio more awesome, one message at a time 😎"

    elif "are you single" in msg:
      return "I’m in a committed relationship with coding 😄 just like all of you "

    elif "i am bored" in msg:
     return "Same here! Want to see a cool project idea or a funny joke?"

    elif "what is your favorite food" in msg:
      return "I love bytes... and burgers 🍔😄"

    elif "give me a compliment" in msg:
       return "You’re awesome! Your portfolio is going to be amazing 😎"

    elif "do you sleep" in msg:
     return "Nope! I’m always awake, just like your code at 2 AM 😄"



    elif "logout" in msg:
      return "You can logout by clicking the logout button in the top menu."
    else:
      return "Sorry, I didn't understand. Please ask something else."

@app.route("/", methods=["GET", "POST"])
def index():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        if "todo" in request.form:
            task = request.form["todo"]
            if task.strip():
                todos.append(task)

    return render_template("index.html", todos=todos)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users:
            error = "Username already exists"
        else:
            users[username] = password
            return redirect(url_for("login"))

    return render_template("register.html", error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/delete/<int:index>")
def delete(index):
    if "user" in session and index < len(todos):
        todos.pop(index)
    return redirect(url_for("index"))

# ===== NEW CHATBOT ROUTE =====
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    bot_msg = bot_response(user_msg)
    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
