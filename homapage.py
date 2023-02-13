from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['GET'])
def benvenuto():
    return render_template('descrizionemilano.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)