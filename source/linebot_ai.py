import os
import sys
from argparse import ArgumentParser
from fastapi import FastAPI, Request, HTTPException
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from dotenv import load_dotenv

load_dotenv(verbose=True)

app = FastAPI()

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.get("/")
async def root():
    return {"message": "Hello World !!"}


@app.post("/callback")
async def callback(request: Request):
    """
    LINE PlatformのRequestを処理します
    Args:
        request: Message Webhook event object which contains the sent message.
        https://developers.line.biz/en/reference/messaging-api/#message-event
    """

    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = (await request.body()).decode("utf-8")

    try:
        # 署名を検証し、問題なければhandleに定義されている関数を呼び出す
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 署名検証で失敗したときは例外をあげる
        raise HTTPException(
            status_code=400, detail="Signature verification failed")

    return 'OK'

# @handler.addメソッドの第一引数には、LINE Platformからの"Webhook Event Objects"を指定します。
# https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects
#
# Eventはlinebot.modelsに定義されていて以下の種類があります。
# 　TextMessage,
# 　ImageMessage,
# 　VideoMessage,
# 　AudioMessage,
# 　LocationMessage,
# 　StickerMessage,
# 　FileMessage
# handler.addメソッドはメッセージイベントの場合にテキストや画像のようなメッセージの
# 内容でも処理を分けることができます。


@handler.add(MessageEvent, message=TextMessage)
def message_text(event: MessageEvent) -> None:
    """
    MessageEventを処理します。
    Args:
        event: Message Webhook event object which contains the sent message.
        https://developers.line.biz/en/reference/messaging-api/#message-event
    """

    # Natural Language APIに分析を依頼し、
    # 分析結果をresponseに受け取ります。
    response = None

    # 分析結果をメッセージ形式にフォーマットします。
    message = None

    # LINEに分析結果のメッセージを返信します。
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message)
    )
