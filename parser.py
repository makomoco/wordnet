import MeCab
import unicodedata
import re


class MecabParser():
    def __init__(self, word_classes=None, word_class_details=None):
        """
        Args:
            word_classes (list, optional): 日本語で品詞指定. Defaults to None.
            word_class_details (list, optional): 品詞の詳細の指定. Defaults to None.

        mecabの定義する品詞は以下参照
        https://taku910.github.io/mecab/posid.html
        """
        self._word_classes = word_classes
        self._word_class_details = word_class_details

    def _format_text(self, text):
        """
        MeCabに入れる前のテキストの整形
        """
        text = re.sub(r'http(s)?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
        text = re.sub(r'[ -/:-@\[-~_]', "", text)  # 半角記号
        text = re.sub(r'[︰-＠]', "", text)  # 全角記号
        text = re.sub(r'\d', "", text)  # 数字
        text = re.sub('\n', " ", text)  # 改行文字
        text = re.sub('\r', " ", text)  # 改行文字

        return text

    def parse(self, text, is_base=False):
        text = self._format_text(text)

        # 文字コード変換処理。変換しないと濁点と半濁点が分離する。
        text = unicodedata.normalize('NFC', text)

        result = []
        tagger = MeCab.Tagger(
            '-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd')
        # parseToNode前に一度parseしておくとsurfaceの読み取りエラーを回避できる
        tagger.parse('')

        nodes = tagger.parseToNode(text)
        while nodes:
            wclass = nodes.feature.split(',')
            # 品詞指定のない場合はすべて分かち書き
            if not self._word_classes:
                result.append(wclass[6] if is_base else nodes.surface)
                nodes = nodes.next
                continue

            # 品詞詳細の指定の無い場合はその品詞をすべて分かち書き
            if not self._word_class_details:
                if wclass[0] in self._word_classes:
                    result.append(wclass[6] if is_base else nodes.surface)
                    nodes = nodes.next
                    continue

            # 品詞詳細指定に従って分かち書き
            if wclass[0] in self._word_classes and wclass[1] in self._word_class_details:
                result.append(wclass[6] if is_base else nodes.surface)
            nodes = nodes.next

        # 最初と最後の空白文字列の削除
        if len(result) > 0:
            result.pop(0)
            result.pop(-1)

        return result