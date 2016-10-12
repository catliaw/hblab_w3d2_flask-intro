from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<p><a href=\"/hello\">Go to Hello page</a></p><html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label><br>
          <label>Choose a compliment:
            <select name="compliment">
              <option value="awesome">Awesome</option>
              <option value="terrific">Terrific</option>
              <option value="fantastic">Fantastic</option>
            </select>
          </label>
          <input type="submit">
        </form><br>
        <form action="/diss">
         <label>What's your name? <input type="text" name="person"></label><br>
          <label>Or choose an insult instead:
            <select name="insult">
              <option value="lame">Lame</option>
              <option value="terrible">Terrible</option>
              <option value="freaky">Freaky</option>
            </select>
          </label>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Diss user returned from /hello"""

    player = request.args.get("person")

    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, insult)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)
    # print x

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
