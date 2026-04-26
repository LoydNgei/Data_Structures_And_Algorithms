<?php

// array_push - Adding Elements to an Array
$fruits = ['Apple', 'Banana'];
array_push($fruits, 'cherry', 'Orange');
print_r($fruits);

// array_pop - Removing the last elements

$fruits = ['Apple', 'Banana', 'Cherry'];
array_pop($fruits);
print_r($fruits);

// array_merge - Merging 2 arrays
$array1 = [1,2,3];
$array2 = [4,5,6];
$merged = array_merge($array1, $array2);

// array_search - Searching for an element
$fruits = ['Apple', 'Banana', 'Cherry'];
$index = array_search('Banana', $fruits);
echo $index;

// sort and rsort - sorting Arrays
$numbers = [4,1,6,9,3];
sort($numbers);
print_r($numbers);

rsort($numbers);
print_r($numbers);