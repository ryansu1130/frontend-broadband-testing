from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/map')
def mapPage():
    return render_template('map.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

