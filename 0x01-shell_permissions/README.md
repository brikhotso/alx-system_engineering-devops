#!/bin/bash
su - super user
id -un -prints outs effective user name
group -prints out group a user is part of
sudo chown betty hello - changes the file owner to betty
touch  hello - creates a new empty file named "hello"
chmod u+x hello - adds(+) execute(x) permission to owner(u) of file "hello"
chmod u+x,g+x,o+r hello -adds execute(x) permission to user(u),execute permission(x) to group(g) ,read(r) permission to others(o)
chmod ugo+x -adds execute permission to owner,group and others
chmod 007 hello- gives all permissions only to others
chmod 753 hello -gives a file named  "hello" to following permissions -xrwr-x-rw
chmod --reference=olleh hello -sets the mode of the file "hello" the same as "olleh"
chmod -R ugo-X . -gives owner,group and others execute permission in all the subdirectories in the current directory
mkdir -m 751 my_dir - create a new directory *my_dir* with 751 permissions (m stands for mode works like a change mode (chmod) command inside onother command)
chgrp school hello - change group of file "hello" to school

