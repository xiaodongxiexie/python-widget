import pymysql
import time
import socket
import os
import getpass

from configparser import ConfigParser

conf = ConfigParser()
conf.read(os.path.join(os.path.dirname(__file__)) + '/database.cfg')  # 读入配置文件
ip = conf.get('mysql', 'ip')
port = conf.getint('mysql', 'port')
database = conf.get('mysql', "database")
user = conf.get('mysql', 'user')
password = conf.get('mysql', 'password')


# 获取mysql连接
def getMysqlConnection():
    return pymysql.connect(host=ip, port=port, user=user, passwd=password, db=database, use_unicode = True,charset = 'utf8')



def InsertFileRefreshInfo(FileName="", eng_pid=0, eng_path=""):
    mysqlcon = getMysqlConnection()
    upt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = "insert into file_refresh_info(file_path,upt,eng_pid,eng_path) values ('{0}','{1}','{2}','{3}')".format(
        FileName, upt, eng_pid, eng_path)
    try:
        cc = time.clock()
        cur = mysqlcon.cursor()
        print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()
        cc = time.clock() - cc
        print("InsertfileRefreshInfo:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


def InsertTaskInfo(FileName=""):
    mysqlcon = getMysqlConnection()
    exp_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = "insert into pm_task_info(task_file,task_level,task_name,task_state,exp_start_time) values ('{0}','{1}','{2}','{3}','{4}')".format(
        FileName, "normal", "test", "", exp_start_time)
    try:
        cc = time.clock()
        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


        print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()
        cc = time.clock() - cc
        print("InsertTaskInfo:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


def ShowFileRefreshInfo(FileName=""):
    # host="127.0.0.1"
    mysqlcon = getMysqlConnection()
    cur = mysqlcon.cursor()
    sqlstr = "select * from file_refresh_info"
    if FileName != "":
        sqlstr += " where file_path='{0}'".format(FileName)
    print(sqlstr)
    cur.execute(sqlstr)
    ret = cur.fetchall()
    for row in ret[-10:]:
        print(row)
    cur.close()


def ShowTaskInfo(FileName=""):
    # host="127.0.0.1"
    mysqlcon = getMysqlConnection()
    cur = mysqlcon.cursor()
    sqlstr = "select * from pm_task_info"
    if FileName != "":
        sqlstr += " where file_path='{0}'".format(FileName)
    print(sqlstr)
    cur.execute(sqlstr)
    ret = cur.fetchall()
    for row in ret[-10:]:
        print(row)
    cur.close()


# 获取没有 done的列表
def GetTaskList(FileName=""):
    # host="127.0.0.1"
    FileList = []
    mysqlcon = getMysqlConnection()
    try:
        cur = mysqlcon.cursor()
        sqlstr = "select task_file,exp_start_time from pm_task_info"

        sqlstr += " where (task_state ='' or task_state = 'running' or task_state IS NULL)"
        if FileName != "":
            if not FileName.endswith("/"):
                FileName += "/"
            sqlstr += " and task_file like '{0}%'".format(FileName)
        # print(sqlstr)
        cur.execute(sqlstr)
        ret = cur.fetchall()
        for row in ret[-10:]:
            # print(row)
            FileList.append([row[0], str(row[1])])
        cur.close()
    finally:
        mysqlcon.close()
        return FileList


# 设置done|fail|err
def UpdateTaskInfoAfterDone(FileName, exp_start_time, task_state=""):
    mysqlcon = getMysqlConnection()
    real_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = "update pm_task_info set task_state='{0}',real_end_time='{1}'".format(task_state, real_end_time)
    # mysql Mode
    sqlstr += " where task_file = '{0}' and exp_start_time='{1}'".format(FileName, exp_start_time)
    # File Mode
    # sqlstr += " where task_file = '{0}'".format(FileName)
    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpdateTaskInfo:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


# 设置done|fail|err
def UpdateTaskInfoBeforeDone(FileName, exp_start_time, task_state=""):
    mysqlcon = getMysqlConnection()
    real_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = "update pm_task_info set task_state='{0}',real_start_time='{1}'".format(task_state, real_start_time)
    # mysql Mode
    sqlstr += " where task_file = '{0}' and exp_start_time='{1}'".format(FileName, exp_start_time)
    # File Mode
    # sqlstr += " where task_file = '{0}'".format(FileName)
    try:
        cc = time.clock()
        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        #print("UpdateTaskInfo:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


# 添加引擎
def InsertEngineInfo(EngineName="", engine_state="", svr_name="", svr_ip="",eng_type=""):
    mysqlcon = getMysqlConnection()

    cc = time.clock()

    cur = mysqlcon.cursor()
    # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    boot_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # svr_name = socket.gethostname()
    # svr_ip = socket.gethostbyname((svr_name))
    eng_pid = os.getpid()
    user_name = getpass.getuser()
    sqlstr = "insert into pm_engine_info(eng_path,state,boot_time,install_time,svr_name,svr_ip,eng_pid,start_user,eng_type) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}')".format(
        EngineName, engine_state, boot_time, boot_time, svr_name, svr_ip, eng_pid, user_name,eng_type)
    print(sqlstr)

    try:
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        print("InsertEngineInfo:", cc)
        return True
    except ZeroDivisionError:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


# 重启引擎（如果不存在，返回false)
def ResetEngineInfo(EngineName="", engine_state="", svr_name="", svr_ip="",eng_type=""):
    mysqlcon = getMysqlConnection()
    cur = mysqlcon.cursor()
    boot_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # svr_name = socket.gethostname()
    # svr_ip = socket.gethostbyname((svr_name))
    eng_pid = os.getpid()
    user_name = getpass.getuser()
    sqlstr = "update pm_engine_info set state='{0}',boot_time='{1}',svr_name='{2}',svr_ip='{3}',eng_pid='{4}',start_user='{5}'".format(
        engine_state, boot_time, svr_name, svr_ip, eng_pid, user_name)
    sqlstr += " where eng_path = '{0}' and eng_type = '{1}' ".format(EngineName,eng_type)
    try:
        cc = time.clock()

        # print(sqlstr)
        iret = cur.execute(sqlstr)
        # print(iret)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpateEngineInfo:",cc)
        if iret >= 1:
            return True
        else:
            return False
    except ZeroDivisionError:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


# 引擎上报状态
def UpdateEngineInfo(EngineName="", engine_state="", pdf_file="", cur_progress="0",eng_type=""):
    mysqlcon = getMysqlConnection()
    last_up_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = ""
    if pdf_file != "":
        sqlstr = "update pm_engine_info set state='{0}',last_up_time='{1}',last_file='{2}',cur_progress='{3}',last_time='{4}'".format(
            engine_state, last_up_time, pdf_file, cur_progress, last_up_time)
    else:
        sqlstr = "update pm_engine_info set state='{0}',last_up_time='{1}'".format(engine_state, last_up_time)
    sqlstr += " where eng_path = '{0}' and eng_type='{1}'".format(EngineName,eng_type)

    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(sqlstr)
        cur.execute(sqlstr)
        # print("UpateEngineInfo1:", cc)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpateEngineInfo2:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


def UpdateEngineInfoBeforeTask(EngineName="", engine_state="",eng_type=""):
    mysqlcon = getMysqlConnection()
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = ""

    sqlstr = "update pm_engine_info set state='{0}',start_time='{1}'".format(engine_state, start_time)
    sqlstr += " where eng_path = '{0}' and eng_type='{1}'".format(EngineName, eng_type)

    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(sqlstr)
        cur.execute(sqlstr)
        # print("UpateEngineInfo1:", cc)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpateEngineInfo2:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


# 获取引擎列表
def GetEngineList(ip=""):
    # host="127.0.0.1"
    FileList = []
    mysqlcon = getMysqlConnection()
    try:
        cur = mysqlcon.cursor()
        sqlstr = "select eng_path,state,last_up_time,eng_pid from pm_engine_info"
        if ip != "":
            sqlstr += " where (svr_ip ='{0}')".format(ip)

        # print(sqlstr)
        cur.execute(sqlstr)
        ret = cur.fetchall()
        for row in ret[:]:
            # print(row)
            FileList.append([row[0], str(row[1]), str(row[2]), row[3]])
        cur.close()
    finally:
        mysqlcon.close()
        return FileList


# 上报服务器固定信息
def UpdateServerFixInfo(ip=""):
    mysqlcon = getMysqlConnection()
    import uuid
    import platform
    import psutil

    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]

    name = platform.node()
    cpu = psutil.cpu_count()
    meminfo = psutil.virtual_memory()
    mem = round(meminfo.total / 1024 / 1024 / 1024, 0)
    machine = platform.machine()
    osname = platform.system() + platform.release()
    python = platform.python_version()
    cpu_use = psutil.cpu_percent()
    mem_use = meminfo.percent
    last_up_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = ""

    sqlstr = "update pm_svr_info set mac='{0}',name='{1}',cpu='{2}',mem='{3}',os='{4}',machine='{5}',python='{6}'".format(
        mac, name, cpu, mem, osname, machine, python)
    sqlstr += " where ip = '{0}' ".format(ip)

    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(sqlstr)
        cur.execute(sqlstr)
        # print("UpateEngineInfo1:", cc)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpateEngineInfo2:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


# 上报服务器动态信息
def UpdateServerDynamicInfo(ip=""):
    import platform
    import psutil
    mysqlcon = getMysqlConnection()
    name = platform.node()
    cpu = psutil.cpu_count()
    meminfo = psutil.virtual_memory()
    mem = round(meminfo.total / 1024 / 1024 / 1024, 0)
    machine = platform.machine()
    osname = platform.system() + platform.release()
    python = platform.python_version()
    cpu_use = psutil.cpu_percent()
    mem_use = meminfo.percent
    pids = len(psutil.pids())
    last_up_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = ""

    sqlstr = "update pm_svr_info set last_up_time='{0}',cpu_use='{1}',mem_use='{2}',pids='{3}'".format(last_up_time,
                                                                                                       cpu_use,
                                                                                                       mem_use, pids)
    sqlstr += " where ip = '{0}' ".format(ip)

    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(sqlstr)
        cur.execute(sqlstr)
        # print("UpateEngineInfo1:", cc)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpateEngineInfo2:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


import psutil, time

net_io = 0  # psutil.net_io_counters()
disk_io = 0  # psutil.disk_io_counters()
last_clock = time.clock()


def UpdateServerIOInfoInit():
    import psutil
    global net_io
    global disk_io
    try:
        net_io = psutil.net_io_counters()
    except:
        pass
    try:
        disk_io = psutil.disk_io_counters()
    except:
        pass


# 获取服务器IO信息
# 每隔一段时间的增量
def GetServerIOInfo():
    import psutil
    global net_io
    global disk_io
    global last_clock
    net_recv = 0
    net_sent = 0
    disk_read = 0
    disk_write = 0
    step = time.clock() - last_clock
    try:
        cur_net_io = psutil.net_io_counters()
        # cur_disk_io = psutil.disk_io_counters()
        net_recv = cur_net_io.bytes_recv - net_io.bytes_recv
        net_sent = cur_net_io.bytes_sent - net_io.bytes_sent
        # print(net_recv,net_sent)
        net_io = cur_net_io
    except:
        # print("net io err")
        pass
    try:
        cur_disk_io = psutil.disk_io_counters()
        # cur_disk_io = psutil.disk_io_counters()
        disk_read = cur_disk_io.read_bytes - disk_io.read_bytes
        disk_write = cur_disk_io.write_bytes - disk_io.write_bytes
        # print(disk_read,disk_write)
        disk_io = cur_disk_io
    except:
        # print("disk io err")
        pass
    last_clock = time.clock()
    return {"net_recv": net_recv, "net_sent": net_sent, "disk_read": disk_read, "disk_write": disk_write, "step": step}


def UpdateServerIOInfo(ip="", unit="MB"):
    mysqlcon = getMysqlConnection()

    sqlstr = ""
    io_info = GetServerIOInfo()
    # print(io_info)
    step = io_info["step"]
    u = 1024 * 1024
    if unit == "KB":
        u = 1024
    nr = round(io_info["net_recv"] / step / u, 2)
    ns = round(io_info["net_sent"] / step / u, 2)
    dr = round(io_info["disk_read"] / step / u, 2)
    dw = round(io_info["disk_write"] / step / u, 2)

    # print(step, nr, ns, dr, dw)
    sqlstr = "update pm_svr_info set net_recv='{0}',net_sent='{1}',disk_read='{2}',disk_write='{3}'".format(
        nr, ns, dr, dw
    )
    sqlstr += " where ip = '{0}' ".format(ip)

    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # print(sqlstr)
        cur.execute(sqlstr)
        # print("UpateEngineInfo1:", cc)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        # print("UpateEngineInfo2:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()


def InsertEngineLogInfo(eng_log):

    eng_ip = eng_log["eng_ip"]
    mode = eng_log["mode"]
    if "eng_path" not in eng_log:
        return False

    eng_path = eng_log["eng_path"]
    pdf_name = eng_log["pdf_name"]
    file_size = eng_log["file_size"]
    page_count = eng_log['page_count']
    pdf2xml = round(eng_log['pdf2xml'], 2)
    xml2data = round(eng_log["xml2data"], 2)
    data2pos = 0
    try:
        data2pos = round(eng_log["data2pos"], 2)
    except:
        pass
    pos2biz = 0
    try:
        pos2biz = round(eng_log["pos2biz"], 2)
    except:
        pass
    data4html = 0
    try:
        data4html = round(eng_log["data4html"], 2)
    except:
        pass
    data2mongo = 0
    try:
        data2mongo = round(eng_log["data2mongo"], 2)
    except:
        pass
    page2image = 0
    try:
        page2image = round(eng_log["page2image"], 2)
    except:
        pass
    start_time = eng_log["start_time"]
    end_time = eng_log["end_time"]

    mysqlcon = getMysqlConnection()

    sqlstr = "insert into pm_engine_log (ip,mode,eng_path,pdf_name,file_size,page_count,pdf2xml,xml2data,data2pos,pos2biz,data4html,data2mongo,page2image,start_time,end_time) " \
             "values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}'," \
             "'{11}','{12}','{13}','{14}')".format(eng_ip, mode,eng_path, pdf_name,
                                            file_size,
                                            page_count,
                                            pdf2xml,
                                            xml2data,
                                            data2pos,
                                            pos2biz,
                                            data4html,
                                            data2mongo,
                                            page2image,
                                            start_time,
                                            end_time)
    try:
        cc = time.clock()
        cur = mysqlcon.cursor()
        print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()
        cc = time.clock() - cc
        print("InsertfileRefreshInfo:", cc)
        return True
    except :
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()

# 获取标注列表
def GetMarkListFromDB(ips="192.168.2.103",storeip="192.168.2.103"):
    # host="127.0.0.1"
    MarkList = []
    mysqlcon = getMysqlConnection()
    try:
        cur = mysqlcon.cursor()
        sqlstr = "select mid,file,data,client,user from pm_mark_info"
        if ips != "":
            sqlstr += " where mark2train = 0 or mark2train IS NULL"

        # print(sqlstr)
        cur.execute(sqlstr)
        ret = cur.fetchall()
        hasDic={}
        for row in ret[:]:
            # print(row)
            mark_info ={}
            mark_info["mid"] = row[0]
            mark_info['file'] = row[1]#.replace("\n","")
            mark_info['data'] = row[2]#.replace("\n","")
            mark_info["client"] = row[3]
            mark_info["user"] = row[4]

            #if int(mark_info["mid"])<=0:
            #    continue
            skip=0
            iplist = ips.split(",")
            curip = ""
            for ip in iplist:
                if ip not in mark_info["file"]:
                    #if "192.168.2.103" not in mark_info["file"]:
                    skip+=1
                else:
                    curip = ip
                    print("OLD_IP",curip,mark_info["file"])
                    mark_info["file"] = mark_info["file"].replace(curip, storeip)
                    print(curip, "->", storeip)
                    break
            if skip==len(iplist):
                if storeip not in mark_info["file"]:
                    continue
                else:
                    print("STORE_IP",storeip,mark_info["file"])

            mark_info["ori_store_ip"] = curip


            MarkList.append(mark_info)
            # if (mark_info["data"] not in hasDic )and (mark_info["mid"]+mark_info["file"] not in hasDic):
            #     MarkList.append(mark_info)
            #     hasDic[mark_info["data"]] = 1
            #     hasDic[mark_info["mid"]+mark_info["file"]] = 1
        cur.close()
    finally:
        mysqlcon.close()
        return MarkList
    return [{"mid":10,"data":"123|23|45|443|234","file":"//pdf-svr/pm/PDF/2016Q2/Annount/f7b0a4ce4320251a3b3721ff07cb7850.pdf"}]

# 设置状态 1 = 已完成标注到训练数据的转换 0 = 未完成
def UpdateMarkInfo(mark_info, mark2train=1):
    mysqlcon = getMysqlConnection()
    up_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = "update pm_mark_info set mark2train={0},upt='{1}'".format(mark2train, up_time)
    # mysql Mode
    sqlstr += " where mid = '{0}' and data='{1}'".format(mark_info["mid"], mark_info["data"])
    # File Mode
    # sqlstr += " where task_file = '{0}'".format(FileName)
    try:
        cc = time.clock()

        cur = mysqlcon.cursor()
        # exp_start_time =datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()

        cc = time.clock() - cc
        print("UpdateMarkInfo:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()

def InsertTrainData(train_data):
    mysqlcon = getMysqlConnection()
    upt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sqlstr = "insert into pm_train_data(user,mid,file,data,size,md5,upt,ori_store_ip) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(
        train_data["user"],train_data["mid"],train_data["file"],train_data["data"],train_data["size"],train_data["md5"] ,upt,train_data["ori_store_ip"])
    try:
        cc = time.clock()
        cur = mysqlcon.cursor()
        print(sqlstr)
        cur.execute(sqlstr)
        cur.close()
        mysqlcon.commit()
        cc = time.clock() - cc
        print("InsertTrainDataInfo:", cc)
        return True
    except:
        print("error:", sqlstr)
        mysqlcon.rollback()
        return False
    finally:
        mysqlcon.close()