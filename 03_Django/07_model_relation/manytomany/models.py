from django.db import models

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through="Reservation")
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
# doctor1 = Doctor.objects.create(name='ppp2')
# doctor2 = Doctor.objects.create(name='p2')
# patient1 = Patient.objects.create(name='tak')
# patient2 = Patient.objects.create(name='harry')

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'