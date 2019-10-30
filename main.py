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
      host="34.70.48.176",
      user="root",
      passwd="admin",
      database="wcag"
    )

    mycursor = mydb.cursor()

    mycursor.execute('select home_domain,parse_url from parseurltable where parseurlstatus = "completed";')

    myresult = mycursor.fetchall()
    domainname=set()
    for i in myresult:
        domainname.add(i[0])
    data ={}   
    for i in domainname:
        a=[]
        for j in myresult:
            if i == j[0]:
                a.append(j[1])
            else:
                pass
        data[i] = a
        
    return data


@app.route('/send', methods=['GET'])
def some_function():
    data = mysqlread()
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
