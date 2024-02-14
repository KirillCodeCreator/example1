from flask import Flask, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
