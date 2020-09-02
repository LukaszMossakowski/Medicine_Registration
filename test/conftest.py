from datetime import date, time
import pytest
from django.contrib.contenttypes.models import ContentType
from django.test import Client
from django.contrib.auth.models import User, Permission, Group
from registration.models import Specialisation, Doctor, Term, Complaint


@pytest.fixture
def client():
    client=Client()
    return client


@pytest.fixture
def group():
    items=[]
    group=Group.objects.create(name="doctor")
    items.append(group)
    return items


@pytest.fixture
def users(group):
    # models=ContentType.objects.filter(app_label="registration")
    # bv=Permission.objects.filter(content_type__in=models)
    user=User.objects.create(username="test_user", first_name="Kazimierz", last_name="Deyna")
    user.groups.set(group)
    user.set_password("tester2020")
    # user.user_permissions.set(bv)
    user.save()
    return user


@pytest.fixture
def specialisations(group):
    items=[]
    for specialisation, description in [("specialisation1","description1"), ("specialisation2","description2"),
                                        ("specialisation3","description3")]:
        specialisation=Specialisation.objects.create(specialisation=specialisation, description=description)
        items.append(specialisation)
    return items


@pytest.fixture
def doctors(users, specialisations):
    items=[]
    for specialisation in specialisations:
        x=Doctor.objects.create(medical_title="doctor", user=users)
        x.specialisation.set(specialisations)
        items.append(x)
    return items


@pytest.fixture
def terms(doctors, users):
    items=[]
    for doctor in doctors:
        for user in users:
            x=Term.objects.create(doctor=doctor,date=date(2021,7,24),time_from=time(12,15),
                                  time_to=time(12,30),status="reserved",user=user)
            items.append(x)
    return items


@pytest.fixture
def complaint(users, terms):
    items=[]
    for user in users:
        for term in terms:
            for title, description in [("s","skandal"), ("d","dezercja"), ("a","absurd")]:
                c=Complaint.objects.create(title=title, description=description, user=user, term=term)
                items.append(c)
    return items
