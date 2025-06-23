from flask import Flask, request, jsonify

app = Flask(__name__)

class BankAccount:
    def __init__(self, number, acc_type, name, ssn, balance):
        self.account_number = number
        self.account_type = acc_type
        self.account_owner_name = name
        self.account_owner_ssn = ssn
        self.balance = balance

@app.route("/create-account", methods=["POST"])
def create_account():
    # ❌ No authentication check here
    data = request.json
    account = BankAccount(
        number=data["accountNumber"],
        acc_type=data["accountType"],
        name=data["accountName"],
        ssn=data["accountSSN"],
        balance=data["balance"]
    )
    return jsonify({"message": "Account created", "account": account.__dict__})
