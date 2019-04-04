from flask import Blueprint
from dao.db import db

# 创建蓝图
insertNews = Blueprint('insertNews', __name__)


@insertNews.route('/insertNews', methods=['POST'])
def insert_news():
    db.create_all()

    return "sss"
