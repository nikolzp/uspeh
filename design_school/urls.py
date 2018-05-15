from django.urls import path
from design_school.views import DesignSchoolDetail, DesignSchoolCreateView, DesignSchoolTitleView, DesignSchoolDetailUpdateView, DesignSchoolDetailDeleteView, DesignSchoolTitleUpdateView, group

urlpatterns = [
    path('', DesignSchoolDetail.as_view(), name='design_school_detail'),
    path('create-det', DesignSchoolCreateView.as_view(), name='design_school_create_det'),
    path('create-title', DesignSchoolTitleView.as_view(), name='design_school_create_title'),
    path('update-det/<int:pk>/', DesignSchoolDetailUpdateView.as_view(), name='design_school_update_det'),
    path('update-title/<int:pk>/', DesignSchoolTitleUpdateView.as_view(), name='design_school_update_title'),
    path('delete-det/<int:pk>/', DesignSchoolDetailDeleteView.as_view(), name='design_school_delete_det'),
    path('group/<int:pk>/', group, name='group'),

]