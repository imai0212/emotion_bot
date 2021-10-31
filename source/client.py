from google.cloud import language_v1
from google.cloud.language_v1.types.language_service import AnalyzeSentimentResponse

# 渡されたtextの分析結果を返す
def analyze_sentiment(text: str) -> AnalyzeSentimentResponse:
    # API用のクライアントオブジェクト取得
    client = language_v1.LanguageServiceClient()
    # テキストタイプを選択 : PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # テキストとタイプを指定して、APIに渡すドキュメントオブジェクトを生成
    document = language_v1.types.Document(content=text, type_=type_)

    # 文字コード指定 : NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.types.EncodingType.UTF8

    # ドキュメントと文字コードを指定して、分析結果取得
    return client.analyze_sentiment(
        request={'document':document, 'encoding_type': encoding_type}
    )


def input_text() -> str:
    texts = []

    while True:
        val = input()
        # 改行を打つと終了
        if len(val) == 0:
            break
        texts.append(val)
    return '\n'.join(texts)

def format_response_to_message(response: AnalyzeSentimentResponse) -> str:
    message = ""
    # テキスト全体の結果を生成
    message += "\n== Document ==\n\n"
    message += u"Document sentiment score: {}\n".format(
        response.document_sentiment.score)
    message += u"Document sentiment magnitude: {}\n".format(
        response.document_sentiment.magnitude)
    message += "\n== Sentences in the document ==\n\n"

    # 文章ごとの結果を生成
    index = 0
    for sentence in response.sentences:
        index += 1
        message += u"Sentence{} text: {}\n".format(
            index, sentence.text.content)
        message += u"Sentence{} sentiment score: {}\n".format(
            index, sentence.sentiment.score)
        message += u"Sentence{} sentiment magnitude: {}\n\n".format(
            index, sentence.sentiment.magnitude)
    return message

def main() -> None:
    text = input_text()
    response = analyze_sentiment(text)
    # 分液結果を表示用フォーマットに変換
    message = format_response_to_message(response)
    print(message)

if __name__ == "__main__":
    main()
