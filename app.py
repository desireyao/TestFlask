from flask import Flask
from flask_cors import CORS
from dao.db import db
from config.config import CurConfig
from busi.insertNews import insertNews

app = Flask(__name__)

# 跨域支持
CORS(app, supports_credentials=True)

app.config.from_object(CurConfig['CONFIG'])

# 初始化db
db.init_app(app)


app.register_blueprint(insertNews)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
