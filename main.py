from flask import Flask
#from flask.ext.pymongo import pymongo

PORT = 8080
app = Flask(__name__)
@app.route('/loadData')
def load_data():
    return "hello flask!"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=PORT)
