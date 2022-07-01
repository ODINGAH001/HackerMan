<?php
$string = file_get_contents("domains.txt"); // Load text file contents
// $pattern = '/(ht|f)tp(s?):\/{2}(www\.)?([a-z0-9]+\.)?([a-z0-9]+)?(\.[a-z]{2,4})([a-z0-9\/?&=‌​_()#-]*)/';
//$pattern = '/(?<=(ht|f)tp(s?)\:\/\/)[a-zA-Z0-9-.]*|(?<=http\:\/\/)[^w\W][a-zA-Z0-9-.]+/';
$pattern = '/((ht|f)tp(s)\:\/\/)[a-zA-Z0-9-.]*|(?<=http\:\/\/)[^w\W][a-zA-Z0-9-.]+/';
preg_match_all($pattern, $string, $domains);
//print_r($domains);
$domains=$domains[0];
for($i=0;$i<count($domains);$i++)
{
	//if (strpos($domains[$i], '://') === false &&strpos($domains[$i], 'www') != false)
    //$domains[$i] = 'http://' . $domains[$i];
	$token_url = parse_url($domains[$i]);
	if(isset($token_url['host']))
		$domains[$i] = $token_url['host'];
}
$domains=array_unique($domains,SORT_STRING);
sort($domains,SORT_STRING);
for($i=0;$i<count($domains)-1;$i++)
{
	if(isset($domains[$i]))
	{
	//if (strpos($domains[$i], '.') == true )
   	echo $domains[$i].';';
}
}
echo $domains[$i];
?>