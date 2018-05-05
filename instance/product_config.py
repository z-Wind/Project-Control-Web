'''
product_config.py
'''
import os

appFolder = os.path.dirname(__file__)

# 資料庫的路徑
SQLALCHEMY_DATABASE_URI = 'sqlite:///' \
                        + os.path.join(appFolder, r"../", 'data.db')
