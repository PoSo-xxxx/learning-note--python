#tuple
a = tuple(range(0,10));  b = (1, "hello", 1+5j, 2.0, [1,2,3])
print(a)                                                      #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b)                                                      #(1, 'hello', (1+5j), 2.0, [1, 2, 3])
print(a[0], a[2:6], a[-2])                                    #0 (2, 3, 4, 5) 8
print(a[2:]+b[:3])                                            #(2, 3, 4, 5, 6, 7, 8, 9, 1, 'hello', (1+5j))
print(len(a), min(a), max(a), sum(a))                         #10 0 9 45
print(sorted(a, reverse = True))                              #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(b.index("hello"), b.count("hello"))                     #2 1
#the member can be any kind of data type.
#[content]:declare a tuple; tuple(content):turn content into a tuple.
#tuple[-X]:search the Xth element from the right.
#len(tuple):counting the lenght of tuple.
#min(tuple):find the minimum element in the tuple(all element must be the same type).
#max(tuple):find the maximum element in the tuple(all element must be the same type).
#sum(tuple):return the sum of all element in the tuple(all element must be the numeric type).
#sorted(tuple, reverse = True/False(optional)):sort the tuple, the default will be ascending data,
#reverse = True: the data will be sorted in descending.(the output will become  a list).
#tuple.index(element):return the first place of the finding element, if element is not in the tuple will cause exception
#tuple.count(element):return the number of times that the finding element shows up
