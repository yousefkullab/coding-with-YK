from flask import Flask, request, jsonify

app = Flask(__name__)

# GET  >>> Request data from a specified resource
# POST >>> Create a resource
# PUT  >>> Update a resource 
# DELETE >>> Delete a resource

@app.route("/get-user/<user_id>")
def get_user(user_id):
    
    user_data= {
        "user_id": user_id,
        "name": "Yousef",
        "email": "the1yousef98@gmail.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200
# Test Get in browser

@app.route("/create-user", mehtod=["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201
# Test Post in tool called >>> Postman


if __name__ == '__main__':
    app.run(debug=True)
    
    