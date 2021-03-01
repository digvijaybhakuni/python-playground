from tabulate import tabulate

from data import posts

datatable = [['First Name', 'Last Name', 'Age'], ['John', 'Smith', 39], ['Mary', 'Jane', 25], ['Jennifer', 'Doe', 28]]


print(" Simple Output ")
print(tabulate(datatable)) 
print(" Frist Row as headers ")
print(tabulate(datatable, headers='firstrow')) 
print(" table formated as grid ")
print(tabulate(datatable, headers='firstrow', tablefmt='grid')) 
print(" table formated as fancy_grid ")
print(tabulate(datatable, headers='firstrow', tablefmt='fancy_grid')) 

print('using map object to print')
print(tabulate(posts()))

