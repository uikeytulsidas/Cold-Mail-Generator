# from django.urls import path
# from . import views

# urlpatterns = [
#     path("/leads/", views.list_leads, name="list-leads"),
#     path("/leads/create/", views.create_lead, name="create-lead"),
#    path("/emails/<int:lead_id>/", views.list_generated_emails, name="list-emails"),

# ]

from django.urls import path
from .views import LeadListCreateView, GeneratedEmailListView, GenerateEmailView

urlpatterns = [
    path("leads/", LeadListCreateView.as_view(), name="lead-list-create"),
    path("emails/", GeneratedEmailListView.as_view(), name="emails-list"),
    path("emails/generate/<int:lead_id>/", GenerateEmailView.as_view(), name="generate-email"),
     path('generate/<int:lead_id>/', GenerateEmailView.as_view(), name='generate-email'),
]

