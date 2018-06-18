<?php
/*
@desc: Web Services 可以将应用程序转换为网络应用程序，可以被其它程序调用。
基本的Web Services平台是 XML+HTTP。
调用方式：NO-WSDL 与 WSDL。NO-WSDL使用参数来传递信息；WSDL将WSDL文件名作为参数。
@author: keefe
@date: 2018/6/17
@exaple: 使用PHP的SOAP扩展来创建Web Service，首先确保php soap扩展已装，可用phpinfo()查看。
*/

Class SiteInfo
{  // SiteInfo 类用于处理请求
    /**
     *    返回网站名称
     *    @return string
     */
    public function getName() {
        return "getname";
    }
    public function getUrl() {
        return "www.wuqifu.cn";
    }
}

// 创建 SoapServer 对象
$s = new SoapServer(null,array("location"=>"/php/soap/server.php","uri"=>"server.php"));

// 导出 SiteInfo 类中的全部函数
$s->setClass("SiteInfo");
// 处理一个SOAP请求，调用必要的功能，并发送回一个响应。
$s->handle();
?>
