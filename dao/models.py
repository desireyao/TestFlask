from dao.db import db


class News(db.Model):
    __tablename__ = 't_news'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True, index=True)
    title = db.column(db.String(10), nullable=False)
    content = db.column(db.String(64),)
