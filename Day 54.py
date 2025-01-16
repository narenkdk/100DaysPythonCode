#Day 54 - List comprehensions


#Use list comprehensions to filter and transform lists.

nested_list = [["python", "java"], ["php", "perl"], ["ruby", "pandas"]]
result = [
    word.upper() * 2 
    for sublist in nested_list 
    for word in sublist 
    if word.startswith("p") or len(word) > 5
]


print(result)
