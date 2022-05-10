from flask import render_template, request, Blueprint, g

from app.ufi_database import updatedRiskLevel
from flask_login import current_user

site = Blueprint('site', __name__)

questions = [
    {
        "id": "1",
        "question": "What is your investment attitude?",
        "answers": ["a) Conservative", "b) Moderate", "c) Aggressive"],
        "correct1": "a) Conservative",
        "correct2": "b) Moderate",
        "correct3": "c) Aggressive"
    },
    {
        "id": "2",
        "question": "In how many years will you begin making withdrawals from your investment?",
        "answers": ["a) more than 15", "b) 10 - 15", "c) less than 5"],
        "correct1": "a) more than 15",
        "correct2": "b) 10 - 15",
        "correct3": "c) less than 5"
    },
    {
        "id": "3",
        "question": "Protecting my portfolio is more important to me than high returns.",
        "answers": ["a) Agree", "b) Neutral", "c) Disagree"],
        "correct1": "a) Agree",
        "correct2": "b) Neutral",
        "correct3": "c) Disagree"
    },
    {
        "id": "4",
        "question": "Keeping the above answer option in mind which of the following statements make the most "
                    "sense to you?",
        "answers": ["a) To completely avoid losses is something I am more interested in.",
                    "b) I am concerned about losses along with returns.",
                    "c) I am willing to bare the consequences of loss to maximize my returns."],
        "correct1": "a) To completely avoid losses is something I am more interested in.",
        "correct2": "b) I am concerned about losses along with returns.",
        "correct3": "c) I am willing to bare the consequences of loss to maximize my returns."
    },
    {
        "id": "5",
        "question": "Which of the following statements best describes your investment philosophy?",
        "answers": ["a) I feel comfortable with stable investments",
                    "b) I am seeking substantial investment returns",
                    "c) I am seeking potentially high investment returns"],
        "correct1": "a) I feel comfortable with stable investments",
        "correct2": "b) I am seeking substantial investment returns",
        "correct3": "c) I am seeking potentially high investment returns"
    }
]


@site.route("/survey", methods=['POST', 'GET'])
def survey():
    if request.method == 'GET':
        return render_template("survey_questions.html", data=questions)

    else:
        result = 0
        for question in questions:
            if request.form[question.get('id')] == question.get('correct1'):
                result += 1

            elif request.form[question.get('id')] == question.get('correct2'):
                result += 2

            else:
                result += 3

        if (result >= 5 and result < 9):
            riskLevel = "Low"

        elif (result >= 9 and result < 12):
            riskLevel = "Medium"

        elif (result >= 12 and result <= 15):
            riskLevel = "High"

        updatedRiskLevel(current_user.userEmail, riskLevel)

        return render_template('survey_results.html', result=riskLevel)
