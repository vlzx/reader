import unicodedata
from typing import List, Dict

import jaconv
# from janome.tokenizer import Tokenizer
#
# tokenizer = Tokenizer()


def is_kanji(char: str):
    return unicodedata.name(char).startswith('CJK UNIFIED IDEOGRAPH')


def is_hiragana(char: str):
    return unicodedata.name(char).startswith('HIRAGANA')


def tokenize(text: str):
    tokens = []
    # for token in tokenizer.tokenize(text):
    #     # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
    #     keys = ['surface_form', 'pos', 'pos_detail_1', 'pos_detail_2', 'pos_detail_3',
    #             'conjugated_type', 'conjugated_form', 'basic_form',
    #             'reading', 'pronunciation']
    #     values = str(token).split('\t')
    #     values = [values[0], *values[1].split(',')]
    #     tokens.append(dict(zip(keys, values)))
    return tokens


def text2furigana(text: str):
    results = []
    for token in tokenize(text):
        results.extend(reading2furigana(token['surface_form'], token['reading']))
    return results


def reading2furigana(word: str, reading: str):
    tokens = []
    reading_hira = jaconv.kata2hira(reading)

    if all([is_kanji(ch) for ch in word]):
        tokens.append({'word': word, 'furigana': reading_hira})
    elif word in [reading_hira, reading] or reading == '*':
        tokens.append({'word': word, 'furigana': ''})
    elif any([is_kanji(ch) for ch in word]):
        tokens.extend(okurigana2furigana(word, reading_hira))
    else:
        tokens.extend({'word': word, 'furigana': ''})

    return tokens


def okurigana2furigana(word: str, reading: str):
    tokens = []
    word_index, reading_index = 0, 0
    while word_index < len(word):
        if word[word_index] == reading[reading_index]:
            tokens.append({'word': word[word_index], 'furigana': ''})
            word_index += 1
            reading_index += 1
        else:
            kanji = ''
            furigana = ''
            while word_index < len(word):
                if is_hiragana(word[word_index]):
                    break
                kanji += word[word_index]
                word_index += 1
            tailing_hira = ''
            if word_index < len(word):
                tailing_hira = word[word_index]
            while reading_index < len(reading):
                if tailing_hira and reading[reading_index] == tailing_hira:
                    if reading_index == len(reading) - 1:
                        break
                    elif reading[reading_index + 1] != tailing_hira:
                        break
                furigana += reading[reading_index]
                reading_index += 1
            tokens.append({'word': kanji, 'furigana': furigana})
    return tokens


if __name__ == '__main__':
    s = '今日はラーメンや寿司を食べたい。ショック、出会い、お茶、お母さん、ご主人様、駆け抜け、けん銃、可愛い'
    r = text2furigana(s)
    for x in r:
        if x["furigana"]:
            print(f'{x["word"]}({x["furigana"]})', end='')
        else:
            print(f'{x["word"]}', end='')
