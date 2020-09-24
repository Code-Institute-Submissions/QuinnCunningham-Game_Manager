import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'games'
app.config["MONGO_URI"] = 'mongodb+srv://root:asdf1234@myfirstcluster.lcr9v.mongodb.net/games?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_games')
def get_games():
    return render_template("games.html", games=mongo.db.games.find())

@app.route('/addgame')
def addgame():
    return render_template("add_game.html")

@app.route('/enter_games', methods=['POST'])
def enter_games():
    games = mongo.db.games
    games.insert_one(request.form.to_dict())
    return redirect(url_for('get_games'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
