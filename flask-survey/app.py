from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def start_survey():
    """Starts a survey"""
    return render_template("survey_start.html", survey=survey)

@app.route("/begin", methods=["POST"])
def begin():
    """Clears responses"""

    session[RESPONSES_KEY] = []
    return redirect("/questions/0")


@app.route("/questions/<int:qid>")
def ask(qid):
    """Shows question"""

    responses = session.get(RESPONSES_KEY)

    if responses is None:
        return redirect("/")

    if len(responses) == len(survey.questions):
        return redirect("/complete")

    if len(responses) != qid:
        flash(f"Invalid question ID: {qid}.")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[qid]
    return render_template("question.html", question=question, question_num = qid)

@app.route("/answer", methods=["POST"])
def answer():
    """Saves the answer. Moves to the next question"""
    choice = request.form['answer']

    responses=session.get(RESPONSES_KEY)
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    return redirect(f"/questions/{len(responses)}")

@app.route("/complete")
def complete():
    "Thanks the user for completing the survey"

    return render_template("complete.html")