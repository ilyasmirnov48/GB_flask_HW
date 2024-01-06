from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'd4f78cbce70425ae208b7b2915e9ee9734ac38fbc29b15ef33ae035bd9c3d2c3'


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/log/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return render_template('log.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()