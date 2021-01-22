from config.db_config import mysql

def getAllMeal():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM meal")
    rows = cursor.fetchall()
    list_resp = []
    for i in rows:
        dict_resp = {}
        dict_resp['id'] = i[0]
        dict_resp['name'] = i[1]
        dict_resp['price'] = i[2]
        dict_resp['location'] = i[3]
        list_resp.append(dict_resp)
    cursor.close()
    return list_resp

def getMealByLocationAndBudget(location, budget):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM meal WHERE location=%s AND price <=%s",
                   (location, budget))
    rows = cursor.fetchall()
    list_resp = []
    for i in rows:
        dict_resp = {}
        dict_resp['id'] = i[0]
        dict_resp['name'] = i[1]
        dict_resp['price'] = i[2]
        dict_resp['location'] = i[3]
        list_resp.append(dict_resp)
    cursor.close()
    return list_resp