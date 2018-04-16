from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from abr_school.models import ABRDetail, ABRTitle


class ABRSchoolDetail(ListView):
    model = ABRTitle
    template_name = 'abr_school/abr_detail.html'
    context_object_name = 'data'


class ABRSchoolCreateView(CreateView):
    model = ABRDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'abr_school/abr_detail_add.html'


class ABRSchoolTitleView(CreateView):
    model = ABRTitle
    fields = ('name_cours', 'description')
    template_name = 'abr_school/abr_title_add.html'


class ABRSchoolDetailUpdateView(UpdateView):
    model = ABRDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'abr_school/abr_detail_update.html'


class ABRSchoolTitleUpdateView(UpdateView):
    model = ABRTitle
    fields = ('name_cours', 'description')
    template_name = 'abr_school/abr_title_update.html'
    success_url = reverse_lazy('abr_school_detail')


class ABRSchoolDetailDeleteView(DeleteView):
    model = ABRDetail
    template_name = 'abr_school/abr_detail_delete.html'
    success_url = reverse_lazy('abr_school_detail')





