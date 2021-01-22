from services import queryAll as query_all, queryBundle as query_bundle, queryWithURL as query_withurl
from config.app import app
from flask import request

@app.route('/queryBundle', methods=['GET'])
def listBundle():
    req_data = request.get_json()
    resp = query_bundle.getBundle(req_data)
    return resp

@app.route('/queryAll')
def alldata():
    resp = query_all.getAll()
    return resp

@app.route('/queryWithURL/location=<string:location>&budget=<int:budget>')
def queryWithURL(location, budget):
    resp = query_withurl.getBundle(location, budget)
    return resp