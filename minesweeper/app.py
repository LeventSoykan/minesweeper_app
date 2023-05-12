from flask import render_template, Flask, request
from game import Game

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    game = Game()
    return render_template('home.html', data=game.board)

if __name__ == '__main__':
    app.run(debug=True)