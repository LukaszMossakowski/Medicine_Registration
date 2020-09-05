from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from registration.forms import SpecialisationForm, GroupForm, DoctorForm, TermForm, ComplaintForm
from registration.models import Specialisation, Doctor, Term, Complaint


class IndexView(View):
    """
    View leading to the mane page with listing of available specialisations and doctors.
    Page available from direct url designed for local host.
    """
    def get(self, request):
        doctors = Doctor.objects.all().order_by("id")
        specialisation_list = list(Specialisation.objects.all().order_by("id"))
        if len(specialisation_list) > 0:
            return render(request, "index.html", {"objects1": specialisation_list[0],
                                                  "objects2": specialisation_list[1:],
                                                  "doctors": doctors})
        return render(request, "index.html")


class SpecialisationView(PermissionRequiredMixin, View):
    """
        View enables addition and modification of medical specialisation available for
        patients in medical center. The "pk" parameter is id of modified specialisation
        which is instance from module "Specialisation". The "pk" parameter is enabled by url.
        Data for new created of modified instance is obtained via the form.
    """
    permission_required = ['registration.specialisation']

    def get(self, request, pk=None):
        specialisation = Specialisation.objects.all().order_by("id")
        specialisation_list = list(specialisation)
        if pk is None:
            form = SpecialisationForm()
        else:
            item = Specialisation.objects.get(pk=pk)
            form = SpecialisationForm(instance=item)
        if len(specialisation_list) > 0:
            return render(request, "manage_specialisation.html", {"form": form, "objects": specialisation,
                                                                  "objects1": specialisation_list[0],
                                                                  "objects2": specialisation_list[1:]})
        else:
            return render(request, "manage_specialisation.html", {"form": form})

    def post(self, request, pk=None):
        if pk is None:
            form = SpecialisationForm(request.POST, request.FILES)
        else:
            item = Specialisation.objects.get(pk=pk)
            form = SpecialisationForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
        return redirect("specialisation")


class DoctorView(PermissionRequiredMixin, View):
    """
        View enables addition and modification of medical staff: "doctor" available for
        patients in medical center. The "pk" parameter is id of modified doctor
        which is instance from module "Doctor". The "pk" parameter is enabled by url.
        Data for new created of modified instance is obtained via the form.
    """
    permission_required = ['registration.doctor']

    def get(self, request, pk=None):
        doctor = Doctor.objects.all().order_by("id")
        if pk is None:
            form = DoctorForm()
        else:
            item = Doctor.objects.get(pk=pk)
            form = DoctorForm(instance=item)
        return render(request, "manage_doctor.html", {"form": form, "objects": doctor})

    def post(self, request, pk=None):
        if pk is None:
            form = DoctorForm(request.POST, request.FILES)
        else:
            doctor = Doctor.objects.get(pk=pk)
            form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("manage_doctor")
        return render(request, "manage_doctor.html", {"form": form})


class GroupView(PermissionRequiredMixin, View):
    """
        View enables addition and modification the groups name of users. In another view: "UserToGroupView"
        the desirable user is assigned to the proper group.
        The "pk" parameter is id of modified group which is instance from module "Group".
        The "pk" parameter is enabled by url. Data for new created of modified instance is obtained via the form.
    """

    permission_required = ['auth.group']

    def get(self, request, pk=None):
        group = Group.objects.all().order_by("id")
        if pk is None:
            form = GroupForm()
        else:
            item = Group.objects.get(pk=pk)
            form = GroupForm(instance=item)
        return render(request, "manage_group.html", {"form": form, "objects": group})

    def post(self, request, pk=None):
        if pk is None:
            form = GroupForm(request.POST)
        else:
            item = Group.objects.get(pk=pk)
            form = GroupForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("group")


