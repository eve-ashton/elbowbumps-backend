from flask import Flask, request, jsonify
from __main__ import app

@app.route('/register', methods=('GET', 'POST'))
def register():
    reg_data = {}
    if request.method == 'POST':
        #TODO: register new accound
        print('register')
    return jsonify(reg_data)

@app.route('/login', methods=('GET', 'POST'))
def login():
    login_creds = {}
    if request.method == 'POST':
        #TODO: login to an exiting accound
        print('login')
    return jsonify(login_creds)