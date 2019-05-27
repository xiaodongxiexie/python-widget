#encoding:UTF-8
import os,json,time,codecs
import  sys
sys.path.append(".")
#from publictool
import mysqlHelper as mh

mysqlcon = mh.getMysqlConnection()

def InsertHouserInfo(FileName,debug=False):
    try:
        # mysqlcon = mh.getMysqlConnection()
        upt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     FileName = u"../data/h9月13（100）/h9月13（100）/南大和园-3房2厅1厨1卫1阳台-李一1.png.json"
        state = "正常"
        user_id = 0
        designer_id = 0
        sqlstr = "insert into house_info(file_name,upt,state,user_id,designer_id) values ('{0}','{1}','{2}','{3}','{4}')".format(
                FileName, upt, state, user_id,designer_id)
        try:
            cc = time.clock()
            cur = mysqlcon.cursor()
            if debug:
                print(sqlstr)
            x = cur.execute(sqlstr)
            cur.close()
            mysqlcon.commit()
            cc = time.clock() - cc
    #         print("InsertHouserInfo:", cc)
            return GetIDByFileAndUPT(FileName,upt)
        #     return True
        except ZeroDivisionError:
            print("error:", sqlstr)
            mysqlcon.rollback()
        #     return False
            return -1
        finally:
            # mysqlcon.close()
            pass
    except:
        print("Error: FileName={}".format(FileName))
        return -1


def GetIDByFileAndUPT(FileName="../data/h9月13（100）/h9月13（100）/南大和园-3房2厅1厨1卫1阳台-李一1.png.json",upt=""):
    # mysqlcon = mh.getMysqlConnection()
    try:
        cur = mysqlcon.cursor()
        sqlstr = "select id from house_info"
        if FileName != "":
            sqlstr += " where file_name='{0}' and upt ='{1}'".format(FileName,upt)
        # print(sqlstr)
        cur.execute(sqlstr)
        ret = cur.fetchall()
        if len(ret)==0:
            return -1
    #     for row in ret[-10:]:
    #         print(row)
        else:
            return ret[0][0]
    finally:
        # mysqlcon.close()
        pass

def InsertObjInfo(HouseID,ObjNode,debug=False):
    try:
        # mysqlcon = mh.getMysqlConnection()
        upt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     FileName = u"../data/h9月13（100）/h9月13（100）/南大和园-3房2厅1厨1卫1阳台-李一1.png.json"

        sqlstr = "insert into obj_info(house_id,ot,oc,x,y,z,dx,dy,dz,ct,ut,us) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                HouseID,ObjNode["ot"],ObjNode["oc"],ObjNode["x"],ObjNode["y"],ObjNode["z"],ObjNode["dx"],ObjNode["dy"],ObjNode["dz"],ObjNode["ct"],ObjNode["ut"],ObjNode["us"])
        try:
            cc = time.clock()
            cur = mysqlcon.cursor()
            if debug:
                print(sqlstr)
            x = cur.execute(sqlstr)
            cur.close()
            mysqlcon.commit()
            cc = time.clock() - cc
    #         print("InsertObjInfo:", cc)
            return True#GetIDByFileAndUPT(FileName,upt)
        #     return True
        except ZeroDivisionError:
            print("error:", sqlstr)
            mysqlcon.rollback()
        #     return False
            return False
        finally:
            # mysqlcon.close()
            pass
    except:
        print("Error :HouseID={}".format(HouseID))
        pass

