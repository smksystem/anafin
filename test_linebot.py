from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('LvQoS+P+ok7NNC3D63pz2w8873CQ3NGX/vyues85RDRBLM+/EetKf7LFcEcl8YV1wmEjIurpdmgbt1L0cU5Y7T4QKzrwY0/xUNH8rAbypH68sc9d3sw8t+znsNO2xlrMwUj2kj+5CIYqtrbOE/gK8AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c60544ef591611684da9813e562089a0')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()