from flask  import  Flask,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from models import db, User,Review,Game


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
# app.json.compact = False is a configuration that 
# has JSON responses print on separate lines with indentation. 
# This adds some overhead, but if human eyes will be looking at your API, it's always good to have this set to True


migrate =  Migrate(app,db)

db.init_app(app)

@app.route('/')
def index():
    return  "index for Game/Review/User API"

@app.route('/games')
def games():
    
    
    
    games  = []
    for game  in Game.query.all():
        game_dict = {
            "title" : game.title,
            "genre" : game.genre,
            "platform": game.platform,
            "price":game.price,
        }
            #appending games data from dictionary to games empty list
        games.append(game_dict)
            
            
    response  =  make_response(
        
        jsonify(games),
        200
        
    )     
    
    # defining a variable  response then assigning it and method  make_response 
    # that returns all the data in json response format
    # jsonify is a method in Flask that serializes its arguments as JSON and returns
    # a Response object. It can accept lists or dictionaries as arguments
    response.headers["Content-Type"] = "application/json"
    
    return response 
      
      
# method to get game by id
@app.route('/games/<int:id>')
def game_by_id(id):
    game = Game.query.filter_by(id=id).first()

    game_dict = {
        "title": game.title,
        "genre": game.genre,
        "platform": game.platform,
        "price": game.price,
    }

    response = make_response(
        jsonify(game_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response
if  __name__ == '__main__':
    app.run(port=5555)
            
        

    
