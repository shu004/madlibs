"""A madlib game that compliments its users."""

from random import choice
import re

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return render_template("homepage.html")


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game/<player_name>")
def show_madlib_form(player_name):
    #ask instructors about passing in names

    play_game = request.args.get("play_game")

    if play_game == "Yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html", player=player_name)

@app.route("/madlib")
def show_madlib():

    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    rooms = request.args.getlist("room")
    if len(rooms) == 2:
        rooms.insert(1,'and')
    elif len(rooms) == 3:
        rooms.insert(2, 'or')
    bird = request.args.get("bird")
    past_verb = request.args.get("past_verb")
    current_verb = request.args.get("current_verb")

    return render_template("madlib.html", adjective1=adjective1, adjective2=adjective2, rooms=rooms, bird=bird, past_verb=past_verb, current_verb=current_verb)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
