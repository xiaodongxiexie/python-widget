# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from functools import partial
from reprlib import repr

class GentleShow:

    STYLE = {
            'fore': {
                    'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
                    'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37,
            },
            'back': {
                    'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
                    'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47,
            },
            'mode': {
                    'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7,
            },
            'default': {
                    'end': 0,
            }
    }

    def __init__(self, seq, *, column=4, fontdict=None):
        self.seq = seq
        self.column = column
        self.fontdict = fontdict


    def __repr__(self):
        return repr(','.join(self.gentle_show(layout=list)))


    def use_style(self, string, mode='', fore='', back='', special=True):
        STYLE = self.STYLE
        mode = '%s' % STYLE['mode'][mode] if mode in STYLE['mode'] else ''
        fore = '%s' % STYLE['fore'][fore] if fore in STYLE['fore'] else ''
        back = '%s' % STYLE['back'][back] if back in STYLE['back'] else ''
        style = ';'.join([s for s in [mode, fore, back] if s])
        style = '\033[%sm' % style if style else ''
        end = '\033[%sm' % STYLE['default']['end'] if style else ''
        if special:
            return '%s%s%s' % (style, string, end)
        else:
            return string


    def gentle_show(self, layout=str, isolate='|'):

        seq = self.seq
        column = self.column
        fontdict = self.fontdict

        if layout is str:
            ret = ''
            line_break = '\n'
            line_isolate = isolate
            flag = True
        elif layout is list:
            ret = []
            flag = False
            line_break = ''
            line_isolate = ''
        else:
            raise LayoutError('just support str and list')

        if fontdict is None:
            line_color = 'red'
            font_color = 'blue'
        elif isinstance(fontdict, dict):
            line_color = fontdict.get('line_color', 'red')
            font_color = fontdict.get('font_color', 'green')

        seq = list(map(str, seq))
        max_len = len(max(seq, key=len)) + 2

        use_bold_style = partial(self.use_style, mode='bold', special=flag)

        use_bold_line_style = partial(use_bold_style, fore=line_color)
        use_bold_font_style  = partial(use_bold_style, fore=font_color)

        for index, ele in enumerate(seq):
            if index % column == 0:
                string = '-' * max_len * column + '-' * (column - 1)
                string2 = ele.center(max_len, ' ')
                if flag:
                    ret += (use_bold_line_style(string) + line_break)
                    ret += (use_bold_font_style(string2) + line_isolate)
                else:
                    ret.append(use_bold_font_style(string2) + line_isolate)
            else:
                string3 = ele.center(max_len, ' ')
                if (index - column + 1) % column == 0:
                    if flag:
                        ret += (use_bold_font_style(string3) + line_break)
                    else:
                        ret.append(use_bold_font_style(string3) + line_break)
                else:
                    if flag:
                        ret += (use_bold_font_style(string3) + line_isolate)
                    else:
                        ret.append(use_bold_font_style(string3) + line_isolate)
        ret += line_break
        if not flag:
            return list(map(lambda x: x.strip(), ret))
        return ret


class LayoutError(BaseException):
    pass



if __name__ == "__main__":
    gentle_show = GentleShow(dir(10))
    print(gentle_show)
    print(gentle_show.gentle_show(str))
    print(gentle_show.gentle_show(str, '+'))
