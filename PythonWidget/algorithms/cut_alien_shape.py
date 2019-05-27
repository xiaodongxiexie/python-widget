# coding: utf-8
# ---------------------------------------------------------------------------
#    author: xiaodong                                                       #
#    根据ori [{'x': value, 'y': value}, ...., {'x': value, 'y': value}]     *
#    分别从横向或纵向逐个切割出多个矩形。                                       #
# ---------------------------------------------------------------------------

import copy

def gen_lines_from_ori_points(ori_points: list) -> list:
    """
    根据 ori [{'x': value, 'y': value}, ...., {'x': value, 'y': value}]
    生成线条。[[{'x': value, 'y': value}, {'x': value, 'y': value}], ...,
               {'x': value, 'y': value}, {'x': value, 'y': value}] ]
    """

    copy_ori = ori_points.copy()
    copy_ori.append(copy_ori[0])

    lines = []
    for i in range(len(copy_ori)-1):
        lines.append(copy_ori[i:i+2])
    return lines 


def gen_h_v_lines(lines):
    """
    :param lines: [[{}, {}], ..., [{}, {}]]
    :rtype      :dict
    :return     : 水平线 - 垂直线
    """
    # lines = gen_lines_from_ori_points(ori)
    h_lines, v_lines = [], []
    for line in lines:
        # 根据水平长度or垂直长度较大值决定
        if abs(line[0]['x']-line[1]['x']) > abs(line[0]['y']-line[1]['y']):
            h_lines.append(line)
        else:
            v_lines.append(line)
    ret = {'h_lines': h_lines,
           'v_lines': v_lines}
    return ret


def gen_map_points(lines, style='h'):
    """
    将所有点做映射到指定线上，生成可用于组成矩形的点。
    :param lines: h_lines or v_lines
    :param style: 'h' or 'v'
    :rtype      :  list  
    :return     :  [{'x': v, 'y': v2}, ..., {'x': v, 'y':v2}]
    """
    if style == 'h':
        taxis = 'x'  # target_axis
        oaxis = 'y'  # other_axis
    elif style == 'v':
        taxis = 'y'
        oaxis = 'x'
    points = []
    for i, line in enumerate(lines):
        for point in line:
            if point not in points:
                points.append(point)
        # 将其后每个线上对应点对应投射
        for line2 in lines[i+1:]:
            tlist = []
            for point in line + line2:
                tlist.append(point[taxis])
            line_length = abs(line[0][taxis]-line[1][taxis])
            line2_length = abs(line2[0][taxis]-line2[1][taxis])
            multi_length = max(tlist)-min(tlist)
            # 若叠加线段长度小于两者和，说明可以投射
            if multi_length <= line_length+line2_length:
                line_ = copy.deepcopy(line)
                line2_ = copy.deepcopy(line2)
                for point in line_:
                    tlist2 = [line2[0][taxis], line2[1][taxis]]
                    tmin = min(tlist2)
                    tmax = max(tlist2)
                    if tmin <= point[taxis] <= tmax:
                        point[oaxis] = line2[0][oaxis]
                        if point not in points:
                            points.append(point)
                for point in line2_:
                    tlist3 = [line[0][taxis], line[1][taxis]]
                    tmin2 = min(tlist3)
                    tmax2 = max(tlist3)
                    if tmin2 <= point[taxis] <= tmax2:
                        point[oaxis] = line[0][oaxis]
                        if point not in points:
                            points.append(point)
    return points


