# assign-1 Program-4
# 4. Write a program to add employee names in a list EMPNAME and perform add,remove and append methods.




EMPNAME = ["ram", "shyam", "het"]
print(EMPNAME)
print(len(EMPNAME))
print(type(EMPNAME))

EMPNAME.append("ramesh")
print(EMPNAME)

EMPNAME.remove("shyam")
print(EMPNAME)

EMPNAME.insert(2, "shyam")
print(EMPNAME)


# OUTPUT ===>
# ['ram', 'shyam', 'het']
# 3
# <class 'list'>
# ['ram', 'shyam', 'het', 'ramesh']
# ['ram', 'het', 'ramesh']
# ['ram', 'het', 'shyam', 'ramesh']

# === Code Execution Successful ===
