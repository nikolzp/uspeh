from django.urls import path
from ind_school.views import IndSchoolDetail, IndSchoolCreateView, IndSchoolDetailUpdateView, IndSchoolDetailDeleteView

urlpatterns = [
    path('', IndSchoolDetail.as_view(), name='ind_school_detail'),
    path('create-det', IndSchoolCreateView.as_view(), name='ind_school_create_det'),
    path('update-det/<int:pk>/', IndSchoolDetailUpdateView.as_view(), name='ind_school_update_det'),
    path('delete-det/<int:pk>/', IndSchoolDetailDeleteView.as_view(), name='ind_school_delete_det'),
]