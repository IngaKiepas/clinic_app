import sqlite3

#creating database
def createDatabase():
    connection = sqlite3.connect('clinic.db')
    cursor = connection.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT,
                    last_name TEXT,
                    pesel INTEGER,
                    street TEXT,
                    city TEXT,
                    zip_code INTEGER
                )''')
    connection.commit()
    connection.close()

#adding a new patient
def add_patient(first_name, last_name, pesel, street, city, zip_code):
    connection = sqlite3.connect('clinic.db')
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO patients (first_name, last_name, pesel, street, city, zip_code) "
                       "VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, pesel, street, city, zip_code))

        connection.commit()
        print("Patient added!")
    except sqlite3.Error as error:
        print(error)
    finally:
        connection.close()

#editing patient data
def edit_patient(patient_id, first_name, last_name, pesel, street, city, zip_code):
    connection = sqlite3.connect('clinic.db')
    cursor = connection.cursor()

    try:
        cursor.execute('''UPDATE patients
                        SET first_name = ?,
                        last_name = ?,
                        pesel = ?,
                        street = ?,
                        city = ?,
                        zip_code = ?
                        WHERE patient_id = ?''', (first_name, last_name, pesel, street, city, zip_code, patient_id))

        connection.commit()
        print("Data updated!")
    except sqlite3.Error as error:
        print(error)
    finally:
        connection.close()

#deleting patient data
def delete_patient(patient_id):
    connection = sqlite3.connect('clinic.db')
    cursor = connection.cursor()

    try:
        cursor.execute('''DELETE FROM patients WHERE id = ?''',
                       (patient_id,))

        connection.commit()
        print("Data deleted!")
    except sqlite3.Error as error:
        print(error)
    finally:
        connection.close()

#listing all patients
def list_patients():
    connection = sqlite3.connect('clinic.db')
    cursor = connection.cursor()

    try:
        cursor.execute(''' SELECT * FROM patients''')
        rows = cursor.fetchall()
        print("Patients data: ")
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)
    finally:
        connection.close()
