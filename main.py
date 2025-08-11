# CPRG216 Assigment #4 GROUP
# This program read in doctors.txt, facilities.txt,  laboratories.txt, patients.txt.
# Import a Python class for each txt file.
# This main menu displays options to go into sub-menus (1 for each file)
# The sub-menus allow user to create, search or modify data inside corresponded txt file
# In the end, any modification to the txt file will be commited to the file after user selecting 0 to return to the main menu.
#
# Inputs:
#       doctors.txt
#       facilities.txt
#       laboratories.txt
#       patients.txt
#       User's selection and entry
#
# Process Caculations:
#       For each txt file
#       Import the Class from another python file
#       Read the txt file
#       Create an object for each entry and group them into a list
#       Manipulte object's attributes to print, search, and edit object's info
#       Create a new instant when user add a new object
#       Write any modification/addition to file when user selects 0
#
# Output:
#       Print the doctors, facilities, laboratories and patients data to their corresponded txt file
#
# Author Duc Nguyen, Isabelle Helbig, Sean Lam
# Version 2022-12-11
#

# Calling the Main memu function
def main():
    mainMemu()

##########################################___DOCTOR_SESSION___##############################################################
import Doctor as d

# This function asks attributes and create a doctor object
def enterDoctorInfo():
    id = input("Enter Doctor ID: ")
    name = input("Enter Doctor name: ")
    specialty = input("Enter Doctor specialty: ")
    schedule = input("Enter Doctor schedule : ")
    qualification = input("Enter Doctor qualification: ")
    roomNumber = input("Enter Doctor roomNumber: ")
    doctor = d.Doctor(id, name, specialty, schedule, qualification, roomNumber)
    return doctor

# This function reads in the text file and create an object for each Doctor
def readDoctorsFile(doctors_list):
    doctor_file = open("doctors.txt", 'r')
    for line in doctor_file:
        items = line.rstrip().split('_')
        Doctor = d.Doctor(items[0], items[1], items[2], items[3], items[4], items[5])
        doctors_list.append(Doctor)
    doctor_file.close()    

# This function asks for an ID to look for in doctors objects list.
def searchDoctorById(doctors_list):
    doctor_id = input("Enter the doctor ID: ")
    for obj in doctors_list:
        if doctor_id == obj.id:
            obj.__str__()
            return obj
    print("Doctor with ID {} not found in file".format(doctor_id))
    return -1

# searchDoctorByName
def searchDoctorByName(doctors_list):
    doctor_id = input("Enter the doctor name: ")
    for obj in doctors_list:
        if doctor_id == obj.name:
            obj.__str__()
            return obj
    print("Doctor {} not found in file".format(doctor_id))
    return -1

# This function call another function to look for ID of an object, and modify its attributes
def editDoctorInfo(doctors_list):
    obj = searchDoctorById(doctors_list)
    obj.name = input("Enter Doctor name: ")
    obj.specialty = input("Enter Doctor specialty: ")
    obj.schedule = input("Enter Doctor schedule : ")
    obj.qualification = input("Enter Doctor qualification: ")
    obj.roomNumber = input("Enter Doctor roomNumber: ")
    print()
    displayDoctorsList(doctors_list)

# This function call a method to print formated text of the doctors
def displayDoctorsList(doctors_list):
    for doctor in doctors_list:
        doctor.__str__()
    print()

# This function write objects in memory to the text file
def writeDoctorsListToFile(doctors_list):
    doctor_file = open("doctors.txt", 'w')
    for obj in doctors_list:
        doctor_file.write("{}_{}_{}_{}_{}_{}\n".format(obj.id, obj.name,  obj.specialty, obj.schedule, obj.qualification, obj.roomNumber))
    doctor_file.close()

# This function adds new Doctor to Doctor object list
def addDrToList(doctors_list, new_doctor):
        doctors_list.append(new_doctor)

# This function prints the Doctor menu, and keeps looping until user selecting 0, The call to function to write objects to text file
def doctorsMenu(doctors_list):
    print("Doctor Menu")
    print("0 - Return to the Main Menu")
    print("1 - Display Doctor's list")
    print("2 - Search for Doctor by ID")
    print("3 - Search for Doctor by Name")
    print("4 - Add Doctor")
    print("5 - Edit Doctor info")
    choice = input("Enter option: ")
    while choice != "0":
        print()
        match choice:
            case "1": 
                displayDoctorsList(doctors_list)
            case "2":
                searchDoctorById(doctors_list)
            case "3":
                searchDoctorByName(doctors_list)
            case "4":
                new_Doctor = enterDoctorInfo()
                addDrToList(doctors_list, new_Doctor)
            case "5":
                editDoctorInfo(doctors_list)
        print()
        print("Doctor's Menu")
        print("0 - Return to the Main Menu")
        print("1 - Display Doctor's list")
        print("2 - Search for Doctor by ID")
        print("3 - Search for Doctor by Name")
        print("4 - Add Doctor")
        print("5 - Edit Doctor info")
        choice = input("Enter option: ")
    writeDoctorsListToFile(doctors_list)

##########################################___FACILITY_SESSION___##############################################################
import facility_class

def facilitiesMenu(facility_list):
#displays facility menu options, accepts, and returns users choice
    menu = int(input("""
Facility Menu
0 - Return to Main Menu
1 - Display Facilities List
2 - Add Facility
Enter option: """))
    
