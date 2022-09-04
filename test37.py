import imp
import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

from game.sound.echo import echo_test as e 
e()
# echo_test 를 e라고 쓰겠다.

from game.sound import *
echo.echo_test()
#  *이란 싹다 불러와라 (모듈이 여러개 있으면 다불러오는 것)



# 잘 쓰지는 않는다.