from app import app, db, cors
from flask import request, jsonify, json
from app.models import Todos
from app.models import User


@app.route('/api/todo', methods=['GET'])

def get_todos():
    todos = Todos.query.all()
    todo_list = [{

        'id': todo.id,

        'title': todo.title,

    } for todo in todos]

    return jsonify(todo_list)
    
    

@app.route('/api/todo', methods=['POST'])
def add_data():
        
    data = request.json
    todos = Todos(title=data["title"]) 
    db.session.add(todos)
    db.session.commit()
    id = todos.id
    data = {
            "id" : id,
            "title" : 'todos.title',
        }
    return jsonify(data),201



@app.route('/api/todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todo = Todos.query.get(todo_id)
    if not todo:

        return jsonify({'error': 'Todo not found'}), 404
    

    data = request.get_json()
    todo.id = data[id]
    todo.title = data['title']
     
    db.session.commit()

    return jsonify(todo)


@app.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):

    todo = Todos.query.get(todo_id)
    if not todo:

        return jsonify({'error': 'Todo not found'}), 404
    

    db.session.delete(todo)

    db.session.commit()

    return jsonify({'message': 'Todo deleted successfully'})


# User Api 

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.json 
    user = User(
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        role=data['role'],
        password=data['password']
    )
    db.session.add(user)
    db.session.commit()
    id = user.id
    psw = user.password
    data = {
            "id" : id,
            "firstname" : 'user.firstname',
            "lastname" : 'user.lastname',
            "email" : 'user.email',
            "role" : 'user.role',
            "password" : psw
            
            }

    return jsonify(data), 201

@app.route('/api/user', methods=['GET'])
def get_user():
    data = User.query.all()
    data = {
            "id" : 15,
            "firstname" : "gvind",
            "lastname" : "shibn",
            "email" : "email",
            "role" : "role",
            "password" : 1214,
            
            }
    return jsonify(data)
    # user_list = [{

    #     'id': user.id,
    #     'firstname': user.firstname,
    #     'lastname' : user.lastname,
    #     'email' : user.email,
    #     'role' : user.role,
    #     'password' : user.password
    # } for user in users]

    # return jsonify(user_list)