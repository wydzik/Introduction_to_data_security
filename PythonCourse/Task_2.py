names=["Marcin","Krzysztof","Filip","Jan","Natan","Nikodem",
       "Natalia","Mela","Lukasz","Robert","Anna","Aleksandra", "Szymon"]

def printing_all_names(names):
    for name in names:
        print(name)

def printing_long_names(names):
    for name in names:
        if len(name)>5:
            print(name)

def printing_long_n_names(names):
    for name in names:
        if len(name) > 5:
            for char in name:
                if char =='n'or char=='N':
                    print(name)
                    break

def ereasing_the_list(names):
    while len(names)>0:
        names.pop()

print("Printing all names: ")
printing_all_names(names)
print("Printing all names longer than 5 characters: ")
printing_long_names(names)
print("Printing all names longer than 5 characters, that contains 'n' letter: ")
printing_long_n_names(names)
print("Clearing the list.")
ereasing_the_list(names)
print("Printing all remaining names: ")
printing_all_names(names)