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

    return """ 
    <!doctype html>
    <html> This is our homepage.
    <a href="/hello">Go to next page.</a></html>
    """


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

@app.route("/game")
def game():
    response = request.args.get("play_yes")
    player = request.args.get("person")
    compliment = choice(AWESOMENESS)
    if response:
        return render_template("game.html", person=player, compliment=compliment)
    else:
        return render_template("goodbye.html", person=player)

@app.route('/madlib')
def madlib():
    color = request.args.get("pick_color")
    noun = request.args.get("pick_noun")
    name_person = request.args.get("get_name_person")
    adjective = request.args.get("pick_adjective")
    return render_template("madlib.html", pick_color=color, pick_noun=noun, get_name_person=name_person, pick_adjective=adjective)



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
