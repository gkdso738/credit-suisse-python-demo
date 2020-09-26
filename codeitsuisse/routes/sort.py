import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
    

@app.route('/sort', methods=['POST'])
def evaluate_sort():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    bkt = []
    for i in range(20001): 
        bkt.append(0)
    for num in data:
        bkt[num + 10000] += 1
    result = []
    for i in range(len(bkt)):
        for j in range(bkt[i]):
            result.append(i - 10000)
            
    logging.info("My result :{}".format(result))
    return jsonify(result);






