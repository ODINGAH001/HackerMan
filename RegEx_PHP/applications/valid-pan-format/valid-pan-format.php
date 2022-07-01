<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$regex='/^[A-Z]{5}\d{4}[A-Z]$/';
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        if(preg_match_all($regex,trim($line)))
        	echo 'YES'.PHP_EOL;
        else
        	echo 'NO'.PHP_EOL;
    }
fclose($_fp);
?>