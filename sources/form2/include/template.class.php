<?php
/*
Classe provenant de http://wiki.jeuphp.net/tutoprog:template_en_php
*/

class template
{
    var $file;
    var $start=false;
    var $vars = array();
    function template($tpl) {
        $this->file = $tpl;
    }
    function start() {
        
        $this->start=ob_start();
    }
    function set($var, $val) {
        $this->vars[$var] = $val;
    }
    function display($contents = null) {
        extract($this->vars);
        if ($contents === null) {
            $contents = ob_get_contents();
            ob_end_clean();
        }
        include $this->file;
    }
    function get($contents = null) {
        extract($this->vars);
        if ($contents === null) {
        	if ($this->start){
            	$contents = ob_get_contents();
            	ob_end_clean();
        	}
        }
        ob_start();
        include $this->file;
        $return= ob_get_contents();
        ob_end_clean();
        return $return;
    }
}