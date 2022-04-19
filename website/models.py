from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.


# Denise
class Requester(models.Model):
    # at the moment we can delete the relationship with other models for testing purposes
    # a user can be one requester, a requester can be one user
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # Denise
    requester_status_choices = (
        ("Good Standing", "Good Standing"),
        ("Delinquent", "Delinquent"),
        ("Disabled", "Disabled"),
        ("Archived", "Archived"),
    )
    first_name = models.CharField(max_length=100)  # required
    last_name = models.CharField(max_length=100)  # required
    email = models.EmailField(max_length=254, blank=True, null=True)  # required
    direct_supervisor_email = models.EmailField(max_length=254, blank=True, null=True)  # required
    branch_chief_email = models.EmailField(max_length=254, blank=True, null=True)  # required
    requester_status = models.CharField(max_length=50, choices=requester_status_choices,
                                        default=requester_status_choices[0][0])  # required

    def __str__(self):
        full_name = (str(self.first_name), str(self.last_name))
        return " ".join(full_name)


# Denise
class Maintainer(models.Model):
    # at the moment we can delete the relationship with other models for testing purposes
    # a user can be one maintainer, a maintainer can be one user
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # Denise
    maintainer_status_choices = (
        ("Active", "Active"),
        ("Disabled", "Disabled"),
        ("Archived", "Archived"),
    )
    first_name = models.CharField(max_length=100)  # required
    last_name = models.CharField(max_length=100)  # required
    email = models.EmailField(max_length=254, blank=True, null=True)  # required
    maintainer_status = models.CharField(max_length=50, choices=maintainer_status_choices,
                                         default=maintainer_status_choices[0][0])  # required

    def __str__(self):  # uncomment to see default name in /admin
        full_name = (str(self.first_name), str(self.last_name))
        return " ".join(full_name)


# Denise
class Auditor(models.Model):
    # at the moment we can delete the relationship with other models for testing purposes
    # a user can be one auditor, a auditor can be one user
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # Denise
    auditor_status_choices = (
        ("Authorized", "Authorized"),
        ("Unauthorized", "Unauthorized"),
        ("Archived", "Archived"),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, null=True)
    auditor_status = models.CharField(max_length=50, choices=auditor_status_choices,
                                      default=auditor_status_choices[0][0])  # required

    def __str__(self):  # uncomment to see default name in /admin
        full_name = (str(self.first_name), str(self.last_name))
        return " ".join(full_name)


# Denise
class HardDrive(models.Model):
    # Denise
    hard_drive_status_choices = (
        ("Assigned", "Assigned"),
        ("Available", "Available"),
        ("End of Life", "End of Life"),
        ("Master Clone", "Master Clone"),
        ("Pending Wipe", "Pending Wipe"),
        ("Destroyed", "Destroyed"),
        ("Lost", "Lost"),
        ("Overdue", "Overdue"),
        ("Picked Up", "Picked Up"),
        ("Returned", "Returned"),
        ("Pending Change", "Pending Change"),
    )
    # Denise
    justifications_choices = [
        ("Text", "Text"),
        ("File Attachment", "File Attachment"),
    ]
    # Denise
    classification_choices = (
        ("Unclassified", "Unclassified"),
        ("Classified", "Classified"),
    )
    # Denise
    boot_test_status_choices = (
        ("Pass", "Pass"),
        ("Fail", "Fail"),
    )
    size_choices = (
        ("16GB", "16GB"),
        ("32GB", "32GB"),
        ("64GB", "64GB"),
        ("128GB", "128GB"),
        ("256GB", "256GB"),
        ("500GB", "500GB"),
        ("1TB", "1TB"),
        ("1.5TB", "1.5TB"),
        ("2TB", "2TB"),
        ("4TB", "4TB"),
        ("6TB", "6TB"),
        ("8TB", "8TB"),
        ("12TB", "12TB"),
        ("Other", "Other"),
    )
    creation_date = models.DateField(auto_now_add=False, blank=False, null=True)
    serial_number = models.CharField(max_length=100, blank=False, null=False)
    manufacturer = models.CharField(max_length=100, blank=False, null=True)
    model_number = models.CharField(max_length=100, blank=False, null=True)
    type = models.CharField(max_length=50, blank=False, null=True)
    connection_port = models.CharField(max_length=50, blank=False, null=True)
    size = models.CharField(max_length=50, choices=size_choices, blank=False, null=True)
    classification = models.CharField(max_length=50, choices=classification_choices, blank=True, null=True)  # required
    classification_change_justification = models.CharField(max_length=50, choices=justifications_choices,
                                                           default='Text', blank=True, null=True)
    image_version_ID = models.CharField(max_length=50, blank=True, null=True)
    boot_test_status = models.CharField(max_length=50, choices=boot_test_status_choices, default='Pass', blank=True,
                                        null=True)
    boot_test_expiration_date = models.DateField(auto_now_add=False, blank=True, null=True)
    status = models.CharField(max_length=50, choices=hard_drive_status_choices, default='Available')
    hard_drive_status_change_justification = models.CharField(max_length=50, choices=justifications_choices,
                                                              default='Text', blank=True, null=True)
    date_issued = models.DateField(auto_now_add=False, blank=True, null=True)  # required
    expected_return_date = models.DateField(auto_now_add=False, blank=True, null=True)  # required
    hard_drive_return_date_justification = models.CharField(max_length=50, choices=justifications_choices,
                                                            default='Text', blank=True, null=True)
    actual_return_date = models.DateField(auto_now_add=False, blank=True, null=True)  # required
    date_modified = models.DateField(auto_now=False, blank=True, null=True)  # required

    def __str__(self):  # uncomment to see default name in /admin
        details = (str(self.serial_number), str(self.status))
        return " ".join(details)


