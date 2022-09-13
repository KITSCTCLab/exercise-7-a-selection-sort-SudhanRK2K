from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(0,size):
    j=i
    for j in range(i+1,size-1):
      if array[i] < array[j]:
        j=1
    (array[i],array[j]) = (array[j],array[i])
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
