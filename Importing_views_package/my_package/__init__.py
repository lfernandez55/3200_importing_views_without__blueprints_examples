from flask import Flask
app = Flask(__name__)
# the below line can also be written as: from . import views
from my_package import views
