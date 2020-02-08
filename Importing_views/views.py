# views.py
from flaskr import app

@app.route('/')
def show_entries():
    return 'Hello!!!!!'