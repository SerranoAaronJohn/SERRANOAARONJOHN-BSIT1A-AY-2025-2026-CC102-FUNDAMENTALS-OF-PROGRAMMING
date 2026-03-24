my_list = []

# 1. Generate a list of numbers from 1 to 9 using range()
for i in range(1, 10):
    my_list.append(i)

# Output the original list and its length
print(f"Original list: {my_list}   Length of list: {len(my_list)}")

# 2. Check for unique elements (Filled-in logic)
y = 1
# Fill in the blank: loop through the length of my_list
for x in range(len(my_list)): 
    # Fill in the blank: check if y is within the list boundaries
    if y < len(my_list): 
        # Fill in the blank: compare current element to the 'y' element
        if my_list[x] == my_list[y]: 
            # my_list.remove(my_list[x])
            del my_list[x]
        else:
            y = y + 1
    else:
        break

print("The list with unique elements only.")
print(my_list)
