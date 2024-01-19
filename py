def indexed_names(names):
    indexed_list = []
    for i, name in enumerate(names):
        indexed_list.append(f"{i}: {name}")
    return indexed_list

empty_list = []
result_empty = indexed_names(empty_list)
print("Test Case 1:")
print(f"Input: {empty_list}")
print(f"Output: {result_empty}")
print()

name_list = ["John", "Jane", "Bob"]
result_names = indexed_names(name_list)
print("Test Case 2:")
print(f"Input: {name_list}")
print(f"Output: {result_names}")
