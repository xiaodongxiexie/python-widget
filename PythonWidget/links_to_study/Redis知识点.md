#### 1、什么是`Redis`?

`Redis`是一个基于内存的高性能`key-value`数据库。

#### 2、`Redis`的特点

`Redis`本质上是一个`Key-Value`类型的数据库， 很像`Memcached`，整个数据库通通加载在内存当中进行操作，

定期通过异步操作把数据库数据`flush`到硬盘上进行保存。

因为是纯内存操作，`Redis`的性能非常出色，每秒可以处理超过10万次读写操作，是已知性能最快的`Key-Value`数据库。

`Redis`的出色之处不仅仅是性能，`Redis`最大的魅力在于支持保存多种数据结构，此外单个`value`的最大限制是1`GB`，不像`Memcached`只能保存1`MB`的数据，因此`Redis`可以用来实现很多有用的功能。

例如可以用`Redis`的`List`来做`FIFO`双向链表，实现一个轻量级的高性能消息队列服务，用`Redis`的`Set`可以做高性能的`tag`系统等等。另外`Redis`也可以对存入的`Key-Value`设置`Expire`时间，因此也可以被当做一个功能加强版的`Memcached`来用。

`Redis`的主要缺点是数据库容量受到物理内存的限制，不能用作海量数据的高性能读写，因此`Redis`适合的场景主要局限在较小数据量的高性能操作和运算上。

#### 3、使用`Redis`有哪些好处？

- 速度快

  ```
  因为数据存在内存中，类似于`HashMap`， `HashMap`的优势就是查找和操作的时间复杂度都是`O(1)`
  ```

- 支持丰富的数据类型

  ```
  支持`String`、`List`、`Set`、`Sorted Set`、`Hash`
  ```

- 支持事务

  ```
  原子性、一致性、隔离性、持久性
  ```

- 丰富的特性

  ```
  可用于缓存、消息，按`key`设置过期时间，过期后将会自动删除
  ```

#### 4、`Redis`相比`Memcached`有哪些优势？

- `Memcached`所有的值都是简单的`string`类型，`Redis`支持更为丰富的数据类型
- `Redis`的速度比`Memcached`快很多
- `Redis`支持持久化其数据

#### 5、`Redis`和`Memcached`的区别有哪些？

- 存储方式

  ```
  `Memcached`把数据全部存在内存中，断电后会丢失所有数据，数据不能超过内存大小
  `Redis`将部分数据存在硬盘中，可以保证数据的持久性。
  ```

- 数据支持类型

  ```
  `Memcached`对数据类型支持相对简单，
  `Redis`支持丰富的数据类型。
  ```

- 使用不同的底层模型

  ```
  底层实现方式不同，以及与客户端之间通信的应用协议不同。
  `Redis`直接构建了`VM`机制，因为一般的系统调用系统函数的话，会浪费一定的时间去移动和请求。
  ```

#### 6、`Redis`常见性能问题

- `Master`写内存快照，`save`命令调度`rdbSave`函数，会阻塞主线程的工作，当快照比较大时对性能影响较大，会间断性暂停服务。
- `Master  AOF`持久化， `AOF`文件过大会影响`Master`重启的恢复速度。
- `Master`调用`BGREWRITEAOF`重写`AOF`文件时会占用大量的`CPU`和内存资源，导致服务`Load`过高，出现短暂服务暂停现象。
- `Redis`主从复制的性能问题，为了主从复制的速度和连接的稳定性，`Slave`和`Master`最好在同一个局域网内。

#### 7、`Redis`数据淘汰策略

- `volatile-lru`

  ```
  从已设置过期时间的数据集中挑选最近最少使用的数据淘汰
  ```

- `volatile-ttl`

  ```
  从已设置过期时间的数据集中挑选将要过期的数据淘汰
  ```

- `volatile-random`

  ```
  从已设置过期时间的数据集中任意选择数据淘汰
  ```

- `allkeys-lru`

  ```
  从数据集中挑选最近最少使用的数据淘汰
  ```

- `allkeys-random`

  ```
  从数据集中任意选择数据淘汰
  ```

- `no-enviction`

  ```
  禁止驱逐数据
  ```

#### 8、`Redis`适合场景

- 会话缓存`Session Cache`
- 全页缓存`FPC`
- 队列
- 排行榜/计数器
- 发布/订阅

#### 9、`Redis`集群

- `Redis`主从复制模型

  ```
  为了使在部分节点失败或大部分节点无法通信的情况下集群仍然可用，所以集群使用了主从复制模型，每个节点都会有`N-1`个副本。
  ```

- `Redis`集群的复制

  ```
  异步复制。
  ```

- `Redis`集群会议欧写操作丢失吗？

```
`Redis`并不能保证数据的强一致性，这意味着在实际中集群在特定的条件下可能会丢失写操作。
```

- `Redis`集群最大节点个数

  ```
  2^14=2**14=16384个
  ```

- `Redis`哈希槽

  ```
  `Redis`集群没有使用一致性在`Hash`，而是引入了哈希槽的概念，`Redis`有16384个哈希槽，每个`Key`通过`CRC16`校验后对16384取模来决定防止哪个槽，集群的每个节点负责一部分`Hash`槽。
  ```

  

- `Redis`集群如何选择数据库

  ```
  `Redis`集群目前无法做数据库选择，默认在0数据库
  ```

