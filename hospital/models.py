from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table ="doctor"

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'hospital'

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return f"{self.doctor.name} -- {self.patient.name}"

    class Meta:
        app_label = 'hospital'

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        app_label = 'hospital'
# Les commentaires suivants ont été ajoutés pour expliquer chaque modèle

# Modèle Doctor (Médecin)
# Ce modèle représente un médecin dans l'application de l'hôpital.
# Il contient les informations telles que le nom, le numéro de téléphone mobile et la spécialité du médecin.

# Modèle Patient
# Ce modèle représente un patient dans l'application de l'hôpital.
# Il contient les informations telles que le nom, le genre, le numéro de téléphone mobile et l'adresse du patient.

# Modèle Appointment (Rendez-vous)
# Ce modèle représente un rendez-vous entre un médecin et un patient dans l'application de l'hôpital.
# Il contient les informations telles que le médecin associé, le patient associé, la date et l'heure du rendez-vous.

# Modèle Contact (Contact)
# Ce modèle représente un formulaire de contact dans l'application de l'hôpital.
# Il contient les informations telles que le nom de la personne, le contact, l'e-mail, le sujet du message, le message lui-même,
# la date du message, et une indication indiquant si le message a été lu ou non.
