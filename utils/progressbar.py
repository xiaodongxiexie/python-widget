"""
动态进度条。
"""
def progressbar(cur_num, total_num, 
                    min=0.8, gap=5, 
                    barwidth=50, 
                    cur_consume_time=None, 
                    total_consume_time=None):
    """
    :param            cur_num: 当前进行到第.次数
    :param         total_nums: 总次数
    :param                min: 到达总进度的min比例时，按gap显示进度
    :param                gap: 与min连用，抵达min进度时，步长gap显示一次进度
    :param           barwidth: 进度条显示宽度
    :param   cur_consume_time: 本次耗时
    :param total_consume_time: 总耗时
    """

    head  = "[{}/{}]".format(cur_num, total_num)
    back  = "\r"
    end   = ""
    arrow = ">"
    ratio = cur_num/total_num if total_num else 0

    finish   = int(barwidth*ratio)
    underway = barwidth - finish
    stat = ""
    if cur_consume_time is not None and total_consume_time is not None:
        stat = "[{:.2f}/{:.2f}]".format(cur_consume_time, total_consume_time)

    if finish == barwidth:
        arrow = "="

    if ratio >= min:
        if cur_num%gap == 1:
            back = ""
            end  = "\n"
        else:
            back = "\r"
            end  = ""

    content = "[" + finish * "=" + arrow + underway * "-" + "]" + stat + back
    print(head, content, end=end)


if __name__ == "__main__":
    import time, random

    start_ = time.time()
    start  = time.time()
    total_num = 50
    for i in range(total_num):
        time.sleep(random.random()/5)
        end = time.time()
        progressbar(i+1, total_num, min=0.6, 
            gap=8,
            cur_consume_time=round(end-start, 2), 
            total_consume_time=round(end-start_, 2))
        start = end 
