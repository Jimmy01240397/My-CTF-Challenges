<?php

function proxy($service) {
    $requestUri = $_SERVER['REQUEST_URI'];
    $parsedUrl = parse_url($requestUri);

    $port = 80;
    if (isset($_GET['port'])) {
        $port = (int)$_GET['port'];
    } else if ($_COOKIE["port"]) {
        $port = (int)$_COOKIE['port'];
    }
    setcookie("service", $service);
    setcookie("port", $port);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    $filter = '!$%^&*()=+[]{}|;\'",<>?_-/#:.\\@';
    $fixeddomain = trim(trim($service, $filter).".cggc.chummy.tw:".$port, $filter);
    $fixeddomain = idn_to_ascii($fixeddomain);
    $fixeddomain = preg_replace('/[^0-9a-zA-Z-.:_]/', '', $fixeddomain);
    curl_setopt($ch, CURLOPT_URL, 'http://'.$fixeddomain.$parsedUrl['path'].'?'.$_SERVER['QUERY_STRING']);
    curl_exec($ch);
    curl_close($ch);
}

if (!isset($_GET['service']) && !isset($_COOKIE["service"])) {
    highlight_file(__FILE__);
} else if (isset($_GET['service'])) {
    proxy($_GET['service']);
} else {
    proxy($_COOKIE["service"]);
}

