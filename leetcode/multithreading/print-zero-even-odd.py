https://leetcode.com/problems/print-zero-even-odd/

from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.semZero = Semaphore()
        self.semOne = Semaphore(0)
        self.semTwo = Semaphore(0)
        
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.semZero.acquire()
            printNumber(0)
            (self.semTwo if i % 2 else self.semOne).release()
            
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n+1, 2):
            self.semTwo.acquire()
            printNumber(i)
            self.semZero.release()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1, 2):
            self.semOne.acquire()
            printNumber(i)
            self.semZero.release()
        