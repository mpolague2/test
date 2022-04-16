from django.urls import path
from . import views

urlpatterns = [

    # shared urls
    ################################################################
    path('', views.base),
    path('base/', views.base, name='base'),
    path('registerPage/', views.registerPage, name='registerPage'),
    path('loginPage/', views.loginPage, name="loginPage"),
    path('logoutUser/', views.logoutUser, name="logoutUser"),
    
    # requester urls
    ################################################################
    path('base_requester/', views.requester, name='requester'),
    path('requester_requests/', views.requester_requests, name='r_requests'),
    path('requester_messages/', views.requester_messages, name='r_messages'),
    path('requester_inventory/', views.requester_inventory, name='r_inventory'),
    path('add_request/', views.add_requests),
    path('requester_profile/', views.requester_profile, name='r_profile'),
    path('amendment_requester/', views.amendment_requester, name='amendment_requester'),#added
    path('metadata_requester/', views.metadata_requester, name='metadata_requester'),#added

    # maintainer urls
    ################################################################
    path('base_maintainer/', views.maintainer, name='maintainer'),
    path('maintainer_requests/', views.maintainer_requests, name='m_requests'),
    path('maintainer_hard_drives/',views.maintainer_hard_drives, name='m_hard_drives'),
    path('maintainer_messages/', views.maintainer_messages, name='m_messages'),
    path('maintainer_reports/', views.maintainer_reports, name='m_reports'),
    path('amendment_maintainer/', views.amendment_maintainer, name='amendment'),#added
    path('metadata_maintainer/', views.metadata_maintainer, name='metadata_maintainer'),#added
    path('maintainer_configurations/',
         views.maintainer_configurations, name='m_configurations'),
    path('maintainer_inventory/', views.maintainer_inventory, name='m_inventory'),

    # auditor urls
    ################################################################
    path('base_auditor/', views.auditor, name='auditor'),
    path('auditor_hard_drives/', views.auditor_hard_drives, name='a_hard_drives'),
    path('auditor_messages/', views.auditor_messages, name='a_messages'),
    path('auditor_reports/', views.auditor_reports, name='a_reports'),

    # admin urls
    path('admin_profile/', views.admin_profile, name='a_profile'),

    #not sure schedulereports
    
    
    path('schedulereports/', views.schedulereports, name='schedulereports'),#added


]
