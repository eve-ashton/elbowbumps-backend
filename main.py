from flask import Flask, request, jsonify
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
import elbowbumps.auth
db = SQLAlchemy(app)
from elbowbumps.models import UserData, UserInterestData

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)

    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# Updates interests for a given user
@app.route('/update_interests', methods=['POST'])
def update_interests():
    param = request.args.get('user_id', None)
    print(param)
    response = {}

    # TODO: check if user exists in database

    if (param):
        response["STATUS_CODE"] = 200
        response["MESSAGE"] = f"User {param} has been updated"
    else:
        response["STATUS_CODE"] = 500
        response["MESSAGE"] = "Please provide a user id"
    return jsonify(response)

# Adds row for interest data
@app.route('/add_interest_score', methods=['POST'])
def add_interest_score():
    param = request.args.get('user_id')
    interest = UserInterestData(1, 'Basketball', 0.5)
    interest2 = UserInterestData(3, 'Basketball', 0.3)
    interest3 = UserInterestData(4, 'Basketball', 0.4)
    db.session.add(interest)
    db.session.add(interest2)
    db.session.add(interest3)
    db.session.commit()
    return jsonify({
        'STATUS_CODE': 200,
        'MESSAGE': 'row added successfully'
    })

# finds nearest neighbours for a given user
@app.route('/find_matches', methods=['GET'])
def find_matches():
    param = request.args.get('user_id')
    limit = request.args.get('limit')
    query = f'select uid1.uid_ud_id, uid2.uid_ud_id, sqrt(uid1.uid_squared_weight + uid2.uid_squared_weight - (2*uid1.uid_interest_weight*uid2.uid_interest_weight)) as distance from user_interest_data uid1 , user_interest_data uid2 where uid1.uid_interest_type = uid2.uid_interest_type and uid1.uid_id <> uid2.uid_id and uid1.uid_ud_id = {param} and uid1.uid_ud_id <> uid2.uid_ud_id group by uid2.uid_ud_id, uid1.uid_ud_id, uid1.uid_squared_weight,uid2.uid_squared_weight,uid1.uid_interest_weight,uid2.uid_interest_weight order by distance limit {limit};'
    results = db.engine.execute(query)
    return jsonify({
        'STATUS_CODE': '200',
        'result': [dict(row) for row in results]
    })

# Gets recommendations for a given user
@app.route('/get_recs_for', methods=['GET'])
def get_recs_for():
    param = request.args.get('user_id')
    test_user = "345"
    fake_users = ["556", "223"]
    if (param == test_user):
        return jsonify({
            "recommendations": fake_users,
            "STATUS_CODE": "200"
        })
    elif (param == None):
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please provide a user id"
        })
    else:
        return jsonify({
            "STATUS_CODE": "500",
            "Message": "Please ensure user exists in database"
        })

# Test endpoint - an example of how to make a transaction
@app.route('/test_user', methods=['POST'])
def create_test_user():
    from random import randint
    user = UserData('Faridz','Ibrahim',19,f'{randint(0, 6000)}','test','M','test3')
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'STATUS_CODE': '200',
        "Message": 'User added'
    })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    ENV = 'live'
    if ENV == 'dev':
        app.debug = True
        # Change the line below to your own local database for testing purposes
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost"
    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lrrucystcdokqx:8dcdf77fcf5031f6d6bf22e181e8e526fc69393bae3bbaed0065588c2963f6fb@ec2-54-198-73-79.compute-1.amazonaws.com:5432/da8ahn3kepucis'
    # Threaded option to enable multiple instances for multiple user access support
    db.create_all()
    app.run(threaded=True, port=5000)
