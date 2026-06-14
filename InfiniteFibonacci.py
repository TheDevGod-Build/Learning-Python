import sys

class FibonacciIterator:
    def __init__(self):
        self.index = -1
        self.current = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == 0:
            return 0
        self.current, self.next = self.next, self.current + self.next
        return self.current

if __name__ == "__main__":
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)

    fib = FibonacciIterator()
    while True:
        print(next(fib))
        