'''
manage.py
'''
from flask_script import Manager, prompt_bool
from pcf import app, db

manager = Manager(app)


@manager.command
def initDB():
    """初始化資料庫"""
    if prompt_bool("將失去所有資料，確定嗎？"):
        db.drop_all()
        db.create_all()

if __name__ == '__main__':
    manager.run()