#selects users choice and sends it to functions. After returned, shows menu again
    while menu !=0:
        if menu == 1:
            displayFacilitiesList(facility_list)
        elif menu == 2:
            addFacilityToList(facility_list)
        menu = int(input("""
Facility Menu
0 - Return to Main Menu
1 - Display Facilities List
2 - Add Facility
Enter option: """))

#Gets new Facility object (with user-entered facility information) and adds it to the facilities list
def addFacilityToList(facility_list):
    print()
    new_facility = str(input("Enter Facility name: "))
    add_facility = facility_class.Facility(new_facility)
    facility_list.append(add_facility)
    writeFacilitiesToFile(facility_list)

#Read “facilities.txt” file into a list of Facility objects
def readFacilitiesFile():
    facility_file = open(r"facilities.txt")
    facility_list = []
    for line in facility_file:
        items = line.rstrip()
        facility = facility_class.Facility(items)
        facility_list.append(facility)
    facility_file.close()
    return facility_list

#Displays all the Facility information(attributes) in facilities list
def displayFacilitiesList(facility_list):
    print()
    for line in facility_list:
        print(line)

#Writes “facilities.txt” file from the list of Facility objects, maintaining correct formatting
def writeFacilitiesToFile(facility_list):
    facility_file = open(r"facilities.txt", 'w')
    for line in facility_list:
        new_line = line.formatFacilityInfo()
        facility_file.write(new_line)
    facility_file.close()

##########################################___PATIENT_SESSION___##############################################################
import Patient as p

# This function asks attributes and create a patient object
def enterPatientInfo():
    id = input("Enter Patient ID: ")
    name = input("Enter Patient name: ")
    diagnosis = input("Enter Patient diagnosis: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")
    patient = p.Patient(id, name, diagnosis, gender, age)
    return patient

# This function reads in the text file and create an object for each patient
def readPatientsFile(patients_list):
    patient_file = open("patients.txt", 'r')
    for line in patient_file:
        items = line.rstrip().split('_')
        patient = p.Patient(items[0], items[1], items[2], items[3], items[4])
        patients_list.append(patient)
    patient_file.close()    

# This function asks for an ID to look for in patients objects list.
def searchPatientById(patients_list):
    patient_id = input("Enter the Patient ID: ")
    for obj in patients_list:
        if patient_id == obj.id:
            obj.__str__()
            return obj
    print("Patient with ID {} not in patient file".format(patient_id))
    return -1

# This function call another function to look for ID of an object, and modify its attributes
def editPatientInfo(patients_list):
    obj = searchPatientById(patients_list)
    obj.name = input("Enter new Name: ")
    obj.diagnosis = input("Enter new diagnosis: ")
    obj.gender = input("Enter new gender: ") 
    obj.age = input("Enter new age: ")
    print()
    displayPatientsList(patients_list)

# This function call a method to print formated text of the patients
def displayPatientsList(patients_list):
    for patient in patients_list:
        patient.__str__()
    print()

# This function write objects in memory to the text file
def writePatientsListToFile(patients_list):
    patient_file = open("patients.txt", 'w')
    for obj in patients_list:
        patient_file.write(obj.formatPatientInfo(obj.id, obj.name, obj.diagnosis, obj.gender, obj.age))
    patient_file.close()

# This function adds new patient to patient object list
def addPatientToList(patients_list, new_patient):
        patients_list.append(new_patient)

# This function prints the patient menu, and keeps looping until user selecting 0, The call to function to write objects to text file
def patientsMenu(patients_list):
    print("Patient Menu")
    print("0 - Return to the Main Menu")
    print("1 - Display patient's list")
    print("2 - Search for patient by ID")
    print("3 - Add patient")
    print("4 - Edit patient info")
    choice = input("Enter option: ")
    while choice != "0":
        print()
        match choice:
            case "1": 
                displayPatientsList(patients_list)
            case "2":
                searchPatientById(patients_list)
            case "3":
                new_patient = enterPatientInfo()
                addPatientToList(patients_list, new_patient)
            case "4":
                editPatientInfo(patients_list)
        print()
        print("Patient Menu")
        print("0 - Return to the Main Menu")
        print("1 - Display patient's list")
        print("2 - Search for patient by ID")
        print("3 - Add patient")
        print("4 - Edit patient info")
        choice = input("Enter option: ")
    writePatientsListToFile(patients_list)


##########################################___MAIN_MENU_SESSION___##############################################################

def mainMemu():
    print("Welcome to the Alberta Rural Patient Care Management System\n")
    print("Main Menu")
    print("0 - Close application")
    print("1 - Doctors")
    print("2 - Facilities")
    print("3 - Laboratories")
    print("4 - Patients")
    choice = input("Enter option: ")
    while choice != "0":
        print()
        match choice:
            case "1": 
                doctors_list = []
                readDoctorsFile(doctors_list)
                doctorsMenu(doctors_list)
            case "2":
                facility_list = readFacilitiesFile()
                facilitiesMenu(facility_list)
            case "4":
                patients_list = []
                readPatientsFile(patients_list)
                patientsMenu(patients_list)
        print("\nWelcome to the Alberta Rural Patient Care Management System\n")
        print("Main Menu")
        print("0 - Close application")
        print("1 - Dortors")
        print("2 - Facilities")
        print("3 - Laboratories")
        print("4 - Patients")   
        choice = input("Enter option: ")            

if __name__ == "__main__":
    main()
