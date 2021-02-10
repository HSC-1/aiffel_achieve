import sys
<<<<<<< HEAD
# n_iter = int(sys.stdin.readline())
=======

n_iter = int(sys.stdin.readline())
>>>>>>> 66736403a91f27c7d94af1e5b9b3137c47e9a1bc
Q = []
# ptr = 0
def push(value):
    Q.append(value)
    # prt += 1

def empty():
    if len(Q) == 0:
<<<<<<< HEAD
        print('1')
=======
        print('-1')
>>>>>>> 66736403a91f27c7d94af1e5b9b3137c47e9a1bc
    else:
        print('0')

def pop():
<<<<<<< HEAD
    try:        
        print(Q.pop(0))        
    except:
=======
    if len(Q) != 0:
        Q.pop(0)
        print(Q.pop(0))
        
    else:
>>>>>>> 66736403a91f27c7d94af1e5b9b3137c47e9a1bc
        print("-1")

def size():
    return len(Q)

def front():
    try: 
        print(Q[0])
    except:
        print('-1')

def back():
    try:
        print(Q[-1])
    except:
        print('-1')

<<<<<<< HEAD
# for _ in range(n_iter):
#     a = sys.stdin.readline().split()
#     if a[0] == 'push':
#         push(a[1])
#     elif a[0] == 'pop':
#         pop()
#     elif a[0] == 'empty':
#         empty()
#     elif a[0] == 'size':
#         print(size())
#     elif a[0] == 'front':
#         front()
#     elif a[0] == 'back':
#         back()

Q = []
push(14)
print(Q)
pop()
pop()
empty()
push(100)
push(10)
print(size())
print(Q)
=======
for _ in range(n_iter):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        push(a[1])
    elif a[0] == 'pop':
        pop()
    elif a[0] == 'empty':
        empty()
    elif a[0] == 'size':
        print(size())
    elif a[0] == 'front':
        front()
    elif a[0] == 'back':
        back()



# def is_full(self) -> bool:
#     return self.ptr >= self.capacity

# def pop(self):
#     if self.is_empty():
#         raise FixedStack.Full
#     self.ptr -= 1
#     return self.stk[self.ptr]
>>>>>>> 66736403a91f27c7d94af1e5b9b3137c47e9a1bc
