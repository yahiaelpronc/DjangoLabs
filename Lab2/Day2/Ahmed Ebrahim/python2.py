#1
str1 = input("Please enter your own String : ")
ch = input("Please enter your own Character : ")

for i in range(len(str1)):
    if(str1[i] == ch ):
        print(ch, " is Found at Position " , i + 1)




#2
num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)


#3
dic = {'p': [11, 2], 
             'r': [3, 2, 1], 
             'q': [7, 4]}
  
# print original dictionary
print("The original dictionary is : " ,dic)
  
# Sort Dictionary key and value List
# dictionary comprehension
sort_dict = {key: sorted(dic[key]) for key in sorted(dic)}

# printing result 
print("The sorted dictionary : " , sort_dict) 

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')