<?php
//$_fp = fopen("php://stdin", "r");
$_fp = fopen("domains.txt", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        if(preg_match_all('/^hi [^dD]/i',trim($line)))	//start
        	echo trim($line).PHP_EOL;
    }
fclose($_fp);
?>