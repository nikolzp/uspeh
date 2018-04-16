from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from design_school.models import DesignDetail, DesignTitle


class DesignSchoolDetail(ListView):
    model = DesignTitle
    template_name = 'design_school/design_detail.html'
    context_object_name = 'data'


class DesignSchoolCreateView(CreateView):
    model = DesignDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'design_school/design_detail_add.html'


class DesignSchoolTitleView(CreateView):
    model = DesignTitle
    fields = ('name_cours', 'description')
    template_name = 'design_school/design_title_add.html'


class DesignSchoolDetailUpdateView(UpdateView):
    model = DesignDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'design_school/design_detail_update.html'


class DesignSchoolTitleUpdateView(UpdateView):
    model = DesignTitle
    fields = ('name_cours', 'description')
    template_name = 'design_school/design_title_update.html'
    success_url = reverse_lazy('design_school_detail')


class DesignSchoolDetailDeleteView(DeleteView):
    model = DesignDetail
    template_name = 'design_school/design_detail_delete.html'
    success_url = reverse_lazy('design_school_detail')





