from flask import Flask, jsonify, request

class User:
  def signup(self):
     user = {
       "id": "",
       "name": request.form.get('name'),
       "email": request.form.get('email'), 
       "password": request.form.get('password')
     }
     
     return jsonify(user), 200