class UserToGroupView(LoginRequiredMixin, View):
    def get(self, request, ):
        groups = Group.objects.all().order_by("id")
        users = User.objects.all().order_by("id")
        return render(request, "user_to_group.html", {"users": users, "groups": groups})

    def post(self, request):
        user_id = request.POST.get("user")
        group_id = request.POST.get("group")
        user = User.objects.get(id=user_id)
        user.groups.set(group_id)
        user.is_staff=True
        user.save()
        return redirect("user_to_group")


class TermView(PermissionRequiredMixin, View):
    """
        View enables addition and modification the offered terms of medical appointments available for patients.
        The "pk" parameter is id of modified group which is instance from module "Term".
        The "pk" parameter is enabled by url. Data for new created of modified instance is obtained via the form.
    """

    permission_required = ['registration.term']

    def get(self, request, pk=None):
        term = Term.objects.all()
        doctor = Doctor.objects.all().order_by("id")
        if pk is None:
            form = TermForm()
        else:
            term = Term.objects.get(pk=pk)
            form = TermForm(instance=term)
        return render(request, "manage_term.html", {"form": form, "terms": term, "doctors": doctor})

    def post(self, request, pk=None):
        term = Term.objects.all().order_by("id")
        doctor = Doctor.objects.all().order_by("id")
        if pk is None:
            form = TermForm(request.POST)
        else:
            term = Term.objects.get(pk=pk)
            form = TermForm(request.POST, instance=term)
        if form.is_valid():
            form.save()
            return redirect("manage_term")
        return render(request, "manage_term.html", {"form": form, "terms": term, "doctors": doctor})


class ListOfDoctorsView(LoginRequiredMixin, View):
    def get(self, request):
        doctors = Doctor.objects.all().order_by("id")
        specialisation_list = list(Specialisation.objects.all().order_by("id"))
        if len(specialisation_list) > 0:
            return render(request, "list_of_doctors.html", {"objects1": specialisation_list[0],
                                                  "objects2": specialisation_list[1:],
                                                  "doctors": doctors})
        else:
            return render(request, "list_of_doctors.html", {"doctors": doctors})


