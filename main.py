from flask import Flask, Response, jsonify
from flask.ext.pymongo import PyMongo

PORT = 1212
app = Flask(__name__)
mongo = PyMongo(app)


# 앱 실행시
# 도서관의 공기 정보를 리스트로 불러옴
@app.route('/loadListData', methods = ['GET'])
def load_list_data():
    return "list data"

# 상세 페이지 진입시
# name 도서관의 상세 정보를 불러옴
@app.route('/loadDetailData/<name>', methods = ['GET'])
def load_detail_data(name):
    return name+"\'s detail data"

# 통계 페이지 진입시
# name 도서관의 통계 정보 불러옴
@app.route('/loadChartData/<name>', methods = ['GET'])
def load_chart_data(name):
    return name+"\'s chart data"


if __name__=='__main__':
    app.run(host='0.0.0.0',port=PORT)
