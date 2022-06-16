from flask import Flask, request, json
import random

app = Flask(__name__)

# 0. Random
# CURL: curl http://127.0.0.1:5000/credit
# Python requests: resp = requests.get('http://127.0.0.1:5000/credit')

# @app.route('/credit', methods=['GET'])
# def get_credit_eligibility():
#     is_eligible = random.choice([True, False])
#     return "Accepted" if is_eligible else "Rejected"

# ----

# 1.0 Univariate threshold
# CURL: curl http://127.0.0.1:5000/credit?debt_ratio=0.2
# CURL: curl -G http://127.0.0.1:5000/credit -d "debt_ratio=0.4"
# Python requests: resp = requests.get('http://127.0.0.1:5000/credit', params={"debt_ratio": 0.4})

DEBT_RATIO_THRESHOLD = 0.3
@app.route('/credit', methods=['GET'])
def get_credit_eligibility():
    debt_ratio = request.args.get('debt_ratio', default=1, type=float)
    is_eligible = (debt_ratio <= DEBT_RATIO_THRESHOLD)

    return "Accepted" if is_eligible else "Rejected"

# 1.1 Univariate threshold, batch
# CURL: curl -X POST -H "Content-type: application/json" -d '[{"id": "001", "debt_ratio": 0.6}, {"id": "002", "debt_ratio": 0.1}]' http://127.0.0.1:5000/credits
# Python requests: resp = requests.post('http://127.0.0.1:5000/credits', json=[{"id": "001", "debt_ratio": 0.6}, {"id": "002", "debt_ratio": 0.1}])
# Python requests: resp = requests.post('http://127.0.0.1:5000/credits', data='[{"id": "001", "debt_ratio": 0.6}, {"id": "002", "debt_ratio": 0.1}]', headers={'content-type': 'application/json'})

@app.route('/credits', methods=['POST'])
def get_credit_eligibilities():
    customer_infos = request.json
    eligibilities = {}
    for customer in customer_infos:
        is_eligible = (customer["debt_ratio"] <= DEBT_RATIO_THRESHOLD)
        eligibilities[customer["id"]] = "Accepted" if is_eligible else "Rejected"

    return eligibilities


if __name__ == '__main__':
    app.run()
