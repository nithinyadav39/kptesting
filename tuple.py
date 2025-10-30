# # # # # t=("hello",1,23,("hi","a",24.5,("re",22,2.5)),46,49)
# # # # # print(len(t))
# # # # # print(t[3][3][0])


# # # # # creds={"ram":1234,"krish":2291,"pavan":1432}
# # # # # d={}
# # # # # username=input("username ")
# # # # # password=int(input("password "))
# # # # # if username=="ram":
# # # # #   if password==creds["ram"]:
# # # # #    print("hi ram")
# # # # # elif username=="krish":
# # # # #   if password==creds["krish"]:
# # # # #    print("hi krish")
# # # # # elif username=="pavan":
# # # # #   if password==creds["pavan"]:
# # # # #    print("hi pavan")
# # # # # else:
# # # # #   print("you enter the wrong creds")


# # # # creds={"ram":1234,"krish":2291,"pavan":1432}
# # # # d={}
# # # # username=input("username ")
# # # # password=int(input("password "))
# # # # if username in creds and password ==creds[username] :
# # # #   print("hi",username)



# # # l=["hi",22,33.5,[44.5,"hy",[2,4.5,"re",["e",298]]],44.5,48.2,"final"]
# # # print(len(l))
# # # l.append(653)
# # # print(l)
# # # l.remove(653)
# # # print(l)
# # # b=[963]
# # # l.extend(b)
# # # print(l)
# # # l.pop()
# # # print(l)
# # # l.insert(1,6)
# # # print(l)
# # # l.remove(6)
# # # print(l)

# # # # l[3][2][3].remove(l[3][2][3][0])
# # # del l[3][2][3][0]
# # # print(l)
# # # l.reverse()
# # # print(l)

# # example1 ={"A","B"}
# # example1.add("C")
# # print(example1)
# s=set()
# for i in range(1,21):
#     if i%3==0:
#         s.add(i)
# print(s)


l=[1,2,3,4,5,6,7,8,9]
s=set(l)
print(s)
s.add(10)
s.pop()
s.discard(3)
ss={1,2,13,4,15}
print(s.difference(ss))
print(s.union(ss))
print(s.intersection(ss))
print(s.symmetric_difference(ss))
print(s.clear())


l.append()