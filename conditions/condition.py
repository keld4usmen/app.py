user = 'Admin'
logged_in = 'True'

if user =='Admin' and 'logged_in':
        print('Admin Page')
else:
        print('Bad cred')        


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5== 0):
         return "Fizz_Buzz"
    if input  % 3== 0:
         return "fizz"
    if input % 5== 0:
         return "buzz"
         return input
  
print(fizz_buzz(10))