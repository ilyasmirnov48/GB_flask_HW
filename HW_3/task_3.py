from flask import Flask, request, render_template, flash, redirect, url_for
from HW_3.models import db, User
from flask_wtf.csrf import CSRFProtect
from HW_3.forms import RegistrationForm
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = b'47942b1b65002ed2fa1c16025502aa85768554cf4f260efd228b5dcbc645906'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../registration.db'
db.init_app(app)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(name=name, surname=surname, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash(f'Вы успешно зарегистрировались!')
        return redirect(url_for('registration'))
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
