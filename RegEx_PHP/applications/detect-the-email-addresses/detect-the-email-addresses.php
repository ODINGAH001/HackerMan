<?php
$_fp = fopen("php://stdin", "r");
$string = file_get_contents("php://stdin"); // Load text file contents

// don't need to preassign $matches, it's created dynamically

// this regex handles more email address formats like a+b@google.com.sg, and the i makes it case insensitive
$pattern = '/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}/';

// preg_match_all returns an associative array
preg_match_all($pattern, $string, $emails);

// the data you want is in $matches[0], dump it with var_export() to see it
//var_export($matches[0]);

$emails=array_unique($emails[0],SORT_STRING);
sort($emails,SORT_STRING);
for($i=0;$i<count($emails)-1;$i++)
    echo $emails[$i].';';
echo $emails[$i];
fclose($_fp);
?>