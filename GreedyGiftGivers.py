'''
LANG: PYTHON3
PROG: gift1
'''
import re
x = open("gift1.in")
content = x.readlines()
index = 0
count = 0
people = {}
donor = ""
giving = False
donating = False
for i in content:
    i = i.strip()
    if index == 0:
        count = int(i)
    elif index - 1 < count:
        people[i] = 0
    else:
        if giving == True:
            nums = re.findall(r'\d+',i)
            nums = [eval(x) for x in nums]
            people_count = nums[1]
            amount = nums[0]
            people[donor] -= amount
            if people_count == 0 and amount == 0:
                pass
            else:
                donating = True
            giving = False
            num = 1
        elif donating == True:
            if num == people_count:
                try:
                    people[i] += amount//people_count
                    people[donor] += (amount % people_count)
                except:
                    pass
                donating = False
            else:
                try:
                    people[i] += amount//people_count 
                except:
                    pass
            num += 1
        else:
            donor = i
            giving = True
    index += 1
x.close()
x = open("gift1.out","w")
for i in people.keys():
    x.write(f"{i} {people[i]}\n")



















