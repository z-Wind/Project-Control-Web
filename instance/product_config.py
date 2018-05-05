'''
product_config.py
'''
import os

appFolder = os.path.dirname(__file__)

# 資料庫的路徑
SQLALCHEMY_DATABASE_URI = 'sqlite:///' \
                        + os.path.join(appFolder, r"../", 'data.db')

# 用 os.urandom(24) 產生一組即可
SECRET_KEY = b'j\x92\xedV\xab~\xd1U#\xef\x9cp\xb0\x90\x1c]\x99\xd6\xd1\xf94\x8f\xb1\xe7'
