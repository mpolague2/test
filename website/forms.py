from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

class HardDriveForm(ModelForm):
    class Meta:
        model = HardDrive
        fields = [
            'creation_date',
            'serial_number',
            'manufacturer',
            'model_number',
            'type',
            'connection_port',
            'size',
            'classification',
            'classification_change_justification',
            'image_version_ID',
            'boot_test_status',
            'boot_test_expiration_date',
            'status',
            'hard_drive_status_change_justification',
            'date_issued',
            'expected_return_date',
            'hard_drive_return_date_justification',
            'actual_return_date',
        ]

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_event': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'participants': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class HardDriveRequestForm(ModelForm):
    class Meta:
        model = HardDriveRequest
        fields = "__all__"

        widgets = {
            'hd_classification': forms.Select(attrs={'class': 'form-control'}),
            'amount_required': forms.NumberInput(attrs={'class': 'form-control'}),
            'connection_port': forms.Select(attrs={'class': 'form-control'}),
            'hd_size': forms.Select(attrs={'class': 'form-control'}),
            'type_of_hd': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
            
        }   