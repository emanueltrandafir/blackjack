mode 95,36

title Blackjack Night

set /a color1=C
set /a color2=%random% %% 16
set HEX=0123456789ABCDEF
call set hexcolors=%%HEX:~%color1%,1%%%%HEX:~%color2%,1%%
color %hexcolors%


python ./Main.py

pause
 