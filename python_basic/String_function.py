#character&string
a = 'hello '; b = 'python'; c = 10
a += b; b *= 2
print(a, b)                            #hello python pythonpython
print(a[0], b[2:5])                    #h tho
print(r'\n')                           #\n
print(len(a), type(str(c)))            #12 <class 'str'>
#string:string is immutable sequence,but it can be ressigan to
#different memory address.
#r'content':remain special 'content', for example:\n.
#len(s):count the long of a string; str(s):turn s into string.

a = 'hello'; b = 'HELLO '
c = "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.s.x.y.z.1.2.3.4.5.6.7.8.9.0. "
print(a.islower(), b.isupper())        #True True
print(a.isalpha(), a.isdigit())        #True False
print(b.isalnum(), b.isspace())        #False False
print(a.upper(), b.lower())            #HELLO hello
print(c.split('.',10))                 #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k.l.m.n.o.p.q.r.s.t.u.v.w.s.x.y.z.1.2.3.4.5.6.7.8.9.0. ']
print(c.rsplit('.',10))                #['a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.s.x.y.z.1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']
print(c.strip('a'))                    #.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.s.x.y.z.1.2.3.4.5.6.7.8.9.0.
print(c.rstrip('0. '))                 #a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.s.x.y.z.1.2.3.4.5.6.7.8.9
#s.islower():check out if string's content are all lowercase.
#s.isupper():check out if string's content are all capital.
#s.isalpha():check out if string's content are all alphabet.
#s.isdigit():check out if string's content are all number.
#s.isalnum():check out if string's contnet are all alphabet or number.
#s.isspace():check out if string's content are all blankspace.
#s.upper():change lowercase to capital; s.lower():change capital to lowercase.
#s.split(content,maxsplit(optional)):split a string by 'content' for (maxsplit) times from left side.
#s.rsplit(content, maxsplit(optional)): the same as s.split(...), but start from right side.
#s.strip(content):remove 'content' in a string from left side.
#s.rstrip(content):the same as s.strip, but start from right side.