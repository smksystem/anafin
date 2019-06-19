from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('zustrj8yyUuP+hEnrk5j7FWvBvGUMaLoA9ZeokKF/cngUBt9h9V43j4+86JaNljMwmEjIurpdmgbt1L0cU5Y7T4QKzrwY0/xUNH8rAbypH6ayOfmPCwKa7b6a381mkRBVwOgWykoFJSZxSluPBZUagdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a90085058c0bdcc4d9267265f3033440')

@app.route("/")
def hello():
    return "Hello World!"

# @app.route("/webhook", methods=['POST'])
@app.route("/webhook", methods=['POST'])

def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run(debug="DEBUG")