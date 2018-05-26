# scrapy-redis
scrapy-redis distributedJobbole 分布式的结构抓取伯乐在线的数据

1，如果抓取网络数据想要最快，那么把代理ip和分布式（scrapy-redis）结合起来肯定是最快的

2，实现目标用scrapy-redis搭建抓取环境，+ bloomfilter去重，然后统一存储到一个mysql中

3，[scrapy-redis环境搭建](https://github.com/rmax/scrapy-redis)

3，[如果一下关于项目的截图不能查看请点击此链接进行查看](https://blog.csdn.net/han1558249222/article/details/80465383)

win机器抓取截图：

![image](https://github.com/nanmuyao/netbean/tree/master/spiderData/win.png)

mac机器抓取截图：

![image](https://github.com/nanmuyao/netbean/tree/master/spiderData/mac.png)

mysql数据库截图存储数据的时候把数据库中的content字段添加特别是指，win机器抓取的存储为win，mac机器抓取存储为mac：

![image](https://github.com/nanmuyao/netbean/tree/master/spiderData/mysql.png)

