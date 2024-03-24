patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)

raw = 'this\t\n and that'

  # this\t\n and that
print (raw)

multi = """It was the best of times.
  It was the worst of times."""

  # It was the best of times.
  #   It was the worst of times.
print (multi)

letter = "hai sethuraman"
for i in letter:
    if i == "a":
        pass
        print("pass statement is execute ..............")
    else:
        print(i)

def mid_three_char(astring):
    mid =int(len(astring)/2)
    print(mid)
    print( astring[mid-1:mid+2])

mid_three_char("Son")

def buying_candy( amount_of_money ) :
    if amount_of_money < 2:
        return 1
    dp  = {
        1: 1,
        2: 2
    }
    
    for x in range(3, amount_of_money+1):
        if x-1>0 and x-2>0:
            dp[x] = dp[x - 1] + dp[x-2]
        

    return dp[amount_of_money]

print(buying_candy(5))

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print([(1,20)]+[(1,2,3)])
