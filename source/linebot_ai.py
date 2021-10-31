import os
import sys
from fastapi import FastAPI, Request, HTTPException
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
from dotenv import load_dotenv
from source import client

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
            status_code=400, detail="Signature verification failed"
        )
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event: MessageEvent) -> None:
    response = client.analyze_sentiment(event.message.text)
    # 分析結果をメッセージ形式にフォーマット
    message = client.format_response_to_message(response)

    # LINEに分析結果のメッセージを返信します。
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message)
    )
