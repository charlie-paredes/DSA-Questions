class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    #when we enqueue, we append a value to stack 1
    def enqueue(self, value):
        self.stack1.append(value)

    #when we dequeue, if stack 2 is not empty, we pop
    #it's top value from it and return it. 
    #if stack 2 is empty, we loop through stack 1 and pop its values, appending 
    #the values into stack 2.
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

    def is_empty(self):
	    return not self.stack1 and not self.stack2

    # if 1, 2, 3 are appended into stack 1, they stack on has from top to bottom 3, 2, 1
    #if we pop each one and append them to stack 2,
    #stack 2 has from top to bottom 1, 2, 3, so popping its values will give the original
    #first in, first out order of the elements passed in

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # prints 10
print(q.dequeue())  # prints 20
q.enqueue(40)
print(q.dequeue())  # prints 30
print(q.dequeue())  # prints 40
print(q.is_empty())  # prints True

