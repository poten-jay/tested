# from flask import Flask
# from flask_app.routes import main_route
# from flask import render_template
# from flask_sqlalchemy import SQLAlchemy

# __init__.py     (초기 시작)

from flask import Flask
from flask_app.models import db, migrate  # models 파일로 접근해서 db, mg 접근

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

from flask import Blueprint, render_template, request, url_for, redirect
from flask_app.models import db, User

db = SQLAlchemy()
migrate = Migrate()


app = Flask(__name__)

@app.route('/')                          # app 을 bp로 바꿔줌
def index():
    return render_template('index.html')

@app.route('/user/')                    # main_route로 옮겨 줌
def create():
    # User.query
    return render_template('user.html')

@app.route('/compare')
def update():
    return render_template('compare_user.html')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB['user']}:{DB['password']}@{DB['host']}/{DB['database']}"
app.debug = True

db.init_app(app)    
migrate.init_app(app, db) 

from flask_app.routes import main_route  # 순환 이슈로 위에 안하고 밑에
# from flask_app.routes import brand_route

app.register_blueprint(main_route.bp)
# app.register_blueprint(brand_route.bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

# FLASK_APP=flask_app flask run

# FLASK_APP=flask_app flask db init   <- migration 폴더 생김

# FLASK_APP=flask_app flask db migrate   <- db 생성

# FLASK_APP=flask_app flask db upgrade   <- 업그레이드

# 일련의 작헙 후 
# FLASK_APP=flask_app flask db migrate   <- 버전이 새로 생김

# FLASK_APP=flask_app flask db upgrade   <- db에 적용
# db 에 버전이 업뎃 되고 user 테이블이 만들어짐