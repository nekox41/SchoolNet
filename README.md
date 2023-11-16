<p align="center">
    <img style="border-radius:50%;" src="https://foruda.gitee.com/avatar/1699369775963451692/13673284_nekox41_1699369775.png!avatar128"/>
</p>

<div align="center">

# 校园网登录

**❤仅供参考❤**

<p align="center">
	<a href="https://space.bilibili.com/100455457">
		<img src="https://img.shields.io/badge/B%E7%AB%99-white?logo=bilibili">
	</a>
	<a href="https://qm.qq.com/cgi-bin/qm/qr?k=a1sMkSIXA_F2_6tDhuXdnD2u7ibinIcT&noverify=0">
		<img src="https://img.shields.io/badge/QQ-%23339999?logo=Tencent%20QQ">
	</a>
	<img src="https://img.shields.io/badge/%E5%BC%80%E5%8F%91%E8%BF%9B%E5%BA%A6-100%25-red">
</p>
</div>

# 声明

**这个仓库只是提供一些学习代码, 无任何违法违规行为.**

# 这是什么?

一个简单的校园网登录程序, 通过访问同目录下的 SQLite 文件(里面存放有爬下来的校园网账号密码)尝试登录, 如果账号已在线就切换下一个, 以此实现白嫖.

# 发展历程

之前有开过校园网, 有次暑假回家把学校办的卡丢了, 自己另半了一张卡. 回到学校就发现不让用了, 找运营处的人得到了"只有我们这里办卡才能用"的消息, 于是就只能自己想办法了.

期间发现了第一种办法, 校园网一般会开放这些端口:

|端口|端口介绍|
|---|---|
|53|dns 域名服务器|
|67|引导程序协议服务端|
|68|引导程序协议客户端

这种方法简单来说就是让流量走这些端口, 通过校园网的疏漏上网.
(不过我试了一下没成功.)

然后某天梦中仙人授法, 我就想到了这个**废物利用法**, 想办法找到学长们的账号密码, 检测没有人登录的去登.

对着校园网登录网页一番扒, 找到了几个接口:

1. [微软登录网络的重定向网页](http://www.msftconnecttest.com/redirect)  
2. [登录接口](http://10.254.0.42:8081/ibillingportal/LoginAction_login.do)  
3. [获取用户名](http://10.254.0.42:8081/ibillingportal/LoginAction_getFullUserName.do)  
4. [获取用户信息](http://10.254.0.42:8081/ibillingportal/PortalAction_getUserInfo.do)

校园网登录时需要当前分配的**IP地址**和**本机Mac**, 而微软的重定向网页跳转到校园网登录的时候会带上这两个参数.

获取用户信息的接口可以帮我查看这个学籍有没有账号, 账号剩余时间...

其实还有个踢人下线的接口 (