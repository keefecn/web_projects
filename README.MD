

# 常见WEB框架

##  WEB常用框架列表

| 开发语言   | 框架名称    | 简介                                                         | 优点                               | 缺点            |
| ---------- | ----------- | ------------------------------------------------------------ | ---------------------------------- | --------------- |
| PHP        | yii         | 一个基于组件、用于开发大型 Web 应用的高性能 PHP 框架，是一个 MVC 的框架。Yii是创始人薛强的心血结晶，于2008年1月1日开始开发。 | 优异的性能，丰富的功能和清晰的文档 |                 |
| PHP        | symfony     | 一个基于MVC模式的面向对象的PHP5框架。Symfony允许在一个web应用中分离事务控制，服务逻辑和表示层。 |                                    |                 |
| PHP        | codeigniter | 一套给PHP网站开发者使用的应用程序开发框架和工具包。在最小化，最轻量级的开发包中得到最大的执行效率、功能和灵活性。   CodeIgniter是由Ellislab公司的CEO RickEllis开发的。 | 动态实例化。松耦合。组件专一性。   |                 |
| Javascript | nodejs      | Node.js是建立在谷歌Chrome的JavaScript引擎(V8引擎)的Web应用程序框架。 | 数据密集型。                       | CPU密集型慎用。 |
| JavaScript | express     | Express是一个最小的，灵活的Node.js Web应用程序框架，它提供了一套强大的功能来开发Web和移动应用程序。 它有助于基于Node Web应用程序的快速开发。 |                                    |                 |
| JavaScript | JXcore      | 引入了包装和源文件和其他资源加密成JX包一个独特的功能。       |                                    |                 |
| Ruby       | rails       | Rails 是使用 Ruby 语言编写的网页程序开发框架，目的是为开发者提供常用组件，简化网页程序的开发。只需编写较少的代码，就能实现其他编程语言或框架难以企及的功能。 |                                    |                 |
| Ruby       | jekyll      | 一个支持markdown和liquid模板语言的静态站点生成器，作为github项目的标配页面。 | 很适合作BLOG。                     |                 |
| Java       | grails      | 基于Groovy编程语言，并构建于Spring、Hibernate等开源框架之上，是一个高生产力一站式框架。 | 插件系统                           |                 |
| Java       | scooter     |                                                              |                                    |                 |
| Java       | jsp/servlet |                                                              |                                    |                 |
| Java       | SSH         | (spring/structs/hibernate)                                   |                                    |                 |
| Java       | struts      |                                                              |                                    |                 |
| Java       | Spring MVC  |                                                              |                                    |                 |
| perl       | catalyst    | 一个用 Perl 语言开发的 MVC 框架。                            |                                    |                 |
| scala      | lift        | 一个非常优雅的web框架，基于Scala编程语言，使用Apache 2.0 license许可发布。 | 可伸缩应用服务器                   |                 |
| scala      | scalatra    |                                                              |                                    |                 |

**说明**：当前有许多框架可用，敏捷开发中有时并不需自己设计框架，利用已知框架或者在编程过程重构代码中产生框架。这听起来有些荒谬，事实上这正是大多数公司在开发中所采用的模式。



## PHP

* soap: web service框架



## python

* django: 重量级WEB框架，约12万行。
* flask：轻量级WEB框架，仅6000行。
* tornado: 单线程异步，性能较好。



## Ruby

* Ruby-on-rails: 



## node.js

* node.js



## vue



---
# HTTPS配置
.keys：存放自签名证书
* 证书生成: `source get_https_ca.sh`

**gunicorn配置 https**

```shell
gunicorn -w 4 -b0.0.0.0:8000 -certfile=server.pem -keyfile=server.key myapp:app
```



**nginx配置 https**

```nginx
server_names barretlee.com *.barretlee.com
ssl on;
ssl_certificate /etc/nginx/ssl/barretlee.com.crt;
ssl_certificate_key /etc/nginx/ssl/barretlee.com.key;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS !MEDIUM";
# Add perfect forward secrecy
ssl_prefer_server_ciphers on;
add_header Strict-Transport-Security "max-age=31536000; includeSubdomains";
```
