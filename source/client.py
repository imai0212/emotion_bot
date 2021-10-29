#!/usr/bin/env python


# see: https://github.com/googleapis/python-language

from google.cloud import language_v1
from google.cloud.language_v1.types.language_service import AnalyzeSentimentResponse


def analyze_sentiment(text: str) -> AnalyzeSentimentResponse:
    """
    Args:
        text: 分析したいテキスト
    Returns:
        感情分析のレスポンス
        https://cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeSentiment#response-body
    """

    # Natural Language API用のクライアントオブジェクトを取得します
    client = None

    # テキストのタイプを選択します
    # types: PLAIN_TEXT, HTML
    type_ = None

    # 分析したいテキストとテキストのタイプを指定して、
    # APIに渡すドキュメントオブジェクトを生成します
    document = None

    # 文字コードを指定する : NONE, UTF8, UTF16, UTF32
    encoding_type = None

    # ドキュメントと文字コードを指定して、
    # APIに分析を依頼して分析結果を受け取ります
    return None


def input_text() -> str:
    """
    標準入力から複数行のテキストを取得します。
    入力無しでEnter keyが押された場合に終了します。
    Returns:
        入力テキスト
    """
    texts = []

    while True:
        val = input()
        if len(val) == 0:
            break
        texts.append(val)
    return '\n'.join(texts)

def format_response_to_message(response: AnalyzeSentimentResponse) -> str:
    """
    Natural Language API のresponseをメッセージ形式にフォーマットします。
    Args:
        response: Natural Language API のresponse
    Returns:
        メッセージ形式にフォーマット済みの文字列
    """

    message = ""

    # テキスト全体の結果を生成します。
    message += "\n== Document ==\n\n"
    message += u"Document sentiment score: {}\n".format(
        response.document_sentiment.score)
    message += u"Document sentiment magnitude: {}\n".format(
        response.document_sentiment.magnitude)
    message += "\n== Sentences in the document ==\n\n"

    # 文章ごとの結果を生成します。
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
    message = format_response_to_message(response)
    print(message)

if __name__ == "__main__":
    main()
