from typing import List

def selectionSort(array, size) -> List[int]:
  # Write your code here
  for i in range(0,size-2):
    min=i
    for j in range(i+1,size-1):
      if array[i] < array[min]:
        min=j
    (array[i],array[min]) = (array[min],array[i])
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
