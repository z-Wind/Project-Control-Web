'''
main.py
'''
from flask import Flask

# instance_relative_config 設定有 instance 資料夾的存在，預設路徑 ../instance
app = Flask(__name__, instance_relative_config=True)
# 基本設定，來自於上層的 config.py
app.config.from_object("basic_config")

# 來自於 instance 中的 config.py，直接覆蓋之前的設定
# 路徑可用 app.instance_path 得知
# debug 設定，不用時可註解
app.config.from_pyfile('debug_config.py')
# 產品設定，來自於環境變數所提供的路徑
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# 因為 .views 中有用到 app，所以只能把 .views 往後擺
from .views import pcf

app.register_blueprint(pcf)


@app.before_request
def before_request():
    """在 request 前做的事"""
    pass
