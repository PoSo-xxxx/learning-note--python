#list
a = list(range(0,10));  b = [1, "hello", 1+5j, 2.0, (1,2,3)]
print(a)                                                      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b)                                                      #[1, 'hello', (1+5j), 2.0, (1, 2, 3)]
print(a[0], a[2:6], a[-2])                                    #0 [2, 3, 4, 5] 8
print(a[2:]+b[:3])                                            #[2, 3, 4, 5, 6, 7, 8, 9, 1, 'hello', (1+5j)]
print(len(a), min(a), max(a), sum(a))                         #10 0 9 45
print(sorted(a, reverse = True))                              #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b.append("python"); b.remove(2.0); print(b)                   #[1, 'hello', (1+5j), (1, 2, 3), 'python']
b.clear(); print(b)                                           #[]
b = [5, 5 , 78, 1, "hello", 1+5j, 2.0, 5, (1,2,3)]
c = b.copy(); print(c)                                        #[5, 5, 78, 1, 'hello', (1+5j), 2.0, 5, (1, 2, 3)]
print(b.index(5), b.count(5))                                 #0 3
b.extend(c); print(b)                                         #[5, 5, 78, 1, 'hello', (1+5j), 2.0, 5, (1, 2, 3), 5, 5, 78, 1, 'hello', (1+5j), 2.0, 5, (1, 2, 3)]
b.reverse(); print(b)                                         #[(1, 2, 3), 5, 2.0, (1+5j), 'hello', 1, 78, 5, 5, (1, 2, 3), 5, 2.0, (1+5j), 'hello', 1, 78, 5, 5]
b.insert(5, 'test'); print(b)                                 #[(1, 2, 3), 5, 2.0, (1+5j), 'hello', 'test', 1, 78, 5, 5, (1, 2, 3), 5, 2.0, (1+5j), 'hello', 1, 78, 5, 5]
b.pop(3); print(b)                                            #[(1, 2, 3), 5, 2.0, 'hello', 'test', 1, 78, 5, 5, (1, 2, 3), 5, 2.0, (1+5j), 'hello', 1, 78, 5, 5]
#the member can be any kind of data type.
#[content]:declare a list; list(content):turn content into a list.
#[start:end:step]slice:used to choose the specific data in a sequence.
#(step:choosing the data by step,for exmaple:[::2]->1,3,5,7,9)
#list[-X]:search the Xth element from the right.
#len(list):counting the lenght of list.
#min(list):find the minimum element in the list(all element must be the same type).
#max(list):find the maximum element in the list(all element must be the same type).
#sum(list):return the sum of all element in the list(all element must be the numeric type).
#sorted(list, reverse = True/False(optional)):sort the list, the default will be ascending data,
#reverse = True: the data will be sorted in descending.
#list.append(element):add new element to the end of the list
#list.remove(element):remove the element from list, if the element is not in the list will cause exception
#list.clear():clean all element in the list
#list.copy():copy all element in the list
#list.index(element):return the first place of the finding element, if element is not in the list will cause exception
#list.count(element):return the number of times that the finding element shows up
#list1.extend(list2):add list2 to the end of list1
#list.reverse():arrange the whole list reversely
#list.insert(order, element):insert the element in 'order'th's place of the list
#list.pop(order):return and remove the element in the 'order'th place of the list. The default is -1, which is the last element of the list

#list comprehension
s = [x**2 for x in range(10)]                                 #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(s)                                                      #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#list can be declared in mathematical style, 
# the example above equal to:s = {x*x:x in [0...9]}