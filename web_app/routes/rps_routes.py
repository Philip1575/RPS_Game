import random

from flask import Blueprint, render_template, request

from app.rps import VALID_OPTIONS, determine_winner


rps_routes = Blueprint("rps_routes", __name__)


@rps_routes.route("/rps", methods=["GET", "POST"])
def play():
    if request.method == "GET":
        return render_template("rps.html", options=VALID_OPTIONS)

    user_choice = request.form.get("user_choice", "")
    if user_choice not in VALID_OPTIONS:
        return render_template(
            "rps.html", options=VALID_OPTIONS,
            error="Please choose rock, paper, or scissors.",
        ), 400

    computer_choice = random.choice(VALID_OPTIONS)
    return render_template(
        "rps.html", options=VALID_OPTIONS,
        user_choice=user_choice, computer_choice=computer_choice,
        winner=determine_winner(user_choice, computer_choice),
    )
