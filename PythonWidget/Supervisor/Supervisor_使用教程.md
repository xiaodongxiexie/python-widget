

<font color="green"><strong>supervisor是一个Linux/Unix系统上的进程监控工具，supervisor是一个Python开发的通用的进程管理程序，可以管理和监控Linux上面的进程，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启.</strong></font>

### 1、 pip3 install supervisor
	(尽量避免sudo-apt install(ubuntu)或yum install(centos),因为会使用内置的python2)

### 2、默认下载路径是到python3路径下的bin文件夹里
	（比如：/usr/local/python3/bin)

### 3、建立软连接：


	比如我的是：
	
		# 其中/usr/local/python3/bin 是第2步钟的下载路径
		ln -s /usr/local/python3/bin/echo_supervisord_conf /usr/bin/echo_supervisord_conf
		ln -s /usr/local/python3/bin/supervisord /usr/bin/supervisord
		ln -s /usr/local/python3/bin/supervisorctl /usr/bin/supervisorctl


### 4、建立配置文件
 <font color="red"><strong>切换到比如 /etc/supervisor 路径后 --></strong></font>


	1、 mkdir -m 775 -p /etc/supervisor
	2、 mkdir -m 775 /etc/supervisor/your-config-dir
	3、 echo_supercisord_conf > /etc/supervisor/supervisord.conf


###  5、在第4步创建的目录（your-config-dir)中创建配置文件

	比如 your-config.ini
	
	# 注意 其中的 your-app-name 名字要唯一，到时候启动时候要根据这个名字进行启动/关闭等操作的
	
	;------------------your-config.ini-------------------------------
	[program:your-app-name]
	command = python3 /root/work/your-code-dir/your-script.py   ; 在终端执行的命令操作
	autostart = true								   ; 在 supervisord 启动的时候也自动启动
	startsecs = 10									   ; 开始10秒内没有异常退出，就视为正常启动了
	autorestart = true								   ; 异常退出后自动重启
	startretries = 10								   ; 启动失败自动重试次数
	user = root										   ; 以哪个用户启动
	redirect_stderr = true							   ; 把 stderr 重定向到 stdout （默认为False)
	stdout_logfile_maxbytes = 150MB					   ; stdout 日志文件大小（默认为50M）
	stdout_logfile_backups = 20						   ; stdout 日志文件备份个数
	stdout_logfile = /root/work/log/slog.log  ; 日志放置路径，注意，指定目录必须要存在否则报错
	[supervisord]


### 6、添加配置文件到主配置文件
		按上述操作则
	
		打开 /etc/supervisor/supervisord.conf 文件
	
		定位到文件最后一行可以看到
	
			;[include]
			;files = /relative/dictory/*.ini
	
		删除这两行的分号（分号起始为注释），然后添加我们的配置文件，修改后如下：
	
			[include]
			files = /etc/supervisor/your-config-dir/*.ini  ; 如有多个配置文件则以空格隔开即可
			;files = /etc/supervisor/our-config-dir/*.ini /etc/supervisor/example.ini  
	
	`

### 7、启动|重启 | 关闭
启动 supervisor


	supervisord -c /etc/supervisor/supervisord.conf


关闭 supervisor


	supervisorctl shutdown

启动你的程序

	supervisorctl start your-app-name

重启你的程序

	supervisorctl restart your-app-name

关闭你的程序

	supervisorctl stop your-app-name

刷新配置文件  如果启动后修改了 ini 文件，可以通过 reload 命令来刷新

	supervisorctl reload

### 8、查看 supervisor 运行状态

	
	# 这俩方式都可以看
	1.  ps -efH | grep supervisor
	2.  ps aux | grep supervisord
	


参考链接: 
	1. [使用 supervisor 管理进程](http://liyangliang.me/posts/2015/06/using-supervisor/)
	2. [Supervisor 配置过程](https://www.cnblogs.com/alimac/p/5858234.html)
