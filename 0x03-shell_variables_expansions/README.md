#!/bin/bash
==> 0-alias <==
#Creates an alias
alias ls="rm *"
==> 100-decimal_to_hexadecimal <==
#Converts a number from base 10 to base 16
printf %x'\n' $DECIMAL
==> 101-rot13 <==
#Encodes and decodes text using the rot13 encryption. Assume ASCII
tr 'A-Za-z' 'N-ZA-Mn-za-m'
==> 102-odd <==
#Prints every other line from the input, starting with the first line
cat -n | cut -b 6- | grep ^[13579] | cut -f2
==> 103-water_and_stir <==
#Adds the two numbers stored in the environment variables WATER and STIR and prints the result
echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol')
==> 10-love_exponent_breath <==
#Write a script that displays the result of BREATH to the power LOVE
echo $((BREATH**LOVE))
==> 11-binary_to_decimal <==
#Converts a number from base 2 to base 10.
echo "$((2#$BINARY))"
==> 12-combinations <==
#Prints all possible combinations of two letters, except oo
printf %s'\n' {a..z}{a..z} | grep -v "oo"
==> 13-print_float <==
#Prints a number with two decimal places, followed by a new line
printf %0.2f'\n' $NUM
==> 1-hello_you <==
#Prints hello user, where user is the current Linux use
==> 2-path <==
#Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
PATH=$PATH:/action
==> 3-paths <==
#Counts the number of directories in the PATH.
echo $PATH | tr -s ':' '\n' | wc -l
==> 4-global_variables <==
#Lists environment variables
printenv
==> 5-local_variables <==
#Lists all local variables and environment variables, and functions.
set
==> 6-create_local_variable <==
#Creates a new local variable
BEST="School"
==> 7-create_global_variable <==
#Creates a new global variable
export BEST="School"
==> 8-true_knowledge <==
#Prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
echo $((TRUEKNOWLEDGE+128))
==> 9-divide_and_rule <==
#Prints the result of POWER divided by DIVIDE, followed by a new line.
echo $((POWER/DIVIDE))
