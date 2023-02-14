from flask import Flask,render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def benvenuto():
    return render_template('descrizionemilano.html')

@app.route('/immagini', methods=['GET'])
def immagini():
    return render_template('monumentimilano.html')

@app.route('/duomo', methods=['GET'])
def duomo():
    return render_template('duomo.html')

@app.route('/arco', methods=['GET'])
def arco():
    return render_template('arco.html')

@app.route('/castello', methods=['GET'])
def castello():
    return render_template('castello.html')

@app.route('/sansiro', methods=['GET'])
def sansiro():
    return render_template('sansiro.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)