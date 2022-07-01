<?php
$html=file_get_contents("php://stdin");
$dom = new DOMDocument();
$dom->loadHTML($html);
$nodes=array();
$i=0;
foreach($dom->getElementsByTagName('*') as $element ){
if(strcmp($element->nodeName,"html")!=0 && strcmp($element->nodeName,"body")!=0)
    $nodes[$i]=$element->nodeName;
    $i++;
}
$nodes=array_unique($nodes,SORT_STRING);
sort($nodes,SORT_STRING);
for($i=0;$i<count($nodes)-1;$i++)
    echo $nodes[$i].';';
echo $nodes[$i];
?>