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
    elif "お問い合わせ" in text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="お問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hakkason/site.html")
         )
    elif "こんばんわ" in text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="わわわわ")
         )
    elif "ぶんじん" in text:
        img_url = "https://youtuber-love.com/wp-content/uploads/2019/09/%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%88-2019-09-16-101620-1024x596.png"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="文人です"),
                ImageSendMessage(img_url, img_url)
            ]
         )
    elif "犬" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%82%BF%E3%82%99%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%88%E3%82%99%20(1).png"
        img_url2 = "https://blogimg.goo.ne.jp/user_image/34/3b/f7566028f97f4ebe957a4cd239b73eb2.jpg"
        img_url3 = "https://pictkan.com/uploads/converted/15/05/30/467222154-dog-747460_1920-L84-1920x1280-MM-100.jpg"
        img_url4 = "https://aphoto.love/wp-content/uploads/2019/03/2019-03-06-20.58.57-1024x683.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="一部の犬一覧です\n犬種で検索することも可能です\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hakkason/site.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2),
                ImageSendMessage(img_url3, img_url3),
                ImageSendMessage(img_url4, img_url4)
            ]
         )
    elif "猫" in text:
        img_url = "https://free-materials.com/adm/wp-content/uploads/2020/07/adpDSC_6464-760x507-1-300x200.jpg"
        img_url2 = "https://tk.ismcdn.jp/mwimgs/e/b/1140/img_eb31afc9c1fb914d68a7c73b657c7ebe183087.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="猫の一覧です。"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
         )
    elif "ポメラニアン" in text:
        img_url = "https://newscast.jp/attachments/SvukFZqNs1fOe4i1y9XL.jpeg"
        img_url2 = "https://thumb.photo-ac.com/bc/bc49950525af36bb2a1c46ea96fa7576_t.jpeg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="ポメラニアンです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hakkason/site.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )   
    elif "トイプードル" in text:
        img_url = "https://www.petfamilyins.co.jp/pns/wp-content/uploads/2019/06/1mohitseb_shutterstock_1079406218.jpg.webp"
        img_url2 = "https://free-materials.com/adm/wp-content/uploads/2016/02/6776d7d26279ecd81ed614b9bdd8df5a-500x332.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="トイプードルです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hakkason/site.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )       
    elif "チワワ" in text:
        img_url = "https://www.petfamilyins.co.jp/pns/wp-content/uploads/2019/06/f19c76facf185af19e8f77ef6b8fda44.jpg.webp"
        img_url2 = "https://imageslabo.com/wp-content/uploads/2019/05/553_dog_chihuahua_7203.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="チワワです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hakkason/site.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )                   
    elif "通知" in text:
        # 全ユーザにプッシュ
        line_bot_api.broadcast(
            TextSendMessage(text="通知テスト")
        )    
    else:
    	line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="「" + text + "」の意味がわかりません")
         )




if __name__ == "__main__":
    port = int(os.getenv("PORT",8080))
    app.run(host="0.0.0.0", port=port)
