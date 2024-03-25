from typing import List
import re
from preprocessings.utils.utils import is_link, is_id
from collections import defaultdict


class Normalizer:
    def __init__(self, delete_stop_words: bool = True, stop_words_count: int = 50, number_replacement: bool = True):
        self._delete_stop_words = delete_stop_words
        self._stop_words_count = stop_words_count
        self._stop_words = None

        self.number_replacement = number_replacement
        self.number_translation_src = "0123456789%٠١٢٣٤٥٦٧٨٩"
        self.number_translation_dst = "۰۱۲۳۴۵۶۷۸۹٪۰۱۲۳۴۵۶۷۸۹"

        self.stop_chars = [
            ".",
            "؟",
            "+",
            "!",
            ":",
            "؛",
            "٬",
            "٫",
            "،",
            ")",
            "(",
            "/",
        ]

        self.eerab = [
            ("[\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652]", ""),
        ]

        self.suffixes = {
            "ی",
            "ای",
            "ها",
            "های",
            "هایی",
            "تر",
            "تری",
            "ترین",
            "گر",
            "گری",
            "ام",
            "ات",
            "اش",
        }

        self.unicode_replacements = {
            "﷽": "بسم_الله_الرحمن_الرحیم",
            "﷼": "ریال",
            "(ﷰ|ﷹ)": "صلی",
            "ﷲ": "الله",
            "ﷳ": "اکبر",
            "ﷴ": "محمد",
            "ﷵ": "صلعم",
            "ﷶ": "رسول",
            "ﷷ": "علیه",
            "ﷸ": "وسلم",
            "ﻵ|ﻶ|ﻷ|ﻸ|ﻹ|ﻺ|ﻻ|ﻼ": "لا",
        }

    def normalize(self, tokens: List[str]):
        for i in range(tokens.__len__()):
            tokens[i] = tokens[i].replace('\u200C', 'ـ')

        for i in range(tokens.__len__()):
            for char in self.stop_chars:
                if not (is_link(tokens[i]) or is_id(tokens[i])):
                    tokens[i] = tokens[i].replace(char, '')

        for i in range(tokens.__len__()):
            for pattern, replacement in self.eerab:
                tokens[i] = re.sub(pattern, replacement, tokens[i])

        for i in range(tokens.__len__()):
            for pattern, replacement in self.unicode_replacements.items():
                tokens[i] = re.sub(pattern, replacement, tokens[i])

        if self.number_replacement:
            translation = {ord(a): b for a, b in zip(self.number_translation_src, self.number_translation_dst)}
            for i in range(tokens.__len__()):
                tokens[i] = tokens[i].translate(translation)

        if self._delete_stop_words:
            tokens = self.delete_stop_words(tokens)

        return tokens

    def detect_stop_words(self, tokens: List[str]):
        tokens_dic = defaultdict(int)
        for token in tokens:
            tokens_dic[token] += 1

        sorted_dict = dict(sorted(tokens_dic.items(), key=lambda item: item[1], reverse=True)[:self._stop_words_count])
        self._stop_words = sorted_dict.keys()

    def delete_stop_words(self, tokens: List[str]):

        filtered_tokens = [token for token in tokens if token not in self._stop_words]
        return filtered_tokens

