from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/list_prof/<list>', methods=['POST', 'GET'])
def training(list):
    list_prof = ['p', 'o', 'p']
    return render_template('list.html', list=list, profession=list_prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)