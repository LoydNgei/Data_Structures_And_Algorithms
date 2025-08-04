<?php
// What is a linear search? From the word line, we need to go one by one through the list until we find our desired target

$users = ['Alex', 'Brian', 'Carolyne', 'David', 'James', 'Jane'];

function findUser($users, $targetUser)
{
    foreach ($users as $user) {
        if ($user == $targetUser) {
            return "$targetUser found!";
        }
    }
    return "$targetUser not found!";
}

echo (findUser($users, 'James'));




