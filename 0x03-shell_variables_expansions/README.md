#!/bin/bash
#creates an alias named ls with value rm*
alias ls='rm*'
#print hello user, user is the current linux user
echo "hello $USER"
#add /action to the PATH. /action will the the last path shell looks into
alias PATH='pwd/action'
#counts the number of directories in the PATH
find . -type d -name PATH | wc -l
#lists environment variables

