
# main_route

from flask import Blueprint, render_template, request, url_for, redirect
from flask_app.models import db, User
# from flask_app import db

# from py_flask_app.models import db, User  # model �͵��� ���⼭ �۾��ϰ� ������,,

bp = Blueprint('main', __name__)

@bp.route('/')                          # app �� bp�� �ٲ���
def index():
    return render_template('index.html')

@bp.route('/user/')                    # main_route�� �Ű� ��
def create():
    # User.query
    return render_template('user.html')

@bp.route('/compare')
def update():
    return render_template('compare_user.html')


#########



@bp.route('/ind/', methods=('POST', 'GET'))
def index2():
    if request.method == 'POST':
        # return 'Hello'
        task_content = request.form['content']
        new_task = User(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/ind/')
        except:
            return 'Threr was an isuue adding your task'
        
    else:
        tasks = User.query.order_dy(User.date_created).all()
        return render_template('ind.html', tasks=tasks)