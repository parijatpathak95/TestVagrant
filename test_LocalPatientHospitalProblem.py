import unittest
from LocalPatientHospitalProblem import Hospital
from LocalPatientHospitalProblem import Patient
class Test_HospitalPatient(unittest.TestCase):

    def test_allLocalPatientAllLowercas(self):
        hospitalObject=Hospital('ChinmayaMission','Banglore')

        patient2=Patient('Pallu','banglore','2021-3-14')
        patient3=Patient('Deepak','banglore','2021-3-15')
        hospitalObject.addPatientToRecord(patient2,patient3)
        a,b=hospitalObject.getLocalPatientPercentage(10)
        self.assertEqual(round(b),100.0)

    def test_fewLocalPatientMixCases(self):
        hospitalObject=Hospital('ChinmayaMission','Banglore')
        patient1=Patient('Deepak','Delhi','2021-3-14')
        patient2=Patient('Pallu','BANGLORE','2021-3-14')
        patient3=Patient('Deepak','banglore','2021-3-15')
        hospitalObject.addPatientToRecord(patient1,patient2,patient3)
        a,b=hospitalObject.getLocalPatientPercentage(10)
        self.assertEqual(round(b),67.0)

    def test_allOcalPatientGetLocalPatient(self):
        hospitalObject=Hospital('ChinmayaMission','Banglore')
        patient1=Patient('Deepak','Delhi','2021-3-14')
        patient2=Patient('Pallu','BANGLOREML','2021-3-14')
        patient3=Patient('Deepak','banglorenj','2021-3-15')
        hospitalObject.addPatientToRecord(patient1,patient2,patient3)
        a,b=hospitalObject.getLocalPatientPercentage(10)
        self.assertEqual(round(b),0.0)

    def test_allOutsidePatientGetLocalPatient(self):
        hospitalObject=Hospital('ChinmayaMission','Banglore')
        patient1=Patient('Deepak','Delhi','2021-3-14')
        patient2=Patient('Pallu','BANGLOREML','2021-3-14')
        patient3=Patient('Deepak','banglorenj','2021-3-15')
        hospitalObject.addPatientToRecord(patient1,patient2,patient3)
        a,b=hospitalObject.getLocalPatientPercentage(10)
        self.assertEqual(round(b),0.0)

    def test_allOutsidePatientGetOutstationPatient(self):
        hospitalObject=Hospital('ChinmayaMission','Banglore')
        patient1=Patient('Deepak','Delhi','2021-3-14')
        patient2=Patient('Pallu','BANGLOREML','2021-3-14')
        patient3=Patient('Deepak','banglorenj','2021-3-15')
        hospitalObject.addPatientToRecord(patient1,patient2,patient3)
        a,b=hospitalObject.getOutsidePatientPercentage(hospitalObject,tenure=10,)
        self.assertEqual(round(b),100.0)

if __name__ == '__main__':
    unittest.main()
