import json
from googletrans import Translator


# 読み込み
def read(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)


# 書き込み
def save(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


target = read("./lang.json")
result = {}


translator = Translator(service_urls=['translate.googleapis.com'])


def toJapanise(text):
    return translator.translate(text, dest="ja").text


for key in target:
    text = toJapanise(target[key])
    print(text)
    result[key] = text

save("./ja_jp.json", result)
