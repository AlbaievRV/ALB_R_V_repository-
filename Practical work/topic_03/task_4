def find_insertion_index(sorted_list, element):
  for i, item in enumerate(sorted_list):
    if element <= item:
      return i
  # If the element is greater than all elements, it goes to the end
  return len(sorted_list)


# Example usage:
numbers = [10, 20, 30, 40, 50]
new_element = 25

index = find_insertion_index(numbers, new_element)
print(f"Sorted list: {numbers}")
print(f"New element: {new_element}")
print(f"Insertion index: {index}")

# Inserting the element using the found index
numbers.insert(index, new_element)
print(f"List after insertion: {numbers}")