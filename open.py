from os import *
from os import system,remove
import os
from sys import *
from time import *
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
#############
system('clear')
print('''\033[1;36mOOOOOOOOOOOOkdlldkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkollxOOOOOOOOO
\033[1;36mOOOOOOOOOOd;\033[1;37m:dOOx:;\033[1;36mxOOOOOdl::\033[1;37mcclllllcc::\033[1;36mlxOOOOk::\033[1;37mx0Ol,\033[1;36mdOOOOOOO
\033[1;36mOOOOOOOOOl,\033[1;37mKMMMMMM0,cc:cldOXWMMMMMMMMMWXOdlc:c,OMMMMMK,\033[1;36mcOOOOOO
\033[1;36mOOOOOOOOO.\033[1;37m0MMMMMMNold0WMMMMMMMMMMMMMMMMMMMMMXxkMMMMMMMx.\033[1;36mOOOOOO
\033[1;36mOOOOOOOOO'\033[1;37mkMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOk'\033[1;36mlOOOOOO
\033[1;36mOOOOOOOOOd'\033[1;37mxkWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOoo\033[1;36mkOOOOO
\033[1;36mOOOOOOOOkl\033[1;37mkWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdl\033[1;36mOOOO
\033[1;36mOOOOOOOll\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKo\033[1;36moOO
\033[1;36mOOOOOk:\033[1;37mkMMMMMMMMMMMMMMKKMMMMMMMMMMMMMMMMMMMMXoxWMMMMMMMMMMM\033[1;36mOlk
\033[1;36mOOOOk:\033[1;37mKMMMMMMMMMMMMMMd .NMMMKO000000000O0NMMd  0MMMMMMMMMMMM\033[1;36mNc
\033[1;36mOOOk;\033[1;37mKMMMMMMMMMMMMMMMXoOW0kOKWNOoc::coOWXOOONKKMMMMMMMMMMMMMM\033[1;36mX
\033[1;36mOOOl\033[1;37mKMMMMMMMMMMMMMMMMMMOkXMMMK.        'NMMNkxNMMMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mKMMMMMMMMMMMMMMMMMWd0MMMMMN:.      .oMMMMMNoKMMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMWlKMMMMMMMMWKOkkOKWMMMMMMMWoXMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMk0MMMMMMMMMMMMMMMMMMMMMMMMMNdMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXK00XNMMMMMMMMMMMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMWMMMMMMMMMMMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNNWNNNNNWMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMWWMMMMMM
\033[1;36mOOO\033[1;37mXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM''')

print (W + '[' + C + '1' + W + ']' + C + '==' + W + '{' + C + 'Android' + W + '}')
print (W + '[' + C + '2' + W + ']' + C + '==' + W + '{' + C + 'iPhone' + W + '}')
print (W + '[' + C + '0' + W + ']' + C + '==' + W + '{' + C + 'exit' + W + '}')
broid=str(input(W +"              ◎~"+ C +"Enter Number"+ W +"⇒ "+ G))


if broid == "1":
  system('bash Android.sh')

if broid == "2":
  system('bash iPhone.sh')

if broid == "0":
  system('bash exit.sh')
exit()