def GetWoShi(hid, markFile="../data/h9月13（100）/h9月13（100）/南大和园-3房2厅1厨1卫1阳台-李一1.png.json", min_size=2000, debug=False):
    House = json.load(codecs.open(markFile, encoding="utf-8"))
    if House["objNodeList"] == []:
        return [], [], []
    scaleRate = max(House["dx"], House["dy"]) / max(House["objNodeList"][House["idx"]]["dx"],
                                                    House["objNodeList"][House["idx"]]["dy"])
    for obj in House["objNodeList"]:
        obj["x"] = round(scaleRate * obj["x"], 0)
        obj["y"] = round(scaleRate * obj["y"], 0)
        obj["z"] = round(scaleRate * obj["z"], 0)
        obj["dx"] = round(scaleRate * obj["dx"], 0)
        obj["dy"] = round(scaleRate * obj["dy"], 0)
        obj["dz"] = round(scaleRate * obj["dz"], 0)

        if hid > 0:
            InsertObjInfo(hid, obj)
    file = markFile.split("/")[-1]
    QuYu = []
    WuPin = []
    for obj in House["objNodeList"]:
        WuPin.append({"ot": obj["ot"], "oc": obj["oc"], "x": obj["x"], "dx": obj["dx"], "y": obj["y"], "dy": obj["dy"],
                      "file": file})
        if obj["ot"] == '区域':
            QuYu.append(
                {"ot": obj["ot"], "oc": obj["oc"], "x": obj["x"], "dx": obj["dx"], "y": obj["y"], "dy": obj["dy"],
                 "file": file})
    WoShi = []
    for obj in QuYu:
        if '卧' in obj["oc"] or '儿童' in obj["oc"] or "书房" in obj["oc"] or "老人房" in obj["oc"]:
            if (min(obj["dx"], obj["dy"]) < min_size):
                if debug:
                    print("too small:", obj["ot"], obj["oc"], obj["dx"], obj["dy"])
                continue
            WoShi.append(
                {"ot": obj["ot"], "oc": obj["oc"], "x": obj["x"], "dx": obj["dx"], "y": obj["y"], "dy": obj["dy"],
                 "file": file})
    # print(obj)


    return WoShi, QuYu, WuPin


def GetWoShiFromDir(path=r"C:\work\户型标注验收\test\h9月13（100）", debug=False, insertDB=False):
    import os
    fl = os.listdir(path)
    all_ws = []
    all_wp = []
    all_qy = []
    c = 0
    for f in fl:
        if "png.json" in f:
            # 插入mysql表house_info/obj_info
            hid = -1
            if insertDB:
                hid = InsertHouserInfo(f)
                print(hid)
            wss, qys, wps = GetWoShi(hid, markFile=path + "/" + f, debug=debug)
            #             break
            c += 1
            if debug:
                print(f, wss)
            all_ws.extend(wss)
            all_wp.extend(wps)
            all_qy.extend(qys)

            if debug and len(wss) > 0:
                print(wss[0])
                #                 break
    print(c)
    return all_ws, all_wp, all_qy

def MatchObj(objs, x, ot="*", oc="*", k1=0.2, k2=0.2, rc=5, debug=False):
    a = x["dx"]
    b = x["dy"]
    #     x["_dx"]=min(a,b)
    #     x["_dy"]=max(a,b)
    # 面积
    x["a"] = round(a * b / 1000000, 1)
    # 宽高比
    x["b"] = round(max(a, b) / min(a, b), 1)
    if debug:
        print("输入：", x)
    i = 0
    X = []
    for ws in objs:
        a = ws["dx"]
        b = ws["dy"]
        #         ws["_dx"]=min(a,b)
        #         ws["_dy"]=max(a,b)
        # 面积
        ws["a"] = round(a * b / 1000000, 1)
        # 宽高比
        ws["b"] = round(max(a, b) / min(a, b), 1)

        #     print(ws)
        score = 0
        if ot != "*":
            if ot != ws["ot"]:
                #         print("类型不匹配~")
                continue
        if oc != "*":
            if oc != ws["oc"]:
                #         print("类型不匹配~")
                continue

        _k1 = abs(x["a"] - ws["a"]) / x["a"]
        _k2 = abs(x["b"] - ws["b"]) / x["b"]
        if _k1 < k1:
            if _k2 < k2:
                score = 1 - (_k1 + _k2) / 2
                ws["s"] = round(score, 2)
                X.append(ws)

        i += 1
        if i > 100000:
            break
        if len(X) >= rc:
            break
    if debug:
        print("--------")
        print(len(X))
        for x in X:
            print(x)
    X.sort(key=lambda x: (x["s"]), reverse=True)
    return X


