#running application

from clinic_database import *

createDatabase()

while True:
    print('Welcome to the Clinic, these are you options: \n')
    print('1. Add a new patient')
    print('2. Edit existing patient')
    print('3. Delete existing patient')
    print('4. List all patients')
    print('5. Exit our clinic')

    choice = input('Enter your choice: (number)')

    if choice == '1':
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        pesel = input('Enter pesel number: ')
        street = input('Enter street: ')
        city = input('Enter city: ')
        zip_code = input('Enter zip code: ')
        add_patient(first_name, last_name, pesel, street, city, zip_code)
    elif choice == '2':
        patient_id = int(input('Enter patient id: '))
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        pesel = input('Enter pesel number: ')
        street = input('Enter street: ')
        city = input('Enter city: ')
        zip_code = input('Enter zip code: ')
        edit_patient(patient_id, first_name, last_name, pesel, street, city, zip_code)
    elif choice == '3':
        patient_id = int(input('Enter patient id: '))
        delete_patient(patient_id)
    elif choice == '4':
        list_patients()
    elif choice == '5':
        print('Bye! See you soon !')
        break
    else:
        print('Invalid number! Try again and enter valid number (1-5)!')

else:
    print('Error! There is something wrong with creating the database connection!')

