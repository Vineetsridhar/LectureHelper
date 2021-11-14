from flask import Flask, render_template, session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock


async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)


@socket_.on('button_press', namespace='/notes')
def button_press():
    session['is_listening'] = not session.get('is_listening')
    if session.get('is_listening'):
        print("Start listening")
    else:
        print("Stop listening")
    return emit('my_response',
         {'is_listening':session.get('is_listening') })




if __name__ == '__main__':
    socket_.run(app, debug=True)