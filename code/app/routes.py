from app import application, classes, db, models
from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user


@application.route('/index', methods=['GET', 'POST'])
@application.route('/', methods=['GET', 'POST'])
def index():
    """Index our site"""
    if request.method == 'POST':
        a = request.form['answer']
        s = request.form['solution']
        # return render_template('remi.html', answer=a, solution=s)
        cu = current_user.is_authenticated
        return render_template('index.html',
                               authenticated_user=cu,
                               equality=models.levenshtein_distance(s, a) > 0,
                               similarity=models.levenshtein_distance(s, a),
                               checked=True,
                               ans=a,
                               sol=s)
    return render_template('index.html',
                           checked=False,
                           authenticated_user=cu)


@application.route('/register',  methods=('GET', 'POST'))
def register():
    """Register new user"""
    registration_form = classes.RegistrationForm()
    if registration_form.validate_on_submit():
        username = registration_form.username.data
        password = registration_form.password.data
        email = registration_form.email.data

        user_count = classes.User.query.filter_by(username=username).count() \
            + classes.User.query.filter_by(email=email).count()
        if (user_count > 0):
            return '<h1>Error - Existing user : ' + username \
                   + ' OR ' + email + '</h1>'
        else:
            user = classes.User(username, email, password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('register.html', form=registration_form)


@application.route('/login', methods=['GET', 'POST'])
def login():
    """ Login new user"""
    login_form = classes.LogInForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        # Look for it in the database.
        user = classes.User.query.filter_by(username=username).first()

        # Login and validate the user.
        if user is not None and user.check_password(password):
            login_user(user)
            # return("<h1> Welcome {}!</h1>".format(username))
            return redirect(url_for('index'))

    return render_template('login.html', form=login_form)


@application.route('/logout')
@login_required
def logout():
    """Logout user"""
    before_logout = '<h1> Before logout - is_autheticated : ' \
                    + str(current_user.is_authenticated) + '</h1>'

    logout_user()

    after_logout = '<h1> After logout - is_autheticated : ' \
                   + str(current_user.is_authenticated) + '</h1>'
    return before_logout + after_logout


@application.route('/about')
def about():
    return render_template('about.html')

    # return("<h1> WELcome !</h1>")

# @application.route('/about',  methods=('GET', 'POST'))
# def about_us():
#    return render_template('about.html')
