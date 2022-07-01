<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$regex='/^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}/';
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        if(preg_match_all($regex,trim($line)))
        	echo 'VALID'.PHP_EOL;
        else
        	echo 'INVALID'.PHP_EOL;
    }
echo $count;
fclose($_fp);
?>