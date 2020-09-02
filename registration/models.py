from datetime import date
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.db import models

def check_correct_data(value):
    if value < date.today():
        raise ValidationError('Proposed date must be present or future date.')


class Specialisation(models.Model):
    specialisation = models.CharField(max_length=64, verbose_name="Name specialisation")
    description = models.TextField(verbose_name="Describe specialisation")
    image = models.ImageField(upload_to='specialisation/', blank=True, null=True)

    def get_delete_url(self):
        return f"/registration/specialisation/delete/{self.pk}/"
        # return reverse("delete_specialisation", args=(self.pk,)) zapis alternatywny

    def get_modify_url(self):
        return f"/registration/specialisation/modify/{self.pk}/"

    def __str__(self):
        return self.specialisation


class Term(models.Model):
    doctor = models.ForeignKey("Doctor", verbose_name="Select doctor", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Determine date of term (in YYYY-MM-DD form):", validators=[check_correct_data])
    time_from = models.TimeField(verbose_name="Determine beginning time (in HH:MM form)")
    time_to = models.TimeField(verbose_name="Determine ending time (in HH:MM form)")
    status = models.CharField(max_length=64, default="unreserved")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.date} from {self.time_from.strftime('%H:%M')} to {self.time_to.strftime('%H:%M')}"

    def get_modify_url(self):
        return f"/registration/offerterm/modify/{self.pk}/"


class Doctor(models.Model):
    medical_title = models.CharField(max_length=64, verbose_name="medical title")
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="determine the proper user", null=True)
    specialisation = models.ManyToManyField(Specialisation)
    image=models.ImageField(upload_to='doctor/', default='img/doctors/doctors-4.jpg', blank=True, null=True)

    def __str__(self):
        return f"{self.medical_title} {self.user.first_name} {self.user.last_name}"

    def get_modify_url(self):
        return f"/registration/doctor/modify/{self.pk}/"

    def get_terms(self):
        terms=self.term_set.all().order_by("date")
        return terms


class Complaint(models.Model):
    title=models.CharField(max_length=64, verbose_name="complaint title")
    description=models.TextField(verbose_name="complaint description")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    term=models.ForeignKey(Term, verbose_name="related appointment", on_delete=models.CASCADE)

    def get_user(self):
        return f"{self.user.first_name} {self.user.last_name}"

