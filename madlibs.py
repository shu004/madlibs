"""A madlib game that compliments its users."""

from random import choice

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
    # player = request.args.get("person")

    play_game = request.args.get("play_game")

    if play_game == "Yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html", player=player_name)

@app.route("/madlib")
def show_madlib():

    color = request.args.get("color")
    adj = request.args.get("adjective")
    person = request.args.get("person")
    noun = request.args.get("noun")

    return render_template("madlib.html", color=color, noun=noun, person=person, adjective=adj)




if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
