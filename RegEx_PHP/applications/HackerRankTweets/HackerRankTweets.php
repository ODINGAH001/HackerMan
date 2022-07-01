<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$regex='/hackerrank/i';
$count=0;
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        if(preg_match_all($regex,trim($line)))
        {
        	echo $line.'</br>';
            $count++;
        }
    }
echo $count;
fclose($_fp);
?>