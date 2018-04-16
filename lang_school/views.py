from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from lang_school.models import LangDetail, LangTitle


class LangSchoolDetail(ListView):
    model = LangTitle
    template_name = 'lang_school/lang_detail.html'
    context_object_name = 'data'


class LangSchoolCreateView(CreateView):
    model = LangDetail
    fields = ('title', 'coach', 'description', 'price', 'discount', 'time_to_class', 'date_to_start',
              'count_students_in_group', 'count_students')
    template_name = 'lang_school/lang_detail_add.html'


class LangSchoolTitleView(CreateView):
    model = LangTitle
    fields = ('name_cours', 'description')
    template_name = 'lang_school/lang_title_add.html'


class LangSchoolDetailUpdateView(UpdateView):
    model = LangDetail
    fields = ('title', 'coach', 'description', 'price', 'discount', 'time_to_class', 'date_to_start',
              'count_students_in_group', 'count_students')
    template_name = 'lang_school/lang_detail_update.html'


class LangSchoolTitleUpdateView(UpdateView):
    model = LangTitle
    fields = ('name_cours', 'description')
    template_name = 'lang_school/lang_title_update.html'
    success_url = reverse_lazy('lang_school_detail')


class LangSchoolDetailDeleteView(DeleteView):
    model = LangDetail
    template_name = 'lang_school/lang_detail_delete.html'
    success_url = reverse_lazy('lang_school_detail')





