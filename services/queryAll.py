from flask import jsonify, request
from config.app import app
from DAO import hotelDAO, mealDAO, transportDAO

def getAll():
    try:
        hotel = hotelDAO.getAllHotel()
        trans = transportDAO.getAllTrans()
        meal = mealDAO.getAllMeal()

        finalResult = hotel + trans + meal

        resp = jsonify(finalResult)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp