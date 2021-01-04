#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:30:12 2021

@author: pi
"""

# =============================================================================
# Parallel coding using process (different instances are invoked no sharing of data)
# =============================================================================
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:54:29 2021

@author: pi
"""

from multiprocessing import Process
#import threading
import time

class sharing(object):

    def __init__(self):
        self.a = 0
        self.b = 0 
       
    def test_func1(self):

        while True:
            self.a = self.a + 1
            print ("value of a is",self.a)
            time.sleep(1)

    
    def test_func2(self):
        while True:
            if (self.a % 5 == 0):
                self.b+=1
                print ("value of b is",self.b)
#            time.sleep(10)
#            print(self.a % 5)
            time.sleep(1)
            

if __name__ == '__main__':
    x = sharing()
    p1 = Process(target=x.test_func1)
    p1.start()
    p2=Process(target=x.test_func2)
    p2.start()
    p1.join()
    p2.join()
#    p1=threading.Thread(target=x.test_func1)
#    p2=threading.Thread(target=x.test_func2)
#    p1.start()
#    p2.start()
#    p1.join()
#    p2.join()
    
# =============================================================================
# For definition outside of a class
# =============================================================================
#def loop_a():
#
#    while 1:
#
#        print("a")
#        time.sleep(1)
#
#def loop_b():
#
#    while 1:
#
#        print("b")
#        time.sleep()
#
#if __name__ == '__main__':
#
#    Process(target=loop_a).start()
#
#    Process(target=loop_b).start()