def GetObjInside(objs, x, ot="*", oc="*", k=0.1, rc=20, debug=False):
    L = x["x"]
    R = L + x["dx"]
    T = x["y"]
    B = T + x["dy"]
    a = x["dx"]
    b = x["dy"]
    #     x["dx"]=min(a,b)
    #     x["dy"]=max(a,b)
    # 面积
    x["a"] = round(a * b / 1000000, 1)
    # 宽高比
    x["b"] = round(max(a, b) / min(a, b), 1)
    if debug:
        print("输入：", x)
    i = 0

    OBJ = []
    for ws in objs:
        _L = ws["x"]
        _R = _L + ws["dx"]
        _T = ws["y"]
        _B = _T + ws["dy"]

        a = ws["dx"]
        b = ws["dy"]
        #         ws["dx"]=min(a,b)
        #         ws["dy"]=max(a,b)
        # 面积
        ws["a"] = round(a * b / 1000000, 1)
        # 宽高比
        ws["b"] = round(max(a, b) / min(a, b), 1)

        #     print(ws)
        score = 0
        if x["file"] != ws["file"]:
            #             print("户型图不一致~")
            continue
        # print(ws)
        if ot != "*":
            if x["ot"] != ws["ot"]:
                #         print("类型不匹配~")
                continue
        if oc != "*":
            if x["oc"] != ws["oc"]:
                #         print("类型不匹配~")
                continue

        _k1 = abs(L - R) * k
        _k2 = abs(T - B) * k

        if (_L > L - _k1 and _R < R + _k1 and _T > T - _k2 and _B < B + _k2):
            #             print(_k1,_k2)
            OBJ.append(ws)
        else:
            if ws["ot"] == "家具":
                pass
                #                 print(ws)

        i += 1
        if i > 100000:
            break
        if len(OBJ) >= rc:
            break
    if debug:
        print("--------")
        print(len(OBJ))
        for x in OBJ:
            print(x)

    return OBJ

def GetObjAround(objs, x, ot="*", oc="*", k=0.1, k2=200, rc=20,change=True,debug=False):
    L = x["x"]
    R = L + x["dx"]
    T = x["y"]
    B = T + x["dy"]
    a = x["dx"]
    b = x["dy"]
    #     x["dx"]=min(a,b)
    #     x["dy"]=max(a,b)
    # 面积
    x["a"] = round(a * b / 1000000, 1)
    # 宽高比
    x["b"] = round(max(a, b) / min(a, b), 1)
    if debug:
        print("输入：", x)
    i = 0
    L -= k2
    R += k2
    T -= k2
    B += k2
    OBJ = []
    for ws in objs:
        if ws["ot"] != "门窗" and ws["ot"] != "墙体" and ws["ot"] != "区域":
            continue
        _L = ws["x"]
        _R = _L + ws["dx"]
        _T = ws["y"]
        _B = _T + ws["dy"]

        a = ws["dx"]
        b = ws["dy"]
        #         ws["dx"]=min(a,b)
        #         ws["dy"]=max(a,b)
        # 面积
        ws["a"] = round(a * b / 1000000, 1)
        # 宽高比
        ws["b"] = round(max(a, b) / min(a, b), 1)

        #     print(ws)
        score = 0
        if x["file"] != ws["file"]:
            #             print("户型图不一致~")
            continue
        # print(ws)
        if ot != "*":
            if x["ot"] != ws["ot"]:
                #         print("类型不匹配~")
                continue
        if oc != "*":
            if x["oc"] != ws["oc"]:
                #         print("类型不匹配~")
                continue

        _k1 = abs(L - R) * k
        _k2 = abs(T - B) * k
        _k1 = k2
        _k2 = k2

        # 内部的
        #         if (_L>L-_k1 and _R<R + _k1 and _T>T-_k2 and _B<B + _k2):
        # #             print(_k1,_k2,ws)
        #             #OBJ.append(ws)
        #             pass
        #         else:
        # 不能太远！
        # 扩大范围

        # 和范围有交集的 墙体 门窗
        if ws["ot"] == "门窗" or ws["ot"] == "墙体" or ws["ot"] == "区域":
            if min(_R, R) > max(_L, L) and min(_B, B) > max(_T, T):
                OBJ.append(ws)

        i += 1
        if i > 100000:
            break
        if len(OBJ) >= rc:
            break
    if debug:
        print("--------")
        print(len(OBJ))
        for x in OBJ:
            print(x)

    return OBJ

