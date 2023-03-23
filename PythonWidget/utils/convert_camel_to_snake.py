import re


def convert_camel_to_snake(camel_str):
    return re.sub('(?!^)([A-Z]+)', r'_\1', camel_str).lower()


ef camel_to_snake(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
