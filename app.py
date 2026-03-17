
from flask import Flask, render_template, request, redirect
from models import Question, CBT

app = Flask(__name__)

quiz = CBT()

quiz.add_question(Question(
    "What is the capital of Nigeria?",
    ["Lagos", "Abuja", "Kano", "Kaduna"],
    "Abuja"
))

quiz.add_question(Question(
    "Python is a?",
    ["Snake", "Programming Language", "Car", "Game"],
    "Programming Language"
))
quiz.add_question(Question(
    "What does CPU stand for?",
    ["Central Processing Unit", "Computer Personal Unit", "Central Power Unit", "Control Processing Unit"],
    "Central Processing Unit"
))

quiz.add_question(Question(
    "Which language is used with Flask?",
    ["Java", "Python", "C++", "PHP"],
    "Python"
))

quiz.add_question(Question(
    "Which data structure uses FIFO?",
    ["Stack", "Queue", "Tree", "Array"],
    "Queue"
))

current_question = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def take_quiz():
    global current_question

    if request.method == "POST":
        answer = request.form.get("answer")
        if current_question and current_question.check_answer(answer):
            quiz.score += 1

    current_question = quiz.get_next_question()

    if current_question is None:
        return redirect("/result")

    return render_template("quiz.html", question=current_question)

@app.route("/result")
def result():
    score, time = quiz.submit_result()
    return render_template("result.html", score=score, time=time)

if __name__ == "__main__":
    app.run(debug=True)
