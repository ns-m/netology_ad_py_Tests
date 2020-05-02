import requests


URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def translate_to_file(text, lang):

    resp_translate = requests.post(URL, params={
        "key": "trnsl.1.1.20191128T170444Z.c56d359e1889b3b7.8fccca1aa4fe51ff1bb52de2213efc89f26608ff",
        "text": text,
        "lang": lang})

    resp_translate = resp_translate.json()["text"]
    resp_translate = ' '.join(resp_translate)
    return resp_translate


def translate_to_file_status_code(text, lang):

    resp_translate = requests.post(URL, params={
        "key": "trnsl.1.1.20191128T170444Z.c56d359e1889b3b7.8fccca1aa4fe51ff1bb52de2213efc89f26608ff",
        "text": text,
        "lang": lang})

    return resp_translate.status_code
