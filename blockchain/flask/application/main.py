from flask import Flask, render_template, request, url_for, redirect
from blockchain.flask.application.block import *


application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])  # Handle "http://localhost:5000/"
def index():
    if request.method == 'POST':
        sender = request.form['sender']
        sum = request.form['sum']
        recipient = request.form['recipient']

        write_block(sender=sender, amount=sum, recipient=recipient)
        return redirect(url_for('index'))
    return render_template('index.html')


@application.route('/check', methods=['GET'])
def check():
    results = check_block_status()
    return render_template('index.html', results=results)


if __name__ == "__main__":
    application.run(debug=True)