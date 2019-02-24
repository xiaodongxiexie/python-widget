# coding: utf-8

"""
通过 python 脚本在cmd下启动别的py文件
"""

command = '''start cmd /k "{} cd {} & python {}"'''

root_drive         = "C:"
run_dir            = "C:/Users/pc/Desktop"
run_file_name      = "C:/Users/pc/Desktop/test_cmd.py"

if __name__ == "__main__":
    
    import os
    import time
    import datetime

    import redis 

    host     = "localhost"
    db       = 10
    port     = 6379
    key = "for_test"

    redi = redis.Redis(host=host, port=port, db=db)
    while True:
        flag = int(redi.get(key))
        if flag == 1:
            print('重启时间： ', str(datetime.datetime.now()))
            os.system(command.format(root_drive, run_dir, run_file_name))
            redi.set(key, 0)
        else:
            time.sleep(60)