class ListOfTermsView(LoginRequiredMixin, View):
    def get(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        terms = Term.objects.filter(doctor=doctor, date__gte=date.today(), status="unreserved").order_by("date", "time_from")
        return render(request, "list_of_terms.html", {"terms": terms, "key": doctor})


class AppointmentConfirmationView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return render(request, "confirm_appointment.html", {"term": Term.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["confirmation"] == "Yes":
            term = Term.objects.get(pk=pk)
            term.status = "reserved"
            term.user = request.user
            term.save()
            return redirect(reverse("my_appointments"))
        return redirect(reverse("make_appointment1"))


class MyAppointmentsView(LoginRequiredMixin, View):
    """
        View enables the patient listing all of the assigned medical appointments (for request.user),
        divided into past ones and waiting for realisation and selecting the proper one for cancelling.
    """
    def get(self, request):
        term = Term.objects.filter(user=request.user).order_by("date")
        term_past = term.filter(date__lt=date.today())
        term_future = term.filter(date__gte=date.today())
        doctors = Doctor.objects.all().order_by("id")
        specialisation_list = list(Specialisation.objects.all().order_by("id"))
        if len(specialisation_list) > 0:
            return render(request, "my_appointments.html", {"terms_past": term_past, "terms_future": term_future,
                                                            "objects1": specialisation_list[0],
                                                            "objects2": specialisation_list[1:],
                                                            "doctors": doctors})
        return render(request, "my_appointments.html", {"terms_past": term_past, "terms_future": term_future, "doctors": doctors})


class ComplaintView(LoginRequiredMixin, View):
    """
        View enables addition the complaints about the past medical appointments available for request.user.
        Data for new created of modified instance is obtained via the form.
    """
    def get(self, request):
        specialisation_list = list(Specialisation.objects.all().order_by("id"))
        specialisation = Specialisation.objects.all().order_by("id")
        form = ComplaintForm(user_=request.user)
        if len(specialisation_list) > 0:
            return render(request, "complaint.html", {"form": form, "objects": specialisation,
                                                      "objects1": specialisation_list[0],
                                                      "objects2": specialisation_list[1:]})
        else:
            return render(request, "complaint.html", {"form": form, "objects": specialisation})

    def post(self, request):
        form = ComplaintForm(request.POST, user_=request.user)
        obj = form.save(commit=False)
        obj.user = request.user
        if form.is_valid():
            obj.save()
            return redirect("complaint")
        return render(request, "complaint.html", {"form": form})


class ComplaintListView(LoginRequiredMixin, View):
    def get(self, request):
        complaints = Complaint.objects.all().order_by("id")
        paginator = Paginator(complaints, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "complaint_list.html", {"page_obj": page_obj, "complaints": complaints})




# --------------------------------- delete section ---------------------------------------

class SpecialisationDeleteView(PermissionRequiredMixin, View):
    """
        View enables deletion the medical specialisation available for patients.
        The "pk" parameter is id of the proper specialisation which is instance from module "Specialisation".
        The "pk" parameter is enabled by url.
    """
    permission_required = ['registration.delete_specialisation']

    def get(self, request, pk):
        return render(request, "delete_specialisation.html", {"obj": Specialisation.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["delete"] == "Yes":
            Specialisation.objects.get(pk=pk).delete()
        return redirect(reverse("specialisation"))


class GroupDeleteView(PermissionRequiredMixin, View):
    """
        View enables deletion the names of groups available for assignment to proper user.
        The "pk" parameter is id of the proper group which is instance from module "Group".
        The "pk" parameter is enabled by url.
    """

    permission_required = ['auth.delete_group']

    def get(self, request, pk):
        return render(request, "delete_group.html", {"obj": Group.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["delete"] == "Yes":
            Group.objects.get(pk=pk).delete()
        return redirect(reverse("group"))


class DoctorDeleteView(PermissionRequiredMixin, View):
    """
        View enables deletion doctors (medical staff) available for patients in medical center.
        The "pk" parameter is id of the doctor which is instance from module "Doctor".
        The "pk" parameter is enabled by url.
    """

    permission_required = ['registration.delete_doctor']

    def get(self, request, pk):
        return render(request, "delete_doctor.html", {"obj": Doctor.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["delete"] == "Yes":
            Doctor.objects.get(pk=pk).delete()
        return redirect(reverse("manage_doctor"))


class TermDeleteView(PermissionRequiredMixin, View):
    """
        View enables deletion the proper term of appointment available for patients in medical center.
        The "pk" parameter is id of the proper term which is instance from module "Term".
        The "pk" parameter is enabled by url.
    """

    permission_required = ['registration.delete_term']

    def get(self, request, pk):
        return render(request, "delete_term.html", {"term": Term.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["delete"] == "Yes":
            Term.objects.get(pk=pk).delete()
        return redirect(reverse("manage_term"))


class DeleteAppointmentView(PermissionRequiredMixin, View):
    """
        View enables deletion by the patient (by the patient panel) the proper term of appointment
        which has ben already reserved by the patient.
        The "pk" parameter is id of the proper term which is instance from module "Term".
        The "pk" parameter is enabled by url.
    """

    permission_required = ['registration.change_term']

    def get(self, request, pk):
        return render(request, "cancel_appointment.html", {"term": Term.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["cancel"] == "Yes":
            term = Term.objects.get(pk=pk)
            term.status = "unreserved"
            term.user = None
            term.save()
        return redirect(reverse("my_appointments"))


class DeleteUserToGroupView(PermissionRequiredMixin, View):
    """
        View enables deletion of the assignment between group and proper user.
        The "pk" parameter is id of the proper relation instance module "user_groups" from auth.model.
        The "pk" parameter is enabled by url.
    """

    permission_required = ['auth.change_user']

    def get(self, request, pk):
        return render(request, "delete_user_to_group.html", {"user": User.objects.get(pk=pk)})

    def post(self, request, pk):
        if request.POST["delete"] == "Yes":
            user = User.objects.get(pk=pk)
            user.groups.set("")
        return redirect(reverse("user_to_group"))