def collect_suit_points(points, style='h'):

    """
    :param points: 包含透射点在内的所有构成点
    :param style : 'h' or 'v' 决定图像切割方式
    :rtype       : list
    :return      : 构成矩形的四个点的集合(四个点无序。)
                    [
                        [{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v}],
                        ...
                        [{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v}]
                    ]
    """

    if style == 'h':
        taxis = 'x'
        oaxis = 'y'
    elif style == 'v':
        taxis = 'y'
        oaxis = 'x'
    tdict = {}
    # 根据target_axis 收集同点信息
    for point in points:
        tdict.setdefault(point[taxis], []).append(point[oaxis])
    t_dict_list = sorted(tuple(zip(tdict.keys(), tdict.values())), key=lambda obj: obj[0])

    rect_points = []
    # 将收集的信息点排序后，从后至前查找合适的矩形块
    for i in range(1, len(t_dict_list)):
        pre = t_dict_list[i-1]
        post = t_dict_list[i]
        rect = []
        recov_d = {}
        for cur_v in pre[1]:
            rect.append({taxis: pre[0], oaxis: cur_v})
        for cur_v in post[1]:
            rect.append({taxis: post[0], oaxis: cur_v})
        o_dict = {}
        for cur_d in rect:
            o_dict.setdefault(cur_d[oaxis], []).append(cur_d[taxis])
        sorted_o_dict = sorted(tuple(zip(o_dict.keys(), o_dict.values())))
        sorted_o_idct2 = []
        for o_dict in sorted_o_dict:
            if len(o_dict[1]) >= 2:
                sorted_o_idct2.append(o_dict)
        for index in range(1, len(sorted_o_idct2)):
            rect_point = []
            ddds = [{sorted_o_idct2[index][0]: sorted_o_idct2[index][1]}]
            ddds.append({sorted_o_idct2[index-1][0]: sorted_o_idct2[index-1][1]})
            for ddd in ddds:
                for k, vs in ddd.items():
                    rect_point.append({taxis: vs[0], oaxis: k})
                    rect_point.append({taxis: vs[1], oaxis:k})
                rect_points.append(rect_point)
    return rect_points


def offer_rects(rect_points):
    """
    :param rect_points: 构成矩形的四个点的集合(四个点无序。)
                    [
                        [{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v}],
                        ...
                        [{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v},{'x':v, 'y':v}]
                    ]
    :rtype           : list
    :return          : 返回矩形顺次点
    """
    rects = []
    for current_rect in rect_points:
        x0, x1, x3, x2 = sorted(current_rect, key=lambda obj: (obj['y'], obj['x']))
        rect = [x0, x1, x2, x3]
        rects.append(rect)
    return rects


def gen_cand_rects(ori, style='h'):
    """
    所有信息在此组装。
    """
    lines = gen_lines_from_ori_points(ori)
    h_v_lines = gen_h_v_lines(lines)
    tlines = h_v_lines['{}_lines'.format(style)]
    points = gen_map_points(tlines, style)
    rect_points = collect_suit_points(points, style)
    rects = offer_rects(rect_points)
    return rects
    

def rect2suit(rect):
    """
    将点矩形转换为需要的形式
    """
    xlist, ylist = [], []
    for ele in rect:
        xlist.append(ele['x'])
        ylist.append(ele['y'])
    x = min(xlist)
    y = min(ylist)
    dx = max(xlist) - x
    dy = max(ylist) - y
    ret = {}
    ret['x'] = x
    ret['y'] = y
    ret['dx'] = dx
    ret['dy'] = dy
    return ret


def gen_suit_rects_(ori):
    """
    分别横向纵向切割，选择最大面积在当前方出现的作为返回值
    """
    rects = gen_cand_rects(ori, style='h')
    rects2 = gen_cand_rects(ori, style='v')
    h_rects = []
    v_rects = []
    for rect in rects:
        cur_rect = rect2suit(rect)
        if cur_rect not in h_rects:
            h_rects.append(cur_rect)
    for rect in rects2:
        cur_rect = rect2suit(rect)
        if cur_rect not in v_rects:
            v_rects.append(cur_rect)
    max_h_rect = max(h_rects, key=lambda obj: obj['dx']*obj['dy'])
    max_v_rect = max(v_rects, key=lambda obj: obj['dx']*obj['dy'])
    if max_h_rect['dx']*max_h_rect['dy'] > max_v_rect['dx']*max_v_rect['dy']:
        print('h')
        result =  h_rects
    else:
        print('v')
        result =  v_rects
    result2 = []
    for rect in result:
        # 过滤有一边小于指定阈值的矩形
        if min(rect['dx'], rect['dy']) < 400:
            continue
        result2.append(rect)
    result2.sort(key=lambda obj: obj['dx']*obj['dy'], reverse=True)
    return result2


