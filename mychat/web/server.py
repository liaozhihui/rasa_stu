
from flask import Flask, render_template, request
from mychat.bot.action_agent import ActionAgent,UserMessage
import requests
import json
REQUEST_URL = "http://localhost:5005/webhooks/rest/webhook"
HEADER = {'Content-Type':'application/json; charset=utf-8'}


app = Flask(__name__, static_url_path='')


def Botresponse(sender, meg):
    requestDict = {"sender": sender, "message": meg}
    rsp = requests.post(REQUEST_URL, data=json.dumps(requestDict), headers=HEADER)
    if rsp.status_code == 200:
        rspJson = json.loads(rsp.text.encode())
        print(rspJson)
        if not rspJson:
            return "。。。。"
        return rspJson[0]["text"]
    else:
        return ""


########################################


def request_handler_message(message):
    userMessage = UserMessage(message)
    actionAgent = ActionAgent.load("/home/lzh/PycharmProjects/rasa_stu")
    # actionAgent.handle_message(userMessage)


@app.route('/', methods=['GET', 'POST'])
def view():
    return render_template('index.html')


@app.route('/chat', methods=['GET'])
def response():
    data = request.args.to_dict()
    message = data['message']
    if message != '':
        answer = Botresponse("user1", message)
        return answer


@app.route('/forget', methods=['GET'])
def forget():
    return 'success'


@app.route("/action_name",methods = ["POST","GET"])
def get_action():
    data = request.args.to_dict()
    action_name = data.get("action_name")
    try:
        request_handler_message(action_name)
    except Exception as e:
        print(e)
    return action_name



if __name__ == '__main__':
    print("web init success!")
    app.run('localhost','5000', debug=True)
