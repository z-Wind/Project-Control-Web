'''
view.py
'''
from flask import render_template, Blueprint
from .main import app

pcf = Blueprint('pcf', __name__)


@pcf.route('/', methods=["GET"])
def index():
    return render_template('index.html', title="總覽")
