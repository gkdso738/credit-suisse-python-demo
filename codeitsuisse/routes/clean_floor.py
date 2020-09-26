import logging
import json
import numpy as np

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

def get_ans(floor):
    n = len(floor)
    now = []
    sufsum = []
    for fl in floor:
        now.append(fl)
        sufsum.append(0)
    sufsum[n-1] = now[n-1]
    for i in range(n-2, -1, -1):
        sufsum[i] = sufsum[i+1] + now[i]

    ans = 0
    for i in range(1, n-1):
        ans += (now[i-1] * 2)
        now[i] -= now[i-1]
        now[i-1] = 0
        if now[i] < 0:
            now[i] = (-now[i]) % 2
        if sufsum[i+1] + now[i] == 0:
            return ans
        
        ans += 1
        now[i] -= 1
        if now[i] < 0:
            now[i] = (-now[i]) % 2
        
    
    x = now[n-2]
    y = now[n-1]
    
    if x + y == 0:
        return ans
    
    # print(ans, x, y)
    
    m = max(x-1, y-1)
    ans += m * 2
    x -= m
    y -= m

    if x < 0:
        x = (-x) % 2
    if y < 0:
        y = (-y) % 2
        
    # print(ans, x, y)
    
    if x == 0 and y == 0:
        return ans
    if x == 0 and y == 1:
        return ans + 1
    if x == 1 and y == 0:
        return ans + 3
    if x == 1 and y == 1:
        return ans + 2

    

@app.route('/clean_floor', methods=['POST'])
def evaluate_clean_floor():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    
    answer_dic = {}
    for key in data["tests"]:
        ans = get_ans(data["tests"][key]["floor"])
        answer_dic[key] = ans

    
    # logging.info("My result :{}".format(result))
    return jsonify({"answers": answer_dic});



