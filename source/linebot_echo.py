import os
import sys
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.post("/callback")
async def callback(request: Request):
    """
    LINE PlatformのRequestを処理します
    Args:
        request: Message Webhook event object which contains the sent message.
        https://developers.line.biz/en/reference/messaging-api/#message-event
    """

    # リクエストヘッダーから署名検証のための値を取得

    # リクエストボディを取得

    # try:
    # 署名を検証し、問題なければhandleに定義されている関数を呼び出す

    # except InvalidSignatureError:
    # 署名検証で失敗したときは例外をあげる
    # raise HTTPException(
    #    status_code=400, detail="Signature verification failed")

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
