from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import Requester, HardDrive

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