def gen_suit_rects(ori):
    """
    对于同簇矩形进行合并。
    """ 

    results = gen_suit_rects_(ori)

    xlist, ylist = [], []
    dxlist, dylist = [], []
    for obj in results:
        xlist.append(obj['x'])
        ylist.append(obj['y'])
        dxlist.append(obj['x']+obj['dx'])
        dylist.append(obj['y']+obj['dy'])
    max_rect = {}
    max_rect['x'] = min(xlist)
    max_rect['y'] = min(ylist)
    max_rect['dx'] = max(dxlist)-min(xlist)
    max_rect['dy'] = max(dylist)-min(ylist)
    max_rect_area = max_rect['dx']*max_rect['dy']
    sum_ori_rects_area = 0
    for rect in results:
        sum_ori_rects_area += rect['dx']*rect['dy']
    # 若合并后的矩形框大小与原有矩形总面积接近，使用合并后矩形
    if max_rect_area * 0.95 <= sum_ori_rects_area:
        print('使用合并后矩形框...')
        rects = [max_rect]
    else:
        rects = results
    return rects


if __name__ == '__main__':

    from matplotlib import pyplot as plt

    ori = [  {'x': 0,    'y': 0},
             {'x': 3700, 'y': 0},
             {'x': 3700, 'y': 1300},
             {'x': 3190, 'y': 1300},
             {'x': 3190, 'y': 1400},
             {'x': 3780, 'y': 1400},
             {'x': 3780, 'y': 2610},
             {'x': 0,    'y': 2610}]


    ori = [  {'x': 3790, 'y': 0},
             {'x': 4890, 'y': 0},
             {'x': 4910, 'y': 6680},
             {'x': 5320, 'y': 6680},
             {'x': 5320, 'y': 8480},
             {'x': 3790, 'y': 8480},
             {'x': 3790, 'y': 7890},
             {'x': 0,    'y': 7890},
             {'x': 0,    'y': 4090},
             {'x': 3790, 'y': 4090}]
    ori2 = [{'x': 1910, 'y': 0}, {'x': 3790, 'y': 0}, {'x': 3790, 'y': 4890}, {'x': 0, 'y': 4890}, {'x': 0, 'y': 0}, {'x': 1760, 'y': 0}, {'x': 1760, 'y': 1250}, {'x': 2310, 'y': 1250}, {'x': 2310, 'y': 1100}, {'x': 1910, 'y': 1100}]
    ori2 = [{'x': 1910, 'y': 0}, {'x': 3790, 'y': 0}, {'x': 3790, 'y': 4890}, {'x': 0, 'y': 4890}, {'x': 0, 'y': 0}, {'x': 1760, 'y': 0}, {'x': 1760, 'y': 1250}, {'x': 2310, 'y': 1250}, {'x': 2310, 'y': 1100}, {'x': 1910, 'y': 1100}]
    lines = gen_lines_from_ori_points(ori)
    v_lines = gen_h_v_lines(lines)['v_lines']
    h_lines = gen_h_v_lines(lines)['h_lines']

    if 1:
        fig, axis = plt.subplots(1, 2)
        i = 0
        for style in ['h', 'v']:
            unique_rects = []
            for rect in gen_cand_rects(ori, style):
                cur_rect = rect2suit(rect)
                if cur_rect not in unique_rects:
                    unique_rects.append(cur_rect)
                    # print(cur_rect)
                xlist44, ylist44 = [], []
                for ele in rect:
                    xlist44.append(ele['x'])
                    ylist44.append(ele['y'])
                xlist44.append(xlist44[0])
                ylist44.append(ylist44[0])
                axis[i].plot(xlist44, ylist44)

            xlist, ylist = [], []
            for ele in ori:
                xlist.append(ele['x'])
                ylist.append(ele['y'])
            axis[i].scatter(xlist, ylist, color='red', s=30)
            i += 1
        plt.show()