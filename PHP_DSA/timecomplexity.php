<?php

// O(1) - Constant time example -> Always return the first element, no matter the size of the array
function getFirstElement($arr)
{
    return $arr[0];
}

$arr = [10, 20, 30, 40, 50];
echo getFirstElement($arr) . "\n";


// O(n) - Linear time example - Execution time grows in proportion to the input
function printAllElements($arr1)
{
    foreach($arr1 as $element) {
        echo $element . " ";
    }
}

$arr1 = [10, 20, 30, 40, 50];
printAllElements($arr1) . "\n";


// O(log n) - Binary search example
function binarySearch($arr2, $target)
{
    $start = 0;
    $end = count($arr2) - 1;

    while($start <= $end) {
        $mid = (int)(($start + $end) / 2);

        if ($arr2[$mid] === $target) {
            return "Found: $arr2[$mid]";
        } elseif ($arr2[$mid] < $target) {
            $start = $mid + 1;
        } else {
            $end = $mid - 1;
        }
    }
    return "Not Found";
}

$arr2 = [10, 20, 30, 40, 50, 60];
echo binarySearch($arr2, 30) . "\n";