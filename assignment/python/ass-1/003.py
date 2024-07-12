# assign-1 Program-2
# 3. Create a Marksheet for 5 subjects and calculate total, average and grade with if else.

html = int(input("Enter Mark:-"))
css = int(input("Enter Mark:-"))
js = int(input("Enter Mark:-"))
php = int(input("Enter Mark:-"))
python = int(input("Enter Mark:-"))

total = (html+css+js+php+python)
avg = total/5

if ((avg>90) and (avg<100)):
    {
    print("0")
    }
    elif((avg>80) and (avg<89)):
    {
    print("A")
    }
    elif((avg>70) and (avg<79)):
    {
    print("B")
    }
    elif((avg>60) and (avg<69)):
    {
    print("C")
    }
    elif((avg>50) and (avg<59)):
    {
    print("D")
    }elif((avg>40) and (avg<49)):
    {
    print("E")
    }else:
    {
    print("F")
    }


# OUTPUT ===>
