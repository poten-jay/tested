
# from flask_app import db

# from flask_sqlalchemy import SQLAlchemy 
# #from flask_migrate import Migrate
# from sqlalchemy.orm import backref

# #db = SQLAlchemy()
# #migrate = Migrate()

# class Menu(db.Model):
#     __tablename__ = 'menu'

#     no = db.Column(db.Integer(), primary_key=True)
#     brand_id = db.Column(db.Integer())
#     brand = db.Column(db.String(64), db.ForeignKey('brand.id'))
#     menu  = db.Column(db.String(64))

#     def __repr__(self):
#         return f"Menu {self.menu}"
        
#     # def __repr__(self):
#     #     return 'User %i, name is %s' % (self.id, self.name)


# class Brand(db.Model):
#     __tablename__ = 'brand'

#     id = db.Column(db.Integer(),primary_key=True)
#     brand = db.Column(db.String(64), nullable=False )
#     s_count = db.Column(db.Integer())
#     s_start  = db.Column(db.String(64), nullable=False)
#     s_year  = db.Column(db.Integer())
#     # https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
#     tweets = db.relationship('Menu', backref='user', cascade = 'all, delete')

#     def __repr__(self):
#         return f"Brand {self.id}"

# # FLASK_APP=twit_app flask run


##############################################################

# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String(32))

    def __repr__(self):
        return 'User %i, name is %s' % (self.id, self.name)
