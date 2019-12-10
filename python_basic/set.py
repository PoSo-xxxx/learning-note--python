#set
nn= set({1,2,3,4,5});mm= set({3,4,5,6,7}); oo= set({1,2,3})
print(nn, mm, sep = '\n')                                     #{1, 2, 3, 4, 5}
                                                              #{3, 4, 5, 6, 7}
print(len(nn), max(nn), min(nn), sum(nn))                     #5 5 1 15
print(sorted(mm, reverse=True))                               #[7, 6, 5, 4, 3]
#set need to use set() to declare.
#the elements in a set wil not repeat, only remain one when there are multiple same elements.
#len(set)):counting the lenght of set.
#min(set):find the minimum element in the set(all element must be the same type).
#max(set):find the maximum element in the set(all element must be the same type).
#sum(set):return the sum of all element in the set(all element must be the numeric type).
#sorted(set, reverse = True/False(optional)):sort the set, the default will be ascending data,
#reverse = True: the data will be sorted in descending.(the output will become  a list).
#set(data):turn data into a set.

#set operator
print(nn|mm, nn&mm, nn-mm, nn^mm, sep = '\n')                 #{1, 2, 3, 4, 5, 6, 7}
                                                              #{3, 4, 5}
                                                              #{1, 2}
                                                              #{1, 2, 6, 7}
print(nn>oo, nn<oo, nn.isdisjoint(mm))                        #True False False
oo.add(8); print(oo)                                          #{8, 1, 2, 3}
oo.remove(8); print(oo)                                       #{1, 2, 3}
oo.discard(8); print(oo)                                      #{1, 2, 3}
oo.pop(); print(oo)                                           #{2, 3}
oo.clear(); print(oo)                                         #set()
#a|b:a union b, equal to a.union(*b).(can do with more than two set)
#a&b:a intersection b, equal to a.intersection(*b).(can do with more than two set)
#a-b:a difference b, eqaul to a.difference(*b).(can do with more than two set)
#a^b:a symmetric difference b, equal to a.symmetric_difference(b).
#a>b:is a a superset of b, equal to a.issuperset(b), output is boolean.
#a<b:is a a subset of b, equal to a.issubset(b), output is boolean.
#a.isdisjoint(b):does a and b have joint(a&b), yes->False, no->True.

#other usage:
#a.update(*b) equal to a |= b | ...
#a.intersection_update(*b) equal to a &= b & ...
#a.difference_update(*b) equal to a -= b | ...
#a.symmetric_difference_update(b) equal to a ^= b

#set conprehensions
#just like list, dict, declarsion can be written in mathematical style
