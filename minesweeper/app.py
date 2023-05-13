from flask import render_template, Flask, request
from game import Game

app = Flask(__name__, template_folder='templates')
game = None

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'GET':
        global game
        game = Game()
    if request.method == 'POST':
        row = int(request.form['row'])
        col = int(request.form['col'])
        cell = game.board[row, col]
        cell.visible = True
    return render_template('home.html', data=game.board)

if __name__ == '__main__':
    app.run(debug=True)