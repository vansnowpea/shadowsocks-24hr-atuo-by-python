# shadowsocks-24hr-atuo-by-python
shadowsocks 24hr atuo by python, rely on good source of ss


1、首先，[请参考我的上一个帖子](https://vansnowpea.github.io/2016/10/22/%E5%A6%82%E4%BD%95%E4%BC%98%E9%9B%85%E7%9A%84%E5%BB%BA%E7%AB%8B%E8%87%AA%E5%B7%B1%E7%9A%84SS5%E5%AE%9E%E7%8E%B0%E8%BD%BB%E6%9D%BE%E5%BF%AB%E9%80%9F%E7%BF%BB%E5%A2%99/)，实现了Win下的SS【快速】翻墙，如果没有SS，要翻墙都要忍受蜗牛速度。为SS的原版牛逼作者十万个赞，也要为翻版作者以及iss网站一万个赞。但是有个小问题，因为源头的SS账号每隔6小时变更，因此总是需要人工更新密码，那么如何把他做成自动更新？

2、方案，爬虫捕捉新密码+重写json加载。

3、细节分析：

用lxml代替了bs4，数据部分也变更修改，可能原作者写的时候网站数据模式和如今的不同，另增加了一些函数。

如下图，因为iss变更的是密码，因此爬虫也抓密码就好，比较简单


![](http://ocg7i7pt6.bkt.clouddn.com//blog/20161023/230709584.png)

4、代码,略


5、测试结果：
   通过5分钟一次取密码，重点观察iss站在更换密码的时候，有以下特点：

- 比如18点换密码，老密码回马上失效，但新密码不是马上更新到网站，导致有一段时间的真空期
- 同时，这段时间，读取的密码出现了波动，不过总体影响不算太大。

![](http://ocg7i7pt6.bkt.clouddn.com//blog/20161024/190737721.png)

6、SS 资源站点列表：

- [http://www.ishadowsocks.org/](http://www.ishadowsocks.org/)
- [http://freevpnss.cc/](http://freevpnss.cc/)

7、参考资料：

- [用python实现shadowsocks密码自动更新](http://www.gaococ.com/2016/03/06/%E7%94%A8python%E5%AE%9E%E7%8E%B0shadowsocks%E5%AF%86%E7%A0%81%E8%87%AA%E5%8A%A8%E6%9B%B4%E6%96%B0/)
- [python3 cookbook](http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html)
- [JSON概述以及PYTHON对JSON的相关操作](http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html)

8、安卓手机测试了类似方案，也是通过的，其实更简单，都不需要设置浏览器。

9、特别感谢

LittleCoder 帮忙修正了bug，美化了代码。
