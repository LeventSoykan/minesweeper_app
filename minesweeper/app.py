from flask import render_template, Flask, request
from game import Game

app = Flask(__name__, template_folder='templates')
game = None

@app.route("/", methods=['GET','POST'])
def home():
    global game
    if request.method == 'GET':
        game = Game()
    if request.method == 'POST':
        row = int(request.form['row'])
        col = int(request.form['col'])
        if request.form.get('flag'):
            game.board[row, col].flag = True
        else:
            game.stack = []
            game.check_selection(row, col)
    return render_template('home.html', data=game.board, playing=game.playing)

if __name__ == '__main__':
    app.run(debug=True)