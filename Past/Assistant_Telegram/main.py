import os
import threading
def one():
    os.system('python Sung_Jinwoo.py')
def two():
    os.system('python Cha_Hae-In.py')
one = threading.Thread(target=one,)
one.start()
two = threading.Thread(target=two,)
two.start()

