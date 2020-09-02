import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_of_doctors_view(client):
    client.login(username="test_user", password="tester2020")
    response = client.get(reverse("make_appointment1"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_my_appointments_view(client, users):
    client.login(username="test_user", password="tester2020")
    response = client.get(reverse("my_appointments"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_complaint_view(client, users):
    client.login(username="test_user", password="tester2020")
    response = client.get(reverse("complaint"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_of_doctors_view(client, users, doctors):
    client.login(username="test_user", password="tester2020")
    response = client.get(reverse("make_appointment1"))
    assert response.status_code == 200
    ret_doctors = response.context[
        "doctors"]
    assert list(ret_doctors) == doctors


@pytest.mark.django_db
def test_my_appointments_view(client, users, doctors):
    client.login(username="test_user", password="tester2020")
    response = client.get(reverse("my_appointments"))
    assert response.status_code == 200
    ret_doctors = response.context[
        "doctors"]
    assert list(ret_doctors) == doctors


@pytest.mark.django_db
def test_complaint_view(client, users, specialisations):
    client.login(username="test_user", password="tester2020")
    response = client.get(reverse("complaint"))
    assert response.status_code == 200
    ret_specialisations = response.context[
        "objects"]
    assert list(ret_specialisations) == specialisations