#Denise
class Amendment(models.Model):
    #Denise
    amendment_Status = (
        #(Actual Value, human-readable name)
        ("Created","Created"),
        ("Approved","Approved"),
        ("Denied","Denied"),
    )

    # (blank=False, null=False) means that it is required
    submissionDate  = models.DateField(auto_now_add=False) #required
    description     = models.FileField(upload_to=None, max_length=100) # double check & required
    decisionDate    = models.DateField(auto_now_add=True) #required
    status          = amendment_Status 
    comment         = models.FileField(upload_to=None, max_length=100) # double check

# Alex
class Event(models.Model):
    
    status_choices = (
        ("Confirmed", "Confirmed"),
        ("Forecasted", "Forecasted"),
        ("Cancelled", "Cancelled"),
    )
    duration_choices = (
        ("10 days", "10 days"),
        ("20 days", "20 days"),
        ("30 days", "30 days"),
        ("40 days", "40 days"),
        ("50 days", "50 days"),
        ("60 days", "60 days"),
    )
    type_choices = (
        ("CVPA", "CVPA"),
        ("VoF", "VoF"),
        ("CVI", "CVI"),
        ("PMR", "PMR"),
        ("Cyber Resilience", "Cyber Resilience"),
        ("Individual Project", "Individual Project"),
        ("Research Project", "Research Project"),
        ("System Acceptance", "System Acceptance"),
        ("Other", "Other"),
    )

    user_choices = (
        ("Vince", "Vince"),
        ("Joshua", "Joshua"),
        ("Dr Cheon", "Dr Cheon"), 
        ("Alexis", "Alexis")
    )

    name = models.CharField(max_length=254)  # required
    location = models.CharField(max_length=254)
    type_of_event = models.CharField(max_length=254, choices=type_choices,
                            default=type_choices[0][0])  # required IT IS STILL PENDING
    status = models.CharField(max_length=254, choices=status_choices, default=status_choices[0][0])  # required
    lead = models.CharField(max_length=254, blank=True, null=True, choices=user_choices, default=user_choices[0][0])
    participants = models.CharField(max_length=254, choices=user_choices, default=user_choices[0][0])
    duration = models.CharField(max_length=254, choices=duration_choices, default=duration_choices[0][0])  # required
    start_date = models.DateField(max_length=254)  # required
    end_date = models.DateField(max_length=254)  # required
    description = models.CharField(max_length=254)  # could be file attachment

    def __str__(self):  # uncomment to see default name in /admin
        details = (str(self.name), str(self.lead))
        return " ".join(details)


# Jacob and Bryant
class Request(models.Model):
    # request will stay in system if Requester is deleting for the moment
    requester = models.ForeignKey(Requester, null=True, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, null=True, on_delete=models.CASCADE)
    hard_drive = models.ManyToManyField(HardDrive)
    # Denise
    status_choices = (
        ("Pending Approval", "Pending Approval"),
        ("Under Review", "Under Review"),
        ("Approved", "Approved"),
        ("Denied", "Denied"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
    )
    receipt_number = models.CharField(max_length=50, blank=False, null=False)  # required
    status = models.CharField(max_length=50, choices=status_choices, blank=False, null=False)  # required
    creation_date = models.DateField(max_length=254)  # required
    data_of_last_modification = models.DateField(max_length=254)  # required
    need_hard_drives_by_date = models.DateField(max_length=254)  # required
    number_of_classified_hard_drives_needed = models.PositiveIntegerField(default=0)  # required
    number_of_unclassified_hardDrives_needed = models.PositiveIntegerField(default=0)  # required
    comment = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):  # uncomment to see default name in /admin
        details = (str(self.receipt_number), str(self.status))
        return " ".join(details)

