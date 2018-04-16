from django.urls import path
from lang_school.views import (LangSchoolDetail, LangSchoolCreateView, LangSchoolTitleView, LangSchoolDetailUpdateView, LangSchoolDetailDeleteView, LangSchoolTitleUpdateView)

urlpatterns = [
    path('', LangSchoolDetail.as_view(), name='lang_school_detail'),
    path('create-det', LangSchoolCreateView.as_view(), name='lang_school_create_det'),
    path('create-title', LangSchoolTitleView.as_view(), name='lang_school_create_title'),
    path('update-det/<int:pk>/', LangSchoolDetailUpdateView.as_view(), name='lang_school_update_det'),
    path('update-title/<int:pk>/', LangSchoolTitleUpdateView.as_view(), name='lang_school_update_title'),
    path('delete-det/<int:pk>/', LangSchoolDetailDeleteView.as_view(), name='lang_school_delete_det'),
]