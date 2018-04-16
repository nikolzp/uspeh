from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from pc_school.models import PCDetail, PCTitle

class PCSchoolDetail(ListView):
    model = PCTitle
    template_name = 'pc_school/pc_detail.html'
    context_object_name = 'data'


class PCSchoolCreateView(CreateView):
    model = PCDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'pc_school/pc_detail_add.html'


class PCSchoolTitleView(CreateView):
    model = PCTitle
    fields = ('name_cours', 'description')
    template_name = 'pc_school/pc_title_add.html'


class PCSchoolDetailUpdateView(UpdateView):
    model = PCDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'pc_school/pc_detail_update.html'


class PCSchoolTitleUpdateView(UpdateView):
    model = PCTitle
    fields = ('name_cours', 'description')
    template_name = 'pc_school/pc_title_update.html'
    success_url = reverse_lazy('pc_school_detail')


class PCSchoolDetailDeleteView(DeleteView):
    model = PCDetail
    template_name = 'pc_school/pc_detail_delete.html'
    success_url = reverse_lazy('pc_school_detail')





