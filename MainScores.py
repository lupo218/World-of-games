from flask import Flask, render_template
import Utils
app = Flask(__name__)


try:
    with open(Utils.SCORES_FILE_NAME, "r") as f:  # red
        points = int(f.read())  # get val
    @app.route('/')
    def index():
        return render_template('index.html',SCORE=points)
    if __name__ == '__main__':
        app.run('0.0.0.0', debug=True, port=30000)
except:
    @app.errorhandler(404)
    def not_found(e):
        return render_template('error.html'), 404
    if __name__ == '__main__':
        app.run('0.0.0.0', debug=True, port=30000)
