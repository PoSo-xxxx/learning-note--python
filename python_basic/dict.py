#dictionary
iden = {'name':'John','age':18,'grade':[5,4,1,2,8,3]}; print(iden)     #{'name': 'John', 'age': 18, 'grade': [5, 4, 1, 2, 8, 3]}
alpha = dict(a=1, b=2, c=3, d=4, e=5); print(alpha)                    #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(len(alpha), max(alpha), min(alpha))                              #5 e a
print('a' in iden)                                                     #False
print(iden.get('gender', '404'))                                       #404
print(alpha.setdefault('f', 6))                                        #6
print(alpha)                                                           #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
new_data = {'gender':True}
iden.update(new_data)
print(iden.items(), iden.keys(), iden.values(), sep="\n")              #dict_items([('name', 'John'), ('age', 18), ('grade', [5, 4, 1, 2, 8, 3]), ('gender', True)])
                                                                       #dict_keys(['name', 'age', 'grade', 'gender'])
                                                                       #dict_values(['John', 18, [5, 4, 1, 2, 8, 3], True])
iden.pop('name');iden.popitem()
print(iden)                                                            #{'age': 18, 'grade': [5, 4, 1, 2, 8, 3]}
#the element in dict have two parts:key, value
#len(dict):counting the lenght of dict.
#min(dict):find the minimum element in the dict(all element must be the same type).
#max(dict):find the maximum element in the dict(all element must be the same type).
#dict.get(key, default(optional)):looking for key in dict,
# if find it, output value of key; if not found, output the default.
#dict.setdefault(key, default(optional)):looking for key in dict,
# if find it, output value of key; if not found, create a new key=default in dict.
#dict.update(dict2):add dict2 to dict.
#dict.items():output the whole element in dict.
#dict.keys():output the all keys in dict.
#dict.values():output all values in dict.
#dict.pop('key'):remove the 'key' from dict.
#dict.popitem():remove the one key following LIFO rules(LIFO:last in first out).

#dict comprehension
word = 'letter';word_count = {char:word.count(char) for char in set(word)}
print(word_count)                                                      #{'t': 2, 'l': 1, 'e': 2, 'r': 1}
#the same usage as list