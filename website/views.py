from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm, HardDriveRequestForm, LoginForm, EventForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'pages/base.html')

@unauthenticated_user
def registerPage(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()

            group = Group.objects.get(name='requester')
            user.groups.add(group)
            Requester.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
            )
            Maintainer.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
            )
            Auditor.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
            )

            # redirect to login following registration
            return redirect('loginPage')

    context = {
        'register_form': register_form
    }
    return render(request, 'pages/registerPage.html', context)


@unauthenticated_user
def loginPage(request):
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
    context = {
        'login_form': login_form
    }
    return render(request, 'pages/loginPage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('base')


# requester views
################################################################
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'requester'])
def requester(request):
    if request.user.groups.filter(name='admin').exists():
        my_requests = Request.objects.all()
    else:
        my_requests = request.user.requester.request_set.all()
    context = {
        'my_requests': my_requests
    }
    return render(request, 'pages/base_requester.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'requester'])
def requester_requests(request):
    return render(request, 'pages/requester_requests.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['requester', 'admin'])
def requester_profile(request):
    return render(request, 'pages/requester_profile.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def admin_profile(request):
    return render(request, 'pages/admin_profile.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'requester'])
def add_requests(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        rform = HardDriveRequestForm(request.POST)
        if form.is_valid() or rform.is_valid():
            form.save()
            rform.save()
            return HttpResponseRedirect('/add_request/')

    form = EventForm
    rForm = HardDriveRequestForm
    return render(request, 'pages/add_request.html', {'form': form, 'rForm': rForm})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'requester'])
def requester_messages(request):
    return render(request, 'pages/requester_messages.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'requester'])
def requester_inventory(request):
    hard_drives_object = HardDrive.objects.all()
    labels = ["Available", "Unavailable"]
    c_data = [0, 0]
    classified_drives = HardDrive.objects.filter(
        classification__iexact="classified")
    for drive in classified_drives:
        if drive.status == "Available":
            c_data[0] += 1
        else:
            c_data[1] += 1
    u_data = [0, 0]
    unclassified_drives = HardDrive.objects.filter(
        classification__iexact="unclassified")
    for drive in unclassified_drives:
        if drive.status == "Available":
            u_data[0] += 1
        else:
            u_data[1] += 1
    context = {
        'hard_drives': hard_drives_object,
        'labels': labels,
        'c_data': c_data,
        'u_data': u_data
    }
    return render(request, 'pages/requester_inventory.html', context)

# maintainer views
################################################################


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer(request):
    requesters = Requester.objects.all()
    maintainers = Maintainer.objects.all()
    auditors = Auditor.objects.all()
    requests = Request.objects.all()
    events = Event.objects.all()
    hard_drives = HardDrive.objects.all()
    requester_group = Group.objects.get(name="requester").user_set.all()
    maintainer_group = Group.objects.get(name="maintainer").user_set.all()
    auditor_group = Group.objects.get(name="auditor").user_set.all()


    #Added by Miriam. Changes made on 4/11/2022
    drive_inv_thresh_config = DriveInventoryThresholdConfiguration.objects.all()
    forecasted_req_not_thresh = ForecastedRequestNotificationThresholdConfiguration.objects.all()
    delinquency_not_overdue = DelinquencyNotificationForOverdueHardDriveThresholdConfiguration.objects.all()
    event_config = EventConfiguration.objects.all()
    log_action = LogAction.objects.all()

    context = {
        'requesters': requesters,
        'maintainers': maintainers,
        'auditors': auditors,
        'requests': requests,
        'events': events,
        'hard_drives': hard_drives,
        'requester_group': requester_group,
        'maintainer_group': maintainer_group,
        'auditor_group': auditor_group,


        #Added by Miriam. Changes made on 4/11/2022
        'drive_inv_thresh_config': drive_inv_thresh_config,
        'forecasted_req_not_thresh': forecasted_req_not_thresh,
        'delinquency_not_overdue': delinquency_not_overdue,
        'event_config': event_config,
        'log_action': log_action,
    }
    return render(request, 'pages/base_maintainer.html', context)

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer_reports(request):
    return render(request, 'pages/maintainer_logPage.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer_requests(request):
    return render(request, 'pages/maintainer_requests.html', {})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer_hard_drives(request):
    hard_drives_object = HardDrive.objects.all()
    context = {
        'hard_drives': hard_drives_object
    }
    return render(request, 'pages/maintainer_hard_drives.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer_messages(request):
    return render(request, 'pages/maintainer_messages.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer_reports(request):
    return render(request, 'pages/maintainer_reports.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])
def maintainer_configurations(request):
    return render(request, 'pages/maintainer_configurations.html')

@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'maintainer'])

def maintainer_logPage(request):
    return render(request, 'pages/maintainer_logPage.html')

def maintainer_inventory(request):
    hard_drives_object = HardDrive.objects.all()
    labels = ["Available", "Unavailable"]
    c_data = [0, 0]
    classified_drives = HardDrive.objects.filter(
        classification__iexact="classified")
    for drive in classified_drives:
        if drive.status == "Available":
            c_data[0] += 1
        else:
            c_data[1] += 1
    u_data = [0, 0]
    unclassified_drives = HardDrive.objects.filter(
        classification__iexact="unclassified")
    for drive in unclassified_drives:
        if drive.status == "Available":
            u_data[0] += 1
        else:
            u_data[1] += 1
    context = {
        'hard_drives': hard_drives_object,
        'labels': labels,
        'c_data': c_data,
        'u_data': u_data
    }
    return render(request, 'pages/maintainer_inventory.html', context)

# auditor views
################################################################
@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'auditor'])
def auditor(request):
    return render(request, 'pages/base_auditor.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'auditor'])
def auditor_hard_drives(request):
    hard_drives_object = HardDrive.objects.all()
    context = {
        'hard_drives': hard_drives_object
    }
    return render(request, 'pages/auditor_hard_drives.html', context)


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'auditor'])
def auditor_messages(request):
    return render(request, 'pages/auditor_messages.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'auditor'])
def auditor_reports(request):
    return render(request, 'pages/auditor_reports.html')


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin', 'auditor'])
def auditor_reports(request):
    return render(request, 'pages/auditor_logPage.html')




# Test View (Not sure)
################################################################
@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def amendment_requester(request):
    return render(request, 'pages/amendment_requester.html')

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def amendment_maintainer(request):
    return render(request, 'pages/amendment_maintainer.html')

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def amendment_maintainer(request):
    return render(request, 'pages/amendment_maintainer.html')

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def metadata_requester(request):
    return render(request, 'pages/metadata_requester.html')

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def metadata_maintainer(request):
    return render(request, 'pages/metadata_maintainer.html')

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def schedulereports(request):
    return render(request, 'pages/schedulereports.html')

@login_required(login_url='loginPage')
#@allowed_users(allowed_roles=['requester', 'maintainer'])
def buildreport(request):
    return render(request, 'pages/buildreport.html')

#in order to add a page need to alter the view and then urls page
#views defines the html page for urls to display
