# assign-1 Program-3
# 3. Create a Marksheet for 5 subjects and calculate total, average and grade with if else.

html = int(input("HTML Mark:-"))
css = int(input("CSS Mark:-"))
js = int(input("JS Mark:-"))
php = int(input("PHP Mark:-"))
python = int(input("PYTHON Mark:-"))

total = (html+css+js+php+python)
avg = total/5

if ((avg>90) and (avg<100)):
    print("0")
elif ((avg>80) and (avg<89)):
    print("A")
elif ((avg>70) and (avg<79)):
    print("B")
elif ((avg>60) and (avg<69)):
    print("C")
elif ((avg>50) and (avg<59)):
    print("D")
elif ((avg>40) and (avg<49)):
    print("E")
else:
    print("F")
    


# OUTPUT ===>
# HTML Mark:-55
# CSS Mark:-55
# JS Mark:-55
# PHP Mark:-55
# PYTHON Mark:-55
# E
# === Code Execution Successful ===
