<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        if(preg_match_all('/^hackerrank /',trim($line)))	//start
        	echo '1'.PHP_EOL;
        else if(preg_match_all('/ hackerrank$/',trim($line)))	//end
        	echo '2'.PHP_EOL;
        else if(preg_match_all('/^hackerrank$/',trim($line)))	//start and end
        	echo '0'.PHP_EOL;
        else
        	echo '-1'.PHP_EOL;
    }
fclose($_fp);
?>