#Alex
class HardDriveRequest(models.Model):
    types_of_classification = (
        ("Classified", "Classified"),
        ("Unclassified", "Unclassified"),
    )

    hd_type_choices = (
        ("Slow Hard Drive", "Slow Hard Drive"),
        ("Fast Hard Drive", "Fast Hard Drive"),
        ("Low-Capacity Drive", "Low-Capacity Drive"),
        ("Fast-Capacity Drive", "Fast-Capacity Drive"),
    )

    port_choices = (
        ("SATA", "SATA"),
        ("M.2", "M.2"),
    )

    size_choices = (
        ("16GB", "16GB"),
        ("32GB", "32GB"),
        ("64GB", "64GB"),
        ("128GB", "128GB"),
        ("256GB", "256GB"),
        ("500GB", "500GB"),
        ("1TB", "1TB"),
        ("1.5TB", "1.5TB"),
        ("2TB", "2TB"),
        ("4TB", "4TB"),
        ("6TB", "6TB"),
        ("8TB", "8TB"),
        ("12TB", "12TB"),
        ("Other", "Other"),
    )

    hd_classification = models.CharField(max_length=50, choices=types_of_classification, blank=False, null=False, default=types_of_classification[0][0])
    amount_required = models.PositiveIntegerField(default=0)
    connection_port = models.CharField(max_length=50, choices=port_choices, blank=False, null=False, default=port_choices[0][0])
    hd_size = models.CharField(max_length=50, choices=size_choices, blank=False, null=False, default=size_choices[0][0])
    type_of_hd = models.CharField(max_length=50, choices=hd_type_choices, blank=False, null=False, default=hd_type_choices[0][0])
    comment = models.CharField(max_length=360, blank=True, null=True)

    def __str__(self):  # uncomment to see default name in /admin
        details = (str(self.hd_classification), str(self.amount_required))
        return " ".join(details)

# Jacob
class UserProfile(models.Model):
    user_role_choices = (
        ("Requestor", "Requestor"),
        ("Auditor", "Auditor"),
        ("Maintainer", "Maintainer"),
        ("Admin", "Admin"),
    )
    
    user_profile_status_choices = (
        ("Pending", "Pending"),
        ("Active", "Active"),
        ("Disabled", "Disabled"),
        ("Archived", "Archived"),
    )
    
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email_address = models.EmailField(max_length=100, blank=False, null=False)
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    user_role = models.CharField(max_length=50, choices=user_role_choices, blank=False, null=False)
    direct_supervisors_email = models.EmailField(max_length=100, blank=False, null=False)
    branch_chiefs_email = models.EmailField(max_length=100, blank=False, null=False)
    user_profile_status = models.CharField(max_length=50, choices=user_profile_status_choices, blank=False, null=False)
    last_modified_date = models.DateField(blank=False, null=False)

# Miriam & Jacob
class DriveInventoryThresholdConfiguration(models.Model):
    drive_inventory_threshold_choices = (
        ("Unclassified", "Unclassified"),
        ("Classified", "Classified"),
    )
    
    threshold_level = models.CharField(max_length=50, blank=False, null=False)
    threshold_value = models.PositiveIntegerField(blank=False, null=False)
    drive_inventory_threshold = models.CharField(max_length=50, choices=drive_inventory_threshold_choices, blank=False, null=False)

# Miriam & Jacob
class EventConfiguration(models.Model):
    event_type_name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    length_of_reporting_cycle = models.PositiveIntegerField(blank=False, null=False)
    drive_limit = models.PositiveIntegerField(blank=False, null=False)

# Miriam & Jacob
class ForecastedRequestNotificationThresholdConfiguration(models.Model):
    event_type = models.ForeignKey(EventConfiguration, on_delete=models.CASCADE, to_field='event_type_name', blank=False, null=False)
    threshold_level = models.CharField(max_length=50, blank=False, null=False)
    threshold_value = models.PositiveIntegerField(blank=False, null=False)

# Miriam & Jacob
class DelinquencyNotificationForOverdueHardDriveThresholdConfiguration(models.Model):
    notifyee_choices = (
        ("Requestor", "Requestor"),
        ("Maintainer", "Maintainer"),
        ("Direct Supervisor", "Direct Supervisor"),
        ("Branch Chief", "Branch Chief"),
    )
    
    event_type = models.ForeignKey(EventConfiguration, on_delete=models.CASCADE, to_field='event_type_name', blank=False, null=False)
    notifyee = models.CharField(max_length=50, choices=notifyee_choices, blank=False, null=False)
    threshold_level = models.CharField(max_length=50, blank=False, null=False)
    threshold_value = models.PositiveIntegerField(blank=False, null=False)


#Miriam
class LogAction(models.Model):
    actionPerformed = models.CharField(max_length=254)  # required
    timestampp = models.TimeField(max_length=254)  # required

    def __str__(self):  # uncomment to see default name in /admin
        details = (str(self.name), str(self.lead))
        return " ".join(details)