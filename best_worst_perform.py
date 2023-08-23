import numpy as np

names = ['Ben', 'Omer', 'Karen', 'Celine', 'Sue', 'Bora', 'Rose', 'Ellen', 'Bob', 'Taylor,', 'Jude']
number_of_calls = [300, 10, 500, 70, 100, 100, 600, 800, 200, 450, 80]
average_deal_sizes = [8, 6, 24, 32, 5, 25, 25, 40, 15, 10, 12]
revenues = [2400, 60, 12000, 2275, 500, 770, 4000, 6000, 800, 1200, 500]
data =np.array([],dtype=int)
#Define the append_names function
def append_names(names_list):
  global data
  for i in names_list:
    data = np.append(data,names.index(i))
#Define the append_performance_measures function
def append_performance_measures(feature_list):
  global data
  data = np.append(data,feature_list)

#Use the append_names and append_sales_performance_measures to add the data
append_names(names)
append_performance_measures(number_of_calls)
append_performance_measures(average_deal_sizes)
append_performance_measures(revenues)

#Print the array and its shape to see the result
print(data)
print(data.shape)


#Use the .reshape() method to change the array structure to 4 rows and 11 columns
data = data.reshape(4,11)

#Print the resulting array and its shape
print(data)
print(data.shape)


#Define the function calculate_performance
def calculate_performance(employee_name):
  idx = names.index(employee_name)
  number_of_calls = data[1,idx]
  avg_deal_size = data[2,idx]
  revenue = data[3,idx]

  score =(avg_deal_size*revenue)/number_of_calls

  return score

print(calculate_performance("Ellen"))


#Calculate the performance of each employee
performance_scores = []
for name in names:
  score = int(calculate_performance(name))
  performance_scores.append(score)
print(performance_scores)


#Add the "performance_scores" list to the "data" array
data = np.concatenate( (data, [performance_scores]), axis =0)

#Print the resulting array
print(data)


#Use .argmax() and .argmin() methods to determine the best and worst performing employees
idx_best_employee = np.argmax(data[4])
idx_worst_employee = np.argmin(data[4])


#Print out the results
print(f"Best Performing Employee: {names[idx_best_employee]} ")
print(f"Worst Performing Employee: {names[idx_worst_employee]} ")