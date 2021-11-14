from flask import Flask, render_template, session, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect
from threading import Lock
from listen import ResumableMicrophoneStream, SAMPLE_RATE, CHUNK_SIZE, main
from six.moves import queue
from helpers import get_important_words, get_related_image

stream = ResumableMicrophoneStream(SAMPLE_RATE, CHUNK_SIZE)


async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socket_ = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socket_.async_mode)


@socket_.on('connect', namespace='/notes')
def connect():
    session['sentences'] = []
    session['is_listening'] = False

@socket_.on('button_press', namespace='/notes')
def button_press():
    session['is_listening'] = not session.get('is_listening')
    emit('my_response',
         {'is_listening':session.get('is_listening') })
    if session.get('is_listening'):
        print("Start listening")
        stream.__enter__()
        session["sentences"] = []
        main(stream, session["sentences"])
    else:
        print("Stop listening")
        stream._buff = queue.Queue()
        stream.closed = True        
    return {}

@socket_.on('process_sentence', namespace='/notes')
def process(data):
    n = len(session['sentences']) - 2
    cvt = n - data['idx']

    curr_sentence = session['sentences'][cvt]
    try:
        key_phrases = get_important_words(curr_sentence)
        image = get_related_image(key_phrases[0])
        return emit('sentence_response', {'sentence':curr_sentence, 'words':key_phrases, 'image':image})
    except Exception:
        pass

    return {}


@socket_.on('disconnect', namespace='/notes')
def disconnect():
    stream.__exit__()



if __name__ == '__main__':
    socket_.run(app, debug=True)