import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


def get_ans(n, text):
    new_text = ""
    for ch in text:
        if ch.isalnum():
            new_text += ch.upper()
    
    ans = []
    for i in range(len(new_text)):
        ans.append(0)
    
    cnt = 0
    for st in range(n):
        cur = st
        while cur < len(new_text):
            ans[cur] = new_text[cnt]
            cnt += 1
            cur += n
            
    ret = ""
    for ch in ans:
        ret += ch        
    
    return ret
    

@app.route('/encryption', methods=['POST'])
def evaluate_encryption():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    result = []
    for test_case in data:
        result.append(get_ans(test_case["n"], test_case["text"]))
    logging.info("My result :{}".format(result))
    return jsonify(result);





