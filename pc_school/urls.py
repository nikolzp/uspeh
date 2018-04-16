from django.urls import path
from pc_school.views import PCSchoolDetail, PCSchoolCreateView, PCSchoolTitleView, PCSchoolDetailUpdateView, PCSchoolDetailDeleteView, PCSchoolTitleUpdateView

urlpatterns = [
    path('', PCSchoolDetail.as_view(), name='pc_school_detail'),
    path('create-det', PCSchoolCreateView.as_view(), name='pc_school_create_det'),
    path('create-title', PCSchoolTitleView.as_view(), name='pc_school_create_title'),
    path('update-det/<int:pk>/', PCSchoolDetailUpdateView.as_view(), name='pc_school_update_det'),
    path('update-title/<int:pk>/', PCSchoolTitleUpdateView.as_view(), name='pc_school_update_title'),
    path('delete-det/<int:pk>/', PCSchoolDetailDeleteView.as_view(), name='pc_school_delete_det'),
]