<?php
require_once("config.php");
require_once("include/template.class.php");
function _s($str) {
    
}
$base=sprintf('./theme/%s/',$theme);

//Load locale data
$langs=array();
foreach(glob($base.'locale/*.php') as $filename)
     array_push($langs,$filename);
     
$lang = substr($_SERVER['HTTP_ACCEPT_LANGUAGE'], 0, 2);
if (!in_array($lang,$langs)
    $lang='en';
$json_i18n=file_get_contents($base.'locale/'.$lang.'.php');
$json_i18n=json_decode($json_i18n);


$tpl = new template($base.'index.php');
$tpl->set('base', sprintf('/theme/%s/',$theme));
$tpl->set('i',$json_i18n);
$tpl->display();
