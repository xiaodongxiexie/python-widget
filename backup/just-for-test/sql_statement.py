create_table_sql =  '''
                    create table if not exists obj_infos(
                    house_id int not null,
                    dx int not null,
                    dy int not null,
                    oc varchar(255) not null,
                    ot varchar(255) not null,
                    x int not null,
                    y int not null
                    )
                    '''

create_table_sql2 = '''
                    create table if not exists house_infos(
                    house_id int not null primary key,
                    file_name varchar(255) not null)
                    '''
#给表新增列
sql = '''
        alter table house_infos
        add column area varchar(255)
        not null default '卧室'
'''

#增加表列，指定格式
sql = '''
        alter table table_name
        add sex boolean
'''

#将指定列移到第一列
sql = '''
        alter table table_name
        modify col_name varchar(255) first
'''

#将指定列移动到某一列后面
sql = '''
        alter table table_name
        modify col_name varchar(255) after col_name2
'''

#与另一表关联进行插入数据
sql = '''
        update house_infos h, obj_infos o
        set h.area = o.oc
        where o.ot='区域' and h.room_id=o.room_id
'''

#更改表名
sql = '''
        alter table table_name rename table_name2
'''

#表去重
sql = '''
        select distinct(*) from table_name
'''

#改变表中列名（必须同时指定格式）
sql = '''
        alter table table_name
        change col1 col2 varchar(255)
'''


#将表2中的数据插入到表1中
sql = '''
        insert into table_name
        select * from table_name2
'''

#删除指定表中的主键
sql = '''
        alter table table_name
        drop primary key
'''

sql = '''
        alter table table_name
        add primary key(col_name)
'''

#删除表中指定列
sql = '''
        alter table table_name
        drop col_name
'''

#删除表中指定行
sql = '''
        delete from table_name where col_name=value
'''
