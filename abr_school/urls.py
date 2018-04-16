from django.urls import path
from abr_school.views import ABRSchoolDetail, ABRSchoolCreateView, ABRSchoolTitleView, ABRSchoolDetailUpdateView, ABRSchoolDetailDeleteView, ABRSchoolTitleUpdateView

urlpatterns = [
    path('', ABRSchoolDetail.as_view(), name='abr_school_detail'),
    path('create-det', ABRSchoolCreateView.as_view(), name='abr_school_create_det'),
    path('create-title', ABRSchoolTitleView.as_view(), name='abr_school_create_title'),
    path('update-det/<int:pk>/', ABRSchoolDetailUpdateView.as_view(), name='abr_school_update_det'),
    path('update-title/<int:pk>/', ABRSchoolTitleUpdateView.as_view(), name='abr_school_update_title'),
    path('delete-det/<int:pk>/', ABRSchoolDetailDeleteView.as_view(), name='abr_school_delete_det'),
]