import copy
def CopyObjs(objs):
    return copy.deepcopy(objs)

def CopyObj(obj):
    return copy.deepcopy(obj)

def RoteObjs(Y, deg=0,change=True):

    _Y = CopyObjs(Y)
    if deg == 0 or deg == 360:
        pass
    if deg == 90:
        for obj in _Y:
            dy = obj["dy"]
            dx = obj["dx"]
            x = obj["x"]
            y = obj["y"]
            obj["x"] = -y - dy
            obj["y"] = x
            obj["dx"] = dy
            obj["dy"] = dx
    if deg == 180:
        for obj in _Y:
            dy = obj["dy"]
            dx = obj["dx"]
            x = obj["x"]
            y = obj["y"]
            obj["x"] = -x - dx
            obj["y"] = -y - dy
            obj["dx"] = dx
            obj["dy"] = dy
    if deg == 270:
        for obj in _Y:
            dy = obj["dy"]
            dx = obj["dx"]
            x = obj["x"]
            y = obj["y"]
            obj["x"] = y
            obj["y"] = -x - dx
            obj["dx"] = dy
            obj["dy"] = dx

    if change:
        dx0, dy0 = GetOriPoint(_Y)
        _Y = ChangeOriPoint(_Y, dx0, dy0)
    return _Y

def GetOriPoint(objs):
    x0 = 999999999
    y0 = 999999999
    for obj in objs:
        x0 = min(obj["x"], x0)
        y0 = min(obj["y"], y0)
    return x0, y0

def ChangeOriPoint(objs, dx0=0, dy0=0):
    _objs = CopyObjs(objs)
    for obj in _objs:
        obj["x"] -= dx0
        obj["y"] -= dy0
    return _objs

def MirroObjs(objs,typ="x",change=True):
    _objs = CopyObjs(objs)
    if typ =="x":
        for obj in _objs:
            dy = obj["dy"]
            dx = obj["dx"]
            x = obj["x"]
            y = obj["y"]
            obj["x"] = x
            obj["y"] = -y - dy
            obj["dx"] = dx
            obj["dy"] = dy
    else:
        for obj in _objs:
            dy = obj["dy"]
            dx = obj["dx"]
            x = obj["x"]
            y = obj["y"]
            obj["x"] = -x - dx
            obj["y"] = y
            obj["dx"] = dx
            obj["dy"] = dy

    if change:
        dx0, dy0 = GetOriPoint(_objs)
        _objs = ChangeOriPoint(_objs, dx0, dy0)
    return _objs

def MakeObjsList(Y):
    # 平移
    dx0, dy0 = GetOriPoint(Y)
    _Y = ChangeOriPoint(Y, dx0, dy0)
    # 旋转
    Y90 = RoteObjs(_Y, 90)
    Y180 = RoteObjs(_Y, 180)
    Y270 = RoteObjs(_Y, 270)
    Y0 = RoteObjs(_Y, 0)
    # 镜像
    Y0_y = MirroObjs(Y0, "y")
    Y90_y = MirroObjs(Y90, "y")
    Y0_x = MirroObjs(Y0, "x")
    Y90_x = MirroObjs(Y90, "x")

    # dx0, dy0 = GetOriPoint(objs)
    # _objs = ChangeOriPoint(objs, dx0, dy0)

    objsList = []
    objsList.append(Y0)
    objsList.append(Y90)
    objsList.append(Y180)
    objsList.append(Y270)
    objsList.append(Y0_x)
    objsList.append(Y0_y)
    objsList.append(Y90_x)
    objsList.append(Y90_y)
    return objsList


