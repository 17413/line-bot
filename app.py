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
            TextSendMessage(text="お問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html")
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
        img_url = "https://17413.azurewebsites.net/HAckason/IMG_8017.JPG"
        img_url2 = "https://17413.azurewebsites.net/HAckason/IMG_8019.JPG"
        img_url3 = "https://17413.azurewebsites.net/HAckason/IMG_8020.JPG"
        img_url4 = "https://17413.azurewebsites.net//HAckason/%E3%82%BF%E3%82%99%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%88%E3%82%99%20(1).png"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="一部の犬一覧です\n犬種で検索することも可能です\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2),
                ImageSendMessage(img_url3, img_url3),
                ImageSendMessage(img_url4, img_url4)
            ]
         )
    elif "猫" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%81%AD%E3%81%93.jpg"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E3%81%AD%E3%81%A3%E3%81%93.jpeg"
        img_url3 = "https://17413.azurewebsites.net/HAckason/IMG_8022.JPG"
        img_url4 = "https://17413.azurewebsites.net/HAckason/%E3%83%8D%E3%82%B3.jpeg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="一部の猫一覧です\n猫種で検索することも可能です\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2),
                ImageSendMessage(img_url3, img_url3),
                ImageSendMessage(img_url4, img_url4)
            ]
         )
    elif "ポメラニアン" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%82%8F%E3%82%93%E3%82%8F%E3%82%93.JPG"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E3%82%8F%E3%82%93%E3%82%8F%E3%82%93%E3%82%8F%E3%82%93.JPG"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="ポメラニアンです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )   
    elif "トイプードル" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/IMG_8027.JPG"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E3%83%88%E3%82%A4.JPG"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="トイプードルです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )       
    elif "チワワ" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%81%A1%E3%82%8F%E3%82%8F.JPG"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E3%81%A1%E3%82%8F%E3%82%8F%E3%82%8F.JPG"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="チワワです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )       
    elif "スコティッシュフォールド" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%81%99%E3%81%93.jpg"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E3%82%B9%E3%82%B3%E3%83%86%E3%82%A3.jpeg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="スコティッシュフォールドです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )          
    elif "アメリカンショートヘア" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%82%A2%E3%83%A1%E3%83%AA%E3%82%AB%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%83%98%E3%82%A2.jpg"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E9%9B%A8%E5%B7%BB.jpg"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="アメリカンショートヘアです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url),
                ImageSendMessage(img_url2, img_url2)
            ]
        )       
    elif "ブルドッグ" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E3%81%B5%E3%82%99%E3%82%8B.png"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="ブルドッグです\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
                ImageSendMessage(img_url, img_url)
            ]
         )             
    elif "柴" in text:
        img_url = "https://17413.azurewebsites.net/HAckason/%E8%8A%9D.jpg"
        img_url2 = "https://17413.azurewebsites.net/HAckason/%E3%81%97%E3%81%AF%E3%82%99.png"
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="柴犬です\nお問い合わせの際はこちらのサイトからご連絡ください\nhttps://toba17435.azurewebsites.net/hackathon/form.html"),
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
