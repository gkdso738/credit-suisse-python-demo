import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
    

@app.route('/fruitbasket', methods=['POST'])
def evaluate_fruitbasket():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    weights = [50, 50, 50]
    ret = 0
    keys = [key for key in data]
    for i in range(3):
        ret += weights[i] * data[keys[i]]
        
    # logging.info("My result :{}".format(result))
    # return jsonify({"answers": answer_dic});
    return str(ret)



