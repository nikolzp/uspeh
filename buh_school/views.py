from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from buh_school.models import BuhDetail, BuhTitle


class BuhSchoolDetail(ListView):
    model = BuhTitle
    template_name = 'buh_school/buh_detail.html'
    context_object_name = 'data'


class BuhSchoolCreateView(CreateView):
    model = BuhDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'buh_school/buh_detail_add.html'


class BuhSchoolTitleView(CreateView):
    model = BuhTitle
    fields = ('name_cours', 'description')
    template_name = 'buh_school/buh_title_add.html'


class BuhSchoolDetailUpdateView(UpdateView):
    model = BuhDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'buh_school/buh_detail_update.html'


class BuhSchoolTitleUpdateView(UpdateView):
    model = BuhTitle
    fields = ('name_cours', 'description')
    template_name = 'buh_school/buh_title_update.html'
    success_url = reverse_lazy('buh_school_detail')


class BuhSchoolDetailDeleteView(DeleteView):
    model = BuhDetail
    template_name = 'buh_school/buh_detail_delete.html'
    success_url = reverse_lazy('buh_school_detail')

