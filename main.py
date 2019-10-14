from flask import Flask
from flask_socketio import SocketIO , emit
import mysql.connector

app = Flask(__name__)
app.config["INFO"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")


def mysqlread():
    mydb = mysql.connector.connect(
      host="10.128.0.6",
      user="root",
      passwd="admin",
      database="wcag"
    )
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT parseUrl FROM parseurltable;")
    
    myresult = mycursor.fetchall()
    a = []
    for i in myresult:
        a.append(i[0])
    return a


@app.route('/send', methods=['GET'])
def some_function():
    data = {"url":mysqlread()}
    socketio.emit('testEmit', data)
    return "ok"
    
'''
@socketio.on('test')
def handleMessage(test):
    print(test)
@socketio.on('connection')
def handleMessage(asd):
    print(asd)
    
'''
@socketio.on('message')
def handleMessage2(asd):
    print('Message: '+asd)
    some_function()

if __name__ == '__main__':
	socketio.run(app,host="0.0.0.0",port=7444)
