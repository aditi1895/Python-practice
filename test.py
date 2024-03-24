# # STUDENT = {'name': Str,
# #            'Age': '',
# #            'class': ''}

# def verify_sudent_schema(Age):
#     try:
#         int_age = int(Age)
#         return int_age
#     except ValueError as e:
#         raise ValueError

# def update_value(Age):
#     print(Age)
#     return Age
#     # pass

# names = ['Ana','Casper', 'Steve']
# Ages = ['a',15,12]
# Classes = [4,6,5]

# Students = []

# for i in range(3):
#     print(type(names[i]))
#     update_value(Ages[i])
#     # update_value(names[i], Ages[i], Classes[i])
#     # Students.append({'name': names[i], 'Age': Ages[i], 'Class': Classes[i]})
#     # print(Students[i])
def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def prime(max_val):
    for i in range(max_val):
        if is_prime(i):
            yield i

if __name__ == '__main__':
    # print(prime(25))
    g_obj = prime(25)
    for i in prime(25):
        print(i)
        print(prime.iter())
    