import facility_class

def main(facility_list):
#displays facility menu options, accepts, and returns users choice
    menu = int(input("""
Facility Menu
0 - Return to Main Menu
1 - Display Facilities List
2 - Add Facility
Enter option: """))
    
#selects users choice and sends it to functions. After returned, shows menu again
    while menu !="":
        if menu == 0:
            pass
        elif menu == 1:
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
    

if __name__ == "__main__":
    facility_list = readFacilitiesFile()
    main(facility_list)