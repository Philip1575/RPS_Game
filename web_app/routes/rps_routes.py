# this is the "web_app/routes/rps_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.rps import VALID_OPTIONS, determine_winner, generate_random_choice


rps_routes = Blueprint("rps_routes", __name__)


@rps_routes.route("/rps/form")
def rps_form():
    print("RPS FORM...")
    return render_template("rps_form.html", options=VALID_OPTIONS)


@rps_routes.route("/rps/results", methods=["POST"])
def rps_results():
    print("RPS RESULTS...")

    # for data sent via POST request, form inputs are in request.form:
    form_data = dict(request.form)
    print("FORM DATA:", form_data)

    user_choice = form_data.get("user_choice")
    if user_choice not in VALID_OPTIONS:
        flash("Please choose rock, paper, or scissors.", "warning")
        return redirect("/rps/form")

    computer_choice = generate_random_choice()
    outcome = determine_winner(user_choice, computer_choice)

    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )
