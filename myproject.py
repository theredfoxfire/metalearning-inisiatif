#import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

#pickle.dump(knn,open('model.pkl','wb'))

#model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Jaka!</h1>"


@app.route('/person/')
def hai():
    return jsonify({'name':'Hasan',
                    'address':'Magelang'})



if __name__ == "__main__":
    app.run(host='0.0.0.0')
