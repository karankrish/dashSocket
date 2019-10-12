from flask import Flask
from flask_socketio import SocketIO , emit
app = Flask(__name__)
app.config["INFO"] = True
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/send', methods=['GET'])
def some_function():
    socketio.emit('testEmit', "Hi")
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