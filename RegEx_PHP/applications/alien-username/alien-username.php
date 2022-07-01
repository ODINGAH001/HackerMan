<?php
$_fp = fopen("php://stdin", "r");
$Regex_url='/^[_|\.][0-9]+[a-zA-Z]*_?$/';
$line=fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        preg_match_all($Regex_url,$line,$output_url);
        if(isset($output_url[0][0]))
            echo 'VALID'.PHP_EOL;
        else
            echo 'INVALID'.PHP_EOL;
    }
fclose($_fp);
?>