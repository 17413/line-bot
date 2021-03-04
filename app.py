#-*- coding: utf-8 -*-

# インポートするライブラリ
from flask import Flask, request, abort, render_template, jsonify

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage,
    ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction,
    MessageTemplateAction, URITemplateAction, StickerMessage,
    URIAction, RichMenu, PostbackEvent
)

import os
import json


# ウェブアプリケーションフレームワーク:flaskの定義
app = Flask(__name__)

# サーバの環境変数から LINE_Access_Tokenを取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
# サーバの環境変数から LINE_Channel_Secretを取得
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
handler = WebhookHandler(LINE_CHANNEL_SECRET)



# "/"にGETリクエストを送ると返す  (ルートのアドレスに以下のものを配置することを明言)
@app.route("/", methods=["GET"])
def index():
    return "LINE Bot"



# LINE側が送ってきたメッセージが正しいか検証する
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    # プログラムの通常の操作中に発生したイベントの報告
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        # 署名を検証し、問題なければhandleに定義されている関数を呼び出す
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 署名検証で失敗したときは例外をあげる
        abort(400)
    return jsonify({"state": 200})



# MessageEvent　テキストメッセージ受け取った時
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 受け取りデータの確認
    print(f"\nevent：{event}\n")

    # 受け取ったメッセージ
    text = event.message.text

    if "こんにちは" in text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="こんにちは")
         )
    elif "犬" in text:
        img_url = "https://dol.ismcdn.jp/mwimgs/a/f/-/img_afa0fad37e6c4d5ce34c01faf54f9e79108563.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="保護されたがっている犬です"),
                ImageSendMessage(img_url, img_url)
            ]
         )
    elif "犬" in text:
        img_url = "https://public.potaufeu.asahi.com/3c54-p/picture/16534517/a0434cb2264412705c420977d9032401_640px.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="こちらも"),
                ImageSendMessage(img_url, img_url)
            ]
         )
    elif "通知" in text:
        # 全ユーザにプッシュ
        line_bot_api.broadcast(
            TextSendMessage(text="通知テスト")
        )
    elif "猫" in text:
        img_url = "https://newsbyl-pctr.c.yimg.jp/r/iwiz-yn/rpr/nakanishimasao/00147070/top_image.jpeg?w=800"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="保護されたがっている猫です"),
                ImageSendMessage(img_url, img_url)
            ]
         )    
    elif "カブトムシ" in text:
        img_url = "https://www.honda.co.jp/outdoor/knowledge/adventure/picture-book/kabutomushi/images/mv.jpg
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="保護されたがっているカブトです"),
                ImageSendMessage(img_url, img_url)
            ]
         )            
    else:
    	line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="「" + text + "」の意味がわかりません？")
         )




if __name__ == "__main__":
    port = int(os.getenv("PORT",8080))
    app.run(host="0.0.0.0", port=port)
