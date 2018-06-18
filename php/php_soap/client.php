<?php
/*
@desc:
@author: keefe
@date: 2018/6/17
@example: 
call:  http://localhost/php_soap/client.php
result: 
getname
www.wuqifu.cn
*/

try {
    // non-wsdl方式调用web service
    // 创建SoapClient对象, SoapClient对象的location需全路径
    $soap = new SoapClient(null,array('location'=>"http://localhost/php/php_soap/server.php",'uri'=>'server.php'));
    // 调用函数
    $result1 = $soap->getName();
    $result2 = $soap->__soapCall("getUrl",array());
    echo $result1."<br/>";
    echo $result2;
} catch(SoapFault $e) {
    echo $e->getMessage();
} catch(Exception $e) {
    echo $e->getMessage();
}