def ObjCross(obj1, obj2, debug=False):
    L = obj1["x"]
    R = L + obj1["dx"]
    T = obj1["y"]
    B = T + obj1["dy"]

    _L = obj2["x"]
    _R = _L + obj2["dx"]
    _T = obj2["y"]
    _B = _T + obj2["dy"]

    # 和范围有交集的
    if min(_R, R) > max(_L, L) and min(_B, B) > max(_T, T):
        return True
    return False


def BuildStringForObjs(objs, width=1000, height=1000, sm="门",sc="窗",sq="墙",sk="空",debug=False):
    # 获取门窗
    mlist = []
    clist = []
    qlist =[]
    for o in objs:
        if "门" in o["oc"]:
            mlist.append(o)
        if "窗" in o["oc"]:
            clist.append(o)
        if "墙" in o["ot"]:
            qlist.append(o)

    # 获取区域
    x = 0
    y = 0
    w = 0
    h = 0
    for obj in objs:
        if "墙" in obj["ot"]:
            continue
        R = obj["x"] + obj["dx"]
        B = obj["y"] + obj["dy"]
        w = max(w, R)
        h = max(h, B)
        #TODO 墙体裁剪未做
        if obj["ot"]=="区域":
            w=R
            h=B
            break

        # 网格化
    #     width=100
    #     height=100
    m = int(h // width)
    n = int(w // height)
    pl = []
    for j in range(n):
        #     print(j,0)
        pl.append((j, 0))
    # print("-"*8)
    for i in range(m):
        #     print(n,i)
        pl.append((n, i))
    # print("-"*8)
    for i in range(n, 0, -1):
        #     print(i,m)
        pl.append((i, m))

    # print("-"*8)
    for j in range(m, 0, -1):
        #     print(0,j)
        pl.append((0, j))
    objlist = []
    for p in pl:
        obj = {}
        obj["x"] = p[0] * width
        obj["y"] = p[1] * height
        obj["dx"] = width
        obj["dy"] = height
        objlist.append(obj)

    # 编码
    c = "门"
    s = ""
    for o in objlist:
        cm = False
        cc = False
        cq = False
        for m in mlist:
            cm = ObjCross(o, m)
            #         print(o,cm)
            if cm:
                break
        for c in clist:
            cc = ObjCross(o, c)
            #         print(o,cc)
            if cc:
                break
        for q in qlist:
            cq = ObjCross(o, q)
            #         print(o,cc)
            if cc:
                break
        if cm:
            s += sm#"门"
        elif cc:
            s += sc#"窗"
        elif cq:
            s += sq#"墙"
        else:
            s+=sk#"＃"
    return s
    # print(s)

import difflib

# 原来的相似度，慢
def GetEditDistance_OLD(l1, l2):
    dis = 0
    # cc = time.clock()
    d = difflib.SequenceMatcher(None, l1, l2)
    # cc = time.clock()-cc
    for tag, i1, i2, j1, j2 in d.get_opcodes():
        if tag == 'replace':
            dis += max(i2 - i1, j2 - j1)
        elif tag == 'insert':
            dis += (j2 - j1)
        elif tag == 'delete':
            dis += i2 - i1
    return round(1 - dis / (1 + len(l1) + len(l2)) * 2,2)  # ,cc

# 优化后的，快
def GetEditDistance(l1, l2):
    # dis=0
    # cc = time.clock()
    len1 = len(l1)
    len2 = len(l2)
    kk = (min(len1, len2) + 1) / (max(len1, len2) + 1)
    d = difflib.SequenceMatcher(None, l1, l2)
    k = d.real_quick_ratio()
    if k > 0.8:
        k = d.quick_ratio()
        if k > 0.8:
            k = d.ratio()
    # cc = time.clock()-cc
    # print(len1,"\t",len2,"\t",kk,"\t",k)
    return round(k * k * kk,2)
# if __name__ == "__main__":
#     InsertHouserInfo("a.png.json")
#     aws,awp,aqy = GetWoShiFromDir(path="../data/all/",insertDB=True)