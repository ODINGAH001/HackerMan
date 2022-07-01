<?php
$_fp = fopen("php://stdin", "r");
$Regex_url='/href=["\']?([^"\'>]+)["\']?/';
$Regex_text='/>([^<]*)</';
$line=fgets($_fp);
    while (($line = fgets($_fp)) !== false) {
        preg_match_all($Regex_url,$line,$output_url);
        preg_match_all($Regex_text,$line,$output_text);
        if(isset($output_url[1][0]) && isset($output_text[1][1]))
        echo $output_url[1][0].','.$output_text[1][1].PHP_EOL;        
    }
fclose($_fp);
?>


error at test cases:-
1,2,3,5