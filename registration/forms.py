from django import forms
from datetime import date
from django.contrib.auth.models import Group
from registration.models import Specialisation, Doctor, Term, Complaint
# from .widgets import BootstrapDateTimePickerInput

class SpecialisationForm(forms.ModelForm):
    class Meta:
        model = Specialisation
        fields = "__all__"
        widgets = {
            'specialisation': forms.TextInput(attrs={'placeholder': 'name of specialisation', 'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'description of specialisation', 'required': True})
        }


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'group name', 'required': True})
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {
            'medical_title': forms.TextInput(attrs={'placeholder': 'medical title', 'required': True}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first name', 'required': True}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name', 'required': True}),
            'specialisation': forms.CheckboxSelectMultiple()
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        gr = Group.objects.get(name='doctor')
        self.fields['user'].queryset =gr.user_set.all()


class TermForm(forms.ModelForm):
    def clean(self):
        clean_data = super().clean()
        if clean_data['time_from'] >= clean_data['time_to']:
            raise forms.ValidationError("Beginning time of proposed appointment is equal to or over ending time.")
        offerterm = Term.objects.filter(doctor=clean_data.get('doctor'),
                                        date=clean_data.get('date'),
                                        time_to__gt=clean_data.get('time_from'),
                                        time_from__lt=clean_data.get('time_to'))
        if offerterm.count() >= 1:
            raise forms.ValidationError('The proposed term has been already proposed. Please offer another term.')

    class Meta:
        model = Term
        fields = "__all__"
        exclude = ["status", "user"]
        # widgets = {
        #     'date': forms.BootstrapDateTimePickerInput(attrs={'required': True})
        # }


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = "__all__"
        exclude = ["user"]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'complaint title', 'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'descrition of your complaint', 'required': True})
        }

    def __init__(self, *args, user_=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["term"].queryset = Term.objects.filter(user=user_, date__lte=date.today())

