file = open('employee_revenue.txt','r')
data = file.read()
print(data)
#You can see that the data needs to be cleaned and information has to be extracted from these lines.
#To be able to clean the data, you need to separate the text into lines.
# 📌 Use the .splitlines() method.

lines = data.splitlines()
print(lines)
print("#############################################")

string = lines[0]
print(string)
string = string.strip(' ')
print(string)
string = string.lower()
string = string.capitalize()
split_string = string.split(" ")
name = split_string[0]
call_number = split_string[2]
print("#############################################")

for i in split_string:
  #Divide the number from it
  if "$" in i:
    average_deal_size =i.split("$")[0]

#Print the average deal size
print(average_deal_size)
print("#############################################")

#Find the index of element "dollars"
dollars_index = split_string.index("dollars")
#Subtract one from the index to identify the index of the revenue element
revenue_index = dollars_index - 1
#Extract the revenue
revenue = split_string[revenue_index]

#Print out the extracted information
print("Name:", name)
print("Number of calls:", call_number)
print("Average deal size:", average_deal_size)
print("Revenue:", revenue)
print("#############################################")

#Convert the datatypes of average deal size, number of calls, and revenue
average_deal_size = int(average_deal_size)
call_number = int(call_number)
revenue = int(revenue)


#Print out the information again
print("Name type:", type(name))
print("Number of calls type:", type(call_number))
print("Average deal size type:", type(average_deal_size))
print("Revenue type:", type(revenue))
print("#############################################")

#Create empty lists for the names, number of calls, average deal sizes, revenues
names = []
call_numbers = []
average_deal_sizes = []
revenues = []

#Loop over the whole data
for employee in lines:
    #Clean the string
   employee = employee.strip(" ")
   employee = employee.lower()
   employee = employee.capitalize()

    #Split the clean string
   split_employee = employee.split(" ")
    
    #Extract the name
   name = split_employee[0]
   call_number = split_employee[2]
    

    #Extract the average deal size
   for i in split_employee:
    if "$" in i:
      average_deal_size = i
   average_deal_size = average_deal_size.split("$")[0]

    #Extract the revenue
   dollars_index = split_employee.index("dollars")
   revenue_index = dollars_index - 1
   revenue = split_employee[revenue_index]


    #Convert to the correct data types
   average_deal_size = int(average_deal_size)
   call_number = int(call_number)
   revenue = int(revenue)
    #Append the information to the lists
   names.append(name)
   call_numbers.append(call_number)
   average_deal_sizes.append(average_deal_size)
   revenues.append(revenue)
print("#############################################")

#Print out the information
print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal sizes:", average_deal_sizes)
print("Revenues:", revenues)
print("#############################################")

#Create empty lists again
names = []
call_numbers = []
average_deal_sizes = []
revenues = []


#Define a function to clean and extract the data
def clean_extract(lines):

  for employee in lines:


    employee = employee.strip(" ")
    employee = employee.lower()
    employee = employee.capitalize()

    split_employee = employee.split(" ")

    name = split_employee[0]
    call_number = split_employee[2]


    for i in split_employee:
      if "$" in i:
        average_deal_size = i
        average_deal_size = average_deal_size.split("$")[0]
      
    dollars_index = split_employee.index("dollars")
    revenue_index = dollars_index -1
    revenue = split_employee[revenue_index]

    average_deal_size = int(average_deal_size)
    call_number = int(call_number)
    revenue = int(revenue)

    names.append(name)
    call_numbers.append(call_number)
    average_deal_sizes.append(average_deal_size)
    revenues.append(revenue)

    
  return names,call_number,average_deal_sizes,revenues

#Assign returned values to variables
names,call_number,average_deal_sizes,revenues = clean_extract(lines)
print("#############################################")

#Print out the information
print("Names:", names)
print("Number of calls:", call_numbers)
print("Average deal sizes:", average_deal_sizes)
print("Revenues:", revenues)
print("#############################################")

#Check the number of employees
print(len(names))
print("#############################################")

#Generate IDs
IDs = list(range(0,11))
print(IDs)
print("#############################################")
#Check the number of IDs
len(IDs)

dictionary1 = dict(zip(IDs,names))
print(dictionary1)
dictionary2 = dict(zip(revenues,names))
print(dictionary2)
print("#############################################")

#Find the lowest performing employees (ascending order)
sorted_dictionary = sorted(dictionary2,reverse=False)[0:3]

for i in sorted_dictionary:
  print(dictionary2[i])

#Find the best performing employees (descending order)
sorted_dictionary = sorted(dictionary2,reverse= True)[0:3]
print("#############################################")

for i in sorted_dictionary:
  print(dictionary2[i])

