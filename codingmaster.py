import sys
# n_iter = int(sys.stdin.readline())
Q = []
# ptr = 0
def push(value):
    Q.append(value)
    # prt += 1

def empty():
    if len(Q) == 0:
        print('1')
    else:
        print('0')

def pop():
    try:        
        print(Q.pop(0))        
    except:
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