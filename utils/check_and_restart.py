# -*- coding:UTF-8 -*-
"""
通过 python 脚本在cmd下启动别的py文件
"""

command            = '''start cmd /k "{} cd {} & {} {}"'''

# root_drive         = "C:"
# run_dir            = "C:/Users/pc/Desktop"
# run_file_name      = "C:/Users/pc/Desktop/test_cmd.py"

if __name__ == "__main__":
    
    import os
    import time
    import datetime
    import subprocess
    import configparser

    import redis 

    cf = configparser.ConfigParser()
    cf.read("config.cfg", encoding="utf-8")

    same_folder   = cf.get("local", "same_folder")
    if same_folder:
        exe_name   = cf.get("local", "exe_name")
        run_dir    = os.path.dirname(os.path.abspath(__file__))
        root_drive = run_dir.split(":")[0]+":"
        run_file_name = os.path.join(run_dir, exe_name) + ".exe"
    else:
        root_drive    = cf.get("local", "root_drive")
        run_dir       = cf.get("local", "run_dir")
        run_file_name = cf.get("local", "run_file_name")

    host = cf.get("local", "host")
    port = cf.getint("local", "port")
    db   = cf.getint("local", "db")
    key  = cf.get("local", "key")
    password = cf.get("local", "password")
    password = None if password.lower() == "none" else password
    sleep_time = cf.getint("local", "sleep_time")
    # host     = "localhost"
    # db       = 10
    # port     = 6379
    # password = None
    # key      = "for_test"

    redi = redis.Redis(host=host, port=port, db=db, password=password)
    
    while 1:
        if key not in redi:
            redi.set(key, 0)
        flag = int(redi.get(key))
        if flag == 1:
            print('重启时间： ', str(datetime.datetime.now()))
            sc = "python" if run_file_name.endswith(".py") else ""
            cmd_op = command.format(root_drive, run_dir, sc, run_file_name)
            try:
                os.system(cmd_op)
                redi.set(key, 0)
            except Exception as e:
                print('error...', e)
        else:
            #  检查是否需要重启
            time.sleep(sleep_time)

