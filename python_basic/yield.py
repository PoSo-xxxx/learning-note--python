#yield:
def different():
    for i in range(5):
        yield i
w=different()
print(next(w))                  #0
print(next(w))                  #1
print(next(w))                  #2
for i in different():
    print(i,end=' ')            #0 1 2 3 4
#yield:used for generator, yield will return the value without terminate the function.
#      This will keep the function stats until next time being called.

#still need more practice and further study