# Reference : https://medium.com/প্রোগ্রামিং-পাতা/ডকার-এ-পাইথন-ওয়েব-এপ্লিকেশন-চালানো-এবং-ডকার-এর-মূল-ধারণা-e309d7393fc7

#main.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return " Welcome ! This python flask app is running in linux distro inside Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
