from flask import jsonify,request,Blueprint, abort
from werkzeug.security import check_password_hash, generate_password_hash
from models.users.model import User
from models.db import db
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
import validators



users=Blueprint('users',__name__,url_prefix='/users')

@users.post('/login')
def login():
    # the get is to help set a default value incase the user  does not provide, such that the app does not crash
    user_name = request.json.get('name', '')
    user_password = request.json.get('password', '')

    # checking the name
    user =  User.query.filter_by(name=user_name).first()
    if user:
        is_password_correct=check_password_hash(user.password, user_password)
            # if the password is correct
        if is_password_correct:
            # giving them an access token and refresh token
              refresh_token = create_refresh_token(identity=user.id)
              access_token = create_access_token(identity = user.id)

            #   now the user can be redirected to the page he/she wants after recieving the refresh and access
              return jsonify({
                  "user_name":user.name,
                  "access_token": access_token,
                  "refresh_token": refresh_token,
                  "message":"Successfully logged In"
              })
    
    else:
        return jsonify({
            "message":"Wrong credentials",
            "Status code":"401"
        })

# Getting all users
@users.route("/view_all")
def all_users():
    users = User.query.all()
    results =[
        {
        "name":user.name,
        "email":user.email,
        "contact":user.contact,
        "user_type":user.user_type

    }for user in users]

    return{"count":len(results),"users":results}


# create a new user
@users.route('/register',methods=['POST'])
def create_user():
    user_name =request.json['name']
    user_email = request.json['email']
    user_contact =request.json['contact']  
    user_password = request.json['password']
    user_user_type=request.json['user_type']
    password_hash = generate_password_hash(user_password)
  


    # validations
    #getting the user a data
    if not user_name:
        return jsonify({'Message':"Username is required"}),400
    
    if not user_email:
        return jsonify({'Message':"Email is required"}),400
    
    if not user_contact:
        return jsonify({'Message':"Contact is required"}),400
    
    if not user_password:
        return jsonify({'Message':"Password is required"}),400
    
    # password validation length
    if len(user_password)<6:
        return jsonify({'Message':"Password must be atleast 6 characters long"})
    
    # if not user_address:
    #     return jsonify({'Message':"Address is required"}),400
    
    #constaints
    if User.query.filter_by(email=user_email).first():
       return jsonify({'Message':"user_email already exists"}),409
    
    
    existing_user_contact=User.query.filter_by(contact=user_contact).first()
    if existing_user_contact:
            return jsonify({'Message':"user_contact already in use"}),409
     
    

    #storing new user
    new_user = User( name = user_name,
                    email = user_email,
                    contact = user_contact,
                    password=password_hash,
                     user_type=user_user_type)
    #  address = user_address,
    

    #adding a new users to the database
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
                    'Success':True,
                    'Message':f"{new_user.name} you have successfully created an account",
                    }),201

# Getting a specific user
@users.route('/get_user/<id>')
def get_user(id):
    selected_user = User.query.get_or_404(id)
    response = {
        "name":selected_user.name,
        "email":selected_user.email,
        "contact":selected_user.contact,
        "user_type":selected_user.user_type
    }

    return {"User details":response}

# Updating a user
@users.route('/update/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)


    data = request.get_json()

    if not data['name']:
            return jsonify({"message":"Your name is required"})
        
    if not data['email']:
            return jsonify({"message":"Your ameil is required"})
        
    if not data['contact']:
            return jsonify({"message":"Your contact is required"})
        
    if not data['password'] :
            return jsonify({"message":"password is required"})
    
    if not data['user_type'] :
            return jsonify({"message":"user type is required"})
    
    user.name = data['name']
    user.email = data['email']
    user.contact = data['contact']
    user.password = data['password']
    user.user_type = data['user_type']
    db.session.add(user)
    db.session.commit()
    return {"message": f"User {user.id} updated successfully"}
# def update(id, users):
#     existing_user = User.query.get(id)

#     if existing_user:
#         update_user = User.load(users, session=db.session)
#         existing_user.content = update_user.content
#         db.session.merge(existing_user)
#         db.session.commit()
#         return User.dump(existing_user), 201
#     else:
#         abort(404, f"User with ID {id} not found")


# Deleting a user
@users.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    delete_id = User.query.get(id)
    # Incase the user does not exist
    if delete_id is None:
        return {
            "message":"Sorry the user you want to delete does not exist",
        }
    # Otherwise
    db.session.delete(delete_id)
    db.session.commit()
    return {
        "message":"Successfully deleted the user",
        "Status code": 200}
