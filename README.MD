
# 常见WEB框架

## php
* soap: web service框架


## python
* django: 重量级WEB框架，约12万行。
* flask：轻量级WEB框架，仅6000行。

## ruby
* ruby-on-rails: 

## node.js
* node.js

---
# HTTPS配置
.keys：存放自签名证书
* 证书生成: source get_https_ca.sh

```
# gunicorn配置 https
gunicorn -w 4 -b0.0.0.0:8000 -certfile=server.pem -keyfile=server.key myapp:app

# nginx配置 https
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