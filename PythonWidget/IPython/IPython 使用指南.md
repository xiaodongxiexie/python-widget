### Spyder（IPython）使用指南

### 1.` %bookmark `书签的使用

#### 1.1 使用`name`作为`abs_path`的书签名，可通过`cd name`切换到	`abs_path`

`%bookmark name abs_path`



#### 1.2 列出所有书签

`%bookmark -l`



#### 1.3 删除指定书签

`%bookmark -d name`



### 2.`%dhist`

列出所有用过的目录

通过`_dh`以列表的形式返回所有用过的目录



### 3.`%whos`

返回所有用过的全局变量及`type`以及描述



### 4. `%who_ls`

以列表的形式返回所有全局变量（字符串格式）



### 5. `%rep`

`%rep` `rep`默认提取`_`变量的值



### 6. `%env`

显示系统环境变量


### 7. `%load_ext` 
查看指定变量内存占用
`%load_ext memory_profiler`
`%memit your-var`





