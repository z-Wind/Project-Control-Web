'''
manage.py
'''
from flask_script import Manager
from pcf import app

manager = Manager(app)


@manager.command
def initDB():
    """初始化資料庫"""
    pass

if __name__ == '__main__':
    manager.run()
