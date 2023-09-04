#!/bin/bash
echo Hello, World - Prints “Hello, World”, followed by a new line to the standard output
find . -name "*.js" -type f –delete - deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders
find . -mindepth 1 -type d | wc –l - ls -t1 | head -counts the number of directories and sub-directories in the current directory.
sort | uniq –u -takes a list of words as input and prints only words that appear exactly once
cat /etc/passwd | grep "root" - Display the first 10 lines of /etc/passwd
grep -c -i "bin" /etc/passwd - displays the third line of the file iacta
grep -i "root" -A 3 /etc/passwd -Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
grep -i -v "bin" /ect/passwd -Display all the lines in the file /etc/passwd that do not contain the pattern “bin”
grep '^[[:alpha:]]' /etc/ssh/sshd_config -Display all lines of the file /etc/ssh/sshd_config starting with a letter
tr 'Ac' 'Ze' -Replace all characters A and c from input to Z and e respectively
echo "\"(Ôo)'" - displays a confused smiley "(Ôo)'.
tr -d 'cC'- removes all letters c and C from input
rev  - reverse its input
cut -d ':' -f1,6 /etc/passwd | sort - displays all users and their home directories, sorted by users in /etc/passwd
cat /etc/passwd - Display the content of the /etc/passwd file
cat /etc/passwd /etc/hosts - Display the content of /etc/passwd and /etc/hosts
tail -n 10 /etc/passwd -Display the last 10 lines of /etc/passwd
head -n 10 /etc/passwd -
head -n 3 iacta | tail -n 1
echo 'Best School' >> "\\*\\\\'\"Best School\"\\'\\\\*$\\?\\*\\*\\*\\*\\*:)" -creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line
ls -la > ls_cwd_content -writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
tail -n 1 iacta >> iacta -duplicates the last line of the file iacta
