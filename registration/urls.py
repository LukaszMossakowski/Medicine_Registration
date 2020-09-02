from django.urls import path
from registration import views

urlpatterns=[
    path("specialisation/",views.SpecialisationView.as_view(), name="specialisation"),
    path("specialisation/modify/<int:pk>/",views.SpecialisationView.as_view(), name="modify_specialisation"),
    path("specialisation/delete/<int:pk>/",views.SpecialisationDeleteView.as_view(), name="delete_specialisation"),
    path("group/",views.GroupView.as_view(), name="group"),
    path("group/modify/<int:pk>/",views.GroupView.as_view(), name="modify_group"),
    path("group/delete/<int:pk>/",views.GroupDeleteView.as_view(), name="delete_group"),
    path("doctor/",views.DoctorView.as_view(), name="manage_doctor"),
    path('doctor/delete/<int:pk>/', views.DoctorDeleteView.as_view(), name="delete_doctor"),
    path("doctor/modify/<int:pk>/",views.DoctorView.as_view(), name="modify_doctor"),
    path("offerterm/",views.TermView.as_view(), name="manage_term"),
    path("offerterm/delete/<int:pk>/",views.TermDeleteView.as_view(), name="delete_term"),
    path("offerterm/modify/<int:pk>/",views.TermView.as_view(), name="modify_term"),
    path("complaint/",views.ComplaintView.as_view(), name="complaint"),
    path("complaint/list",views.ComplaintListView.as_view(), name="complaint_list"),
# --------------------------------------------below system of reservation-----------------------------------------------
    path("make_appointment/",views.ListOfDoctorsView.as_view(), name="make_appointment1"),
    path("make_appointment/terms/<int:pk>/",views.ListOfTermsView.as_view(), name="make_appointment2"),
    path("make_appointment/terms/confirmation/<int:pk>/",views.AppointmentConfirmationView.as_view(), name="make_appointment3"),
    path("my_appointments/",views.MyAppointmentsView.as_view(), name="my_appointments"),
    path("my_appointment/terms/cancel/<int:pk>/", views.DeleteAppointmentView.as_view(), name="delete_appointment"),
# --------------------------------------------below system of relation user to group------------------------------------
    path("group/user_to_group/", views.UserToGroupView.as_view(), name="user_to_group"),
    path("group/user_to_group/delete/<int:pk>/", views.DeleteUserToGroupView.as_view(), name="delete_user_to_group")

]