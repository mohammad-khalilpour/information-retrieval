import re


def is_link(token: str):
    url_pattern = re.compile(
        r'(?i)\b(?:https?://|www\d?\.)[^\s]+(?:[^\s.,;])'
    )

    return bool(re.match(url_pattern, token))


def is_id(token: str):

    return token.startswith('@')
