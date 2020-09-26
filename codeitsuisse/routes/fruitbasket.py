import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
    

@app.route('/fruitbasket', methods=['POST'])
def evaluate_fruitbasket():
    data = request.get_data();
    
    my_json = data.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    
    weights = [-33, 41, 115]
    ret = 0
    keys = [key for key in data]
    for i in range(3):
        ret += weights[i] * data[keys[i]]
        
    result = "{}".format(ret)
        
    # logging.info("My result :{}".format(n))
    # return jsonify({"answers": answer_dic});
    return "0"
















