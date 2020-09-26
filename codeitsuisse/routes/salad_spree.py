import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def get_ans(n, mp):
    nowbest = np.inf
    valid = 0
    for road in mp:
        nowsum = 0
        nowx = 0
        for i in range(n):
            if road[i] == "X":
                nowx += 1
            else:
                nowsum += int(road[i])
        
        if nowx == 0:
            nowbest = min(nowbest, nowsum)
            valid = 1
        
        for i in range(n, len(road)):
            if road[i] == "X":
                nowx += 1
            else:
                nowsum += int(road[i])
            if road[i-n] == "X":
                nowx -= 1
            else:
                nowsum -= int(road[i-n])
            if nowx == 0:
                nowbest = min(nowbest, nowsum)
                valid = 1
    if valid == 0:
        return 0
    return nowbest
    

@app.route('/salad-spree', methods=['POST'])
def evaluate_salad_spree():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    n = data["number_of_salads"]
    mp = data["salad_prices_street_map"]
    result = get_ans(n, mp)
    
    logging.info("My result :{}".format(result))
    return jsonify({"result": result});



