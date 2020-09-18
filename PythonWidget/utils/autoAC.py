# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date  : 2020/9/18


class AC:
    def __init__(self):
        self.d = {}
        self.end = "\x00"

    def preprocess(self, chars: str) -> str:
        return chars.lower()

    def add(self, chars: str) -> None:
        d = self.d
        chars = self.preprocess(chars)

        if not chars:
            return

        last = None
        for i, t in enumerate(chars):
            if i == len(chars) - 1:
                last[t] = {self.end: 0}
            else:
                if last is None:
                    last = d
                last = last.setdefault(t, {})

    def filter(self, msg, replace_by="*"):
        msg = self.preprocess(msg)
        ret = []
        start = 0
        while start < len(msg):
            exist = 0
            d = self.d
            for char in msg[start:]:
                if char in d:
                    exist += 1
                    if self.end not in d[char]:
                        d = d[char]
                    else:
                        ret.append(replace_by * exist)
                        start += exist - 1
                        break
                else:
                    ret.append(msg[start])
                    break
            else:
                ret.append(msg[start])

            start += 1
        return "".join(ret)

    def exist(self, msg):
        msg = self.preprocess(msg)
        start = 0
        while start < len(msg):
            exist = 0
            d = self.d
            for char in msg[start:]:
                if char in d:
                    exist += 1
                    if self.end not in d[char]:
                        d = d[char]
                    else:
                        start += exist - 1
                        return True
            start += 1
        return False
        
if __name__ == '__main__':

    ac = AC()
    chars = ("abc", "def", "aha")
    for char in chars:
        ac.add(char)

    txts = [
        "dsafasfdasdfbaha",
        "sfafdasfdafda",
        "abdsfa",
        "abc"
    ]
    for txt in txts:
        print(ac.exist(txt))
        print(ac.filter(txt))
        
