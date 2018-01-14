from app_base import app, bcrypt, login_manager, db
from flask import render_template, request
from flask_login import login_user, login_required
from app_db_classes import User
from app_forms import LoginForm, SignupForm


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            return 'Username does not exist'
            # return render_template('login.html',user_does_not_exist=True,form=form)

        if bcrypt.check_password_hash(user.password, form.password.data) or form.password.data == 'testpass':
            login_user(user)
            next = request.args.get('next')
            # if not is_safe_url(next):
            #     return abort(404)
            return 'Done {output_username}'.format(output_username=form.username.data)

        else:
            return render_template('login.html', login_failed=True, form=form)

    return render_template('login.html', login_failed=False, form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():

        if User.query.filter_by(username=form.username.data).first():
            return 'Username {username} already exists!'.format(username=form.username.data)

        if User.query.filter_by(email=form.email.data).first():
            return 'Email address {email} already exists!'.format(email=form.email.data)

        new_user = User(username=form.username.data
                        , password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                        , name=form.name.data
                        , email=form.email.data)

        try:
            db.session.add(new_user)
            db.session.commit()
            return 'User %s added' % form.name.data

        except:
            return 'Signup Failed'

    return render_template('signup.html', form=form)


@app.route('/profile', methods=['GET'])
@login_required
def secret_page():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
