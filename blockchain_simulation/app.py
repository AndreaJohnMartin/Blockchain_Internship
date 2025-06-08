# app.py
from flask import Flask, render_template, redirect, url_for
from blockchain_simulation import create_blockchain, is_chain_valid

app = Flask(__name__)
chain = create_blockchain()

@app.route('/')
def index():
    return render_template('index.html', blockchain=[b.to_dict() for b in chain],
                           is_valid=is_chain_valid(chain))

@app.route('/tamper')
def tamper():
    # Tamper block 1
    chain[1].data = "Tampered Data"
    chain[1].hash = chain[1].generate_hash()
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    global chain
    chain = create_blockchain()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
