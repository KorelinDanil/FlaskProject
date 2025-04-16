
from flask import Flask, request, render_template_string
from forms import RegistrationForm
import subprocess
import shlex

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret'

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = Regi
    strationForm()
    if form.validate_on_submit():
        return "Success!"
    return render_template_string('''
        <form method="post">
            {{ form.csrf_token }}
            {{ form.email.label }} {{ form.email }} {{ form.email.errors }}<br>
            {{ form.phone.label }} {{ form.phone }} {{ form.phone.errors }}<br>
            {{ form.name.label }} {{ form.name }} {{ form.name.errors }}<br>
            {{ form.address.label }} {{ form.address }} {{ form.address.errors }}<br>
            {{ form.index.label }} {{ form.index }} {{ form.index.errors }}<br>
            {{ form.comment.label }} {{ form.comment }} {{ form.comment.errors }}<br>
            <input type="submit">
        </form>
    ''', form=form)


@app.route('/uptime')
def uptime():
    result = subprocess.run(['uptime', '-p'], stdout=subprocess.PIPE)
    return f"Current uptime is {result.stdout.decode().strip()}"


@app.route('/ps')
def ps():
    args = request.args.getlist('arg')
    safe_args = [shlex.quote(arg) for arg in args]
    cmd = ['ps'] + safe_args
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    return f"<pre>{result.stdout.decode()}</pre>"
