from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/training/<prof>', methods=['POST', 'GET'])
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        auth = True
    else:
        auth = False
    return render_template('new.html', auth=auth)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)