from django.urls import path
from graph_school.views import GraphSchoolDetail, GraphSchoolCreateView, GraphSchoolTitleView, GraphSchoolDetailUpdateView, GraphSchoolDetailDeleteView, GraphSchoolTitleUpdateView

urlpatterns = [
    path('', GraphSchoolDetail.as_view(), name='graph_school_detail'),
    path('create-det', GraphSchoolCreateView.as_view(), name='graph_school_create_det'),
    path('create-title', GraphSchoolTitleView.as_view(), name='graph_school_create_title'),
    path('update-det/<int:pk>/', GraphSchoolDetailUpdateView.as_view(), name='graph_school_update_det'),
    path('update-title/<int:pk>/', GraphSchoolTitleUpdateView.as_view(), name='graph_school_update_title'),
    path('delete-det/<int:pk>/', GraphSchoolDetailDeleteView.as_view(), name='graph_school_delete_det'),
]