'''
adminView.py
'''
from flask_admin import Admin

from .main import app

# Create admin
admin = Admin(app, 'PCF', template_mode='bootstrap3')
