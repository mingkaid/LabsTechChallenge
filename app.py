from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/md3422', methods=['GET'])
def md3422():
    return render_template('md3422.html')

if __name__ == '__main__':
    app.run(port=8888)
