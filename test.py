from tabulate import tabulate
table = [['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]
print(tabulate(table, headers=['First Name', 'Last Name', 'Age']))
