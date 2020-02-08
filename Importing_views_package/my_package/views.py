# views.py

# the below line can also be written as from . import app
from my_package import app

@app.route('/')
def show_entries():
    return 'Ola!!!!!'