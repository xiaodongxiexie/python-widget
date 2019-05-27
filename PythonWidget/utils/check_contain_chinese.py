def contain_chinese(s):
    for ch in s:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
