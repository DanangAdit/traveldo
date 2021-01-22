from flask import jsonify, request
from config.app import app
from DAO import hotelDAO, mealDAO, transportDAO

def getBundle(location, budget):
    try:
        hotel = hotelDAO.getHotelByLocationAndBudget(location, budget)
        trans = transportDAO.getTransByLocationAndBudget(location, budget)
        meal = mealDAO.getMealByLocationAndBudget(location, budget)

        list = []

        for i in range(0, len(hotel)):
            if hotel[i]['price'] <= budget:
                temp = {}
                temp['hotel'] = hotel[i]['name']
                temp['sisa'] = budget - hotel[i]['price']
                temp['totalPrice'] = hotel[i]['price']
                list.append(temp)

        list_2 = []
        for i in range(0, len(list)):
            for j in range(0, len(trans)):
                if trans[j]['price'] <= list[i]['sisa']:
                    temp = {}
                    temp['hotel'] = list[i]['hotel']
                    temp['trans'] = trans[j]['name']
                    temp['sisa'] = list[i]['sisa'] - trans[j]['price']
                    temp['totalPrice'] = list[i]['totalPrice'] + trans[j]['price']
                    list_2.append(temp)

        list_3 = []
        for i in range(0, len(list_2)):
            for j in range(0, len(meal)):
                if meal[j]['price'] <= list_2[i]['sisa']:
                    temp = {}
                    temp['hotel'] = list_2[i]['hotel']
                    temp['trans'] = list_2[i]['trans']
                    temp['meal'] = meal[j]['name']
                    temp['sisa'] = list_2[i]['sisa'] - meal[j]['price']
                    temp['totalPrice'] = list_2[i]['totalPrice'] + meal[j]['price']
                    list_3.append(temp)

        finalResult = []
        for data in list_3:
            temp = {}
            temp['dataHotel'] = data['hotel']
            for i in hotel:
                if i['name'] == data['hotel']:
                    temp['priceHotel'] = i['price']
            temp['dataTrans'] = data['trans']
            for i in trans:
                if i['name'] == data['trans']:
                    temp['priceTrans'] = i['price']
            temp['dataMeal'] = data['meal']
            for i in meal:
                if i['name'] == data['meal']:
                    temp['priceMeal'] = i['price']
            temp['totalPrice'] = data['totalPrice']
            finalResult.append(temp)

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