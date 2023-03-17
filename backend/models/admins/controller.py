from flask import jsonify,request,Blueprint, abort
from werkzeug.security import check_password_hash, generate_password_hash
from models.admins.model import Admin
from models.db import db
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token
import validators



admins=Blueprint('admins',__name__,url_prefix='/admins')

@admins.post('/login')
def login():
    # the get is to help set a default value incase the Admin  does not provide, such that the app does not crash
    Admin_name = request.json.get('name', '')
    Admin_password = request.json.get('password', '')

    # checking the name
    Admin =  Admin.query.filter_by(name=Admin_name).first()
    if Admin:
        is_password_correct=check_password_hash(Admin.password, Admin_password)
            # if the password is correct
        if is_password_correct:
            # giving them an access token and refresh token
              refresh_token = create_refresh_token(identity=Admin.id)
              access_token = create_access_token(identity = Admin.id)

            #   now the Admin can be redirected to the page he/she wants after recieving the refresh and access
              return jsonify({
                  "Admin_name":Admin.name,
                  "access_token": access_token,
                  "refresh_token": refresh_token,
                  "message":"Successfully logged In"
              })
    
    else:
        return jsonify({
            "message":"Wrong credentials",
            "Status code":"401"
        })

# Getting all admins
@admins.route("/view_all")
def all_admins():
    admins = Admin.query.all()
    results =[
        {
        "name":admin.name,
        "email":admin.email,
        "contact":admin.contact,
        "Admin_type":admin.admin_type

    }for admin in admins]

    return{"count":len(results),"admins":results}


# create a new Admin
@admins.route('/register',methods=['POST'])
def create_Admin():
    Admin_name =request.json['name']
    Admin_email = request.json['email']
    Admin_contact =request.json['contact']  
    Admin_password = request.json['password']
    A_Admin_type=request.json['Admin_type']
    password_hash = generate_password_hash(Admin_password)
  


    # validations
    #getting the Admin a data
    if not Admin_name:
        return jsonify({'Message':"Admin name is required"}),400
    
    if not Admin_email:
        return jsonify({'Message':"Email is required"}),400
    
    if not Admin_contact:
        return jsonify({'Message':"Contact is required"}),400
    
    if not Admin_password:
        return jsonify({'Message':"Password is required"}),400
    
    if not A_Admin_type:
        return jsonify({'Message':"Admin_type is required"}),400
    
    # password validation length
    if len(Admin_password)<6:
        return jsonify({'Message':"Password must be atleast 6 characters long"})
    
    # if not Admin_address:
    #     return jsonify({'Message':"Address is required"}),400
    
    #constaints
    if Admin.query.filter_by(email=Admin_email).first():
       return jsonify({'Message':"Admin_email already exists"}),409
    
    # if Admin.query.filter_by(admin_type=A_Admin_type).first():
    #    return jsonify({'Message':"Super_Admin already exists"}),409
    
    
    existing_Admin_contact=Admin.query.filter_by(contact=Admin_contact).first()
    if existing_Admin_contact:
            return jsonify({'Message':"Admin_contact already in use"}),409
     
    

    #storing new Admin
    new_Admin = Admin( name = Admin_name,
                    email = Admin_email,
                    contact = Admin_contact,
                    password=password_hash,
                     Admin_type=A_Admin_type)
    #  address = Admin_address,
    

    #adding a new admins to the database
    db.session.add(new_Admin)
    db.session.commit()
    return jsonify({
                    'Success':True,
                    'Message':f"{new_Admin.name} you have successfully created an account",
                    }),201

# Getting a specific Admin
@admins.route('/get_Admin/<id>')
def get_Admin(id):
    selected_Admin = Admin.query.get_or_404(id)
    response = {
        "name":selected_Admin.name,
        "email":selected_Admin.email,
        "contact":selected_Admin.contact,
        "Admin_type":selected_Admin.Admin_type
    }

    return {"Admin details":response}

# Updating a Admin
@admins.route('/update/<id>', methods=['PUT'])
def update_Admin(id):
    Admin = Admin.query.get_or_404(id)


    data = request.get_json()

    if not data['name']:
            return jsonify({"message":"Your name is required"})
        
    if not data['email']:
            return jsonify({"message":"Your ameil is required"})
        
    if not data['contact']:
            return jsonify({"message":"Your contact is required"})
        
    if not data['password'] :
            return jsonify({"message":"password is required"})
    
    if not data['Admin_type'] :
            return jsonify({"message":"Admin type is required"})
    
    Admin.name = data['name']
    Admin.email = data['email']
    Admin.contact = data['contact']
    Admin.password = data['password']
    Admin.Admin_type = data['Admin_type']
    db.session.add(Admin)
    db.session.commit()
    return {"message": f"Admin {Admin.id} updated successfully"}
# def update(id, admins):
#     existing_Admin = Admin.query.get(id)

#     if existing_Admin:
#         update_Admin = Admin.load(admins, session=db.session)
#         existing_Admin.content = update_Admin.content
#         db.session.merge(existing_Admin)
#         db.session.commit()
#         return Admin.dump(existing_Admin), 201
#     else:
#         abort(404, f"Admin with ID {id} not found")


# Deleting a Admin
@admins.route('/delete/<id>', methods=['DELETE'])
def delete_Admin(id):
    delete_id = Admin.query.get(id)
    # Incase the Admin does not exist
    if delete_id is None:
        return {
            "message":"Sorry the Admin you want to delete does not exist",
        }
    # Otherwise
    db.session.delete(delete_id)
    db.session.commit()
    return {
        "message":"Successfully deleted the Admin",
        "Status code": 200}
