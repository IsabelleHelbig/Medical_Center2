class Facility:
    
    #attributes of the Facility Class
    def __init__(self, name):
        self.name = name
    
    #sets attributes
    def set_name(self,name):
        self.name = name
    
    #Formats facility information (attributes) in the same format used in the “facilities.txt” file
    def formatFacilityInfo(self):
        return f"{self.name}\n"
    
    #Formats facility information(attributes) – for display, see Sample Run, “Display Facilities List”
    def __str__(self):
        return f"{self.name}"
    
