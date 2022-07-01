<?php
$_fp = fopen("domains.txt", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$regex='/^[(][+-]?\d{2}\.?\d*, [+-]?\d{3}\.?\d*[)]$/';//myregex
$regex='/^[(][-+]?([1-8]?\d(\.\d+)?|90(\.0+)?), \s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)[)]$/';//stackoverflow
$line = fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        if(preg_match_all($regex,trim($line)))
            echo "VALID"."</br>".PHP_EOL;
            //print_r($output);
            //echo $output[0][0]."</br>";
        else
            echo "INVALID"."</br>".PHP_EOL;
    }
fclose($_fp);
?>