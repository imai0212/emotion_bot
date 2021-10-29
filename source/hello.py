# Step 1: FastAPIをimportします。
from fastapi import FastAPI

# Step 2: FastAPIクラスのインスタンスを生成します。
app = FastAPI()

# Step 3: pathを設定します。pathは、"/" です。
# Step 4: pathに対するfunctionを定義します
@app.get("/")
async def root():
    # Step 5: メッセージ {"message": "Hello World"} をreturnします
    return{'message': 'Hello World'}
