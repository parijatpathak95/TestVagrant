from datetime import date, timedelta
import datetime

class Hospital(object):
    
    def __init__(self,name,location):
        self.name=name
        self.location=location
        self.PatientRecords=[]
    
    def addPatientToRecord(self,*patientList):
        if patientList:
            self.PatientRecords.extend(patientList)
        #print(self.PatientRecords)
        
    def getLocalPatientPercentage(self,tenure=1):
        tenureStartDate=date.today() - timedelta(int(tenure))
        
        localPatientListWithTenureFilter=list(filter(lambda x:((x.location).lower() == (self.location).lower() and x.registrationDate >= tenureStartDate), self.PatientRecords))
        
        localPercentage=(len(localPatientListWithTenureFilter)/len(self.PatientRecords))*100
        
        return localPatientListWithTenureFilter,localPercentage
    
    def getOutsidePatientPercentage(self,hospitalObject,tenure=1,):
        localPatientList,localPercentage=hospitalObject.getLocalPatientPercentage(tenure)
        outsidePatientListWithTenureFilter=list(set(hospitalObject.PatientRecords)-set(localPatientList))
        
        outsidePercentage=100-localPercentage
        return outsidePatientListWithTenureFilter,outsidePercentage
    
class Patient(object):
    
    def __init__(self,name,location,patientRegistrationDate):
        self.name=name
        self.location=location
        year, month, day = map(str,patientRegistrationDate.split('-'))
        registrationDate = datetime.date(int(year),int(month),int(day))

        self.registrationDate=registrationDate
        

hospitalObject=Hospital('ChinmayaMission','Banglore')

patient1=Patient('Pari','Banglore','2021-3-15')
patient2=Patient('Pallu','Banglore','2020-10-14')
patient3=Patient('Deepak','Mumbai','2020-10-14')
hospitalObject.addPatientToRecord(patient1,patient2,patient3)

tenure=5

localPatientList,localPercentage=hospitalObject.getLocalPatientPercentage(tenure)

outsidePatientList,outsidePercentage=hospitalObject.getOutsidePatientPercentage(hospitalObject,tenure)

print("Welcome To Chinmaya Mission Hospital")

print("Registation carried out for last "+str(tenure)+" days consist of "+str(round(localPercentage))+" as local and others "+ str(round(outsidePercentage)) +" being from outstation")



