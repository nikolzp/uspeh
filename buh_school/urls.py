from django.urls import path
from buh_school.views import BuhSchoolDetail, BuhSchoolCreateView, BuhSchoolTitleView, BuhSchoolDetailUpdateView, BuhSchoolDetailDeleteView, BuhSchoolTitleUpdateView

urlpatterns = [
    path('', BuhSchoolDetail.as_view(), name='buh_school_detail'),
    path('create-det', BuhSchoolCreateView.as_view(), name='buh_school_create_det'),
    path('create-title', BuhSchoolTitleView.as_view(), name='buh_school_create_title'),
    path('update-det/<int:pk>/', BuhSchoolDetailUpdateView.as_view(), name='buh_school_update_det'),
    path('update-title/<int:pk>/', BuhSchoolTitleUpdateView.as_view(), name='buh_school_update_title'),
    path('delete-det/<int:pk>/', BuhSchoolDetailDeleteView.as_view(), name='buh_school_delete_det'),
]