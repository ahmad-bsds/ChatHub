from flask import Flask
from connections import Connection # AI response.

app = Flask(__name__)


@app.route('/')
def home():
    res = Connection()
    res = res.response("Write funny poem for.")
    return f'{res}'


if __name__ == '__main__':
    app.run(debug=True)
