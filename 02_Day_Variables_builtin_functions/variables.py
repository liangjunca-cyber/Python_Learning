
# Variables in Python

first_name = 'James'
last_name = 'Liang'
country = 'Canada'
city = 'Ottawa'
age = 54
is_married = True
skills = ['ETL', 'Cognos', 'Python', 'React', 'Testing']
person_info = {
    'firstname': 'James',
    'lastname': 'Liang',
    'country': 'Canada',
    'city': 'Ottawa'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married, wife = 'James', 'Liang', 'Canada', 55, True, 'Jane Xu'

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('Wife: ', wife)