<?php
$_fp = fopen("php://stdin", "r");
// Enter your code here. Read input from STDIN. Print output to STDOUT 
$n=(int)fgets($_fp);
$paragraph='';
$list_words=array();
while($n>0)
    {
    	$paragraph.=' '.fgets($_fp);
   		$n--;
	}
$list_words=preg_split('/[\s]+/', $paragraph, -1, PREG_SPLIT_NO_EMPTY);

$t=(int)fgets($_fp);
$i=0;
while($t>0)
{    
	$count=0;
	$word=trim(fgets($_fp));
    $regex='/\w+'.$word.'\w+/';
	for($i=0;$i<count($list_words);$i++)
	{	
	if(preg_match_all($regex, $list_words[$i]))
		$count++;
	}
	echo $count++.PHP_EOL;
    $t--;
}
fclose($_fp);
?>