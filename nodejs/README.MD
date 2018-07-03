
# 简介
 Node.js 应用是由哪几部分组成的：
 - 引入 required 模块：我们可以使用 require 指令来载入 Node.js 模块。
 - 创建服务器：服务器可以监听客户端的请求，类似于 Apache 、Nginx 等 HTTP 服务器。
 - 接收请求与响应请求 服务器很容易创建，客户端可以使用浏览器或终端发送 HTTP 请求，服务器接收请求后返回响应数据

# 运行
node server.js
Server running at http://127.0.0.1:8888/
* 验证1：http://127.0.0.1:8888/ （网页打开）
* 验证2：curl -I 'http://127.0.0.1:8888/'

# 程序简介
* http-server.js  支持 https协议，需要CA证书
* server.js 常规的http协议
* http-client.js 一个https劫持CA证书的例子
