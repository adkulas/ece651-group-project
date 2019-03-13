from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path("patientrecords", views.all_patient_records.as_view()),
    path("patientrecords/<int:pk>/", views.patient_record.as_view()),
    path("patientrecords/<str:username>/", views.patient_records_byusername.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)