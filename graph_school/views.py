from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from graph_school.models import GraphDetail, GraphTitle


class GraphSchoolDetail(ListView):
    model = GraphTitle
    template_name = 'graph_school/graph_detail.html'
    context_object_name = 'data'


class GraphSchoolCreateView(CreateView):
    model = GraphDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'graph_school/graph_detail_add.html'


class GraphSchoolTitleView(CreateView):
    model = GraphTitle
    fields = ('name_cours', 'description')
    template_name = 'graph_school/graph_title_add.html'


class GraphSchoolDetailUpdateView(UpdateView):
    model = GraphDetail
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students')
    template_name = 'graph_school/graph_detail_update.html'


class GraphSchoolTitleUpdateView(UpdateView):
    model = GraphTitle
    fields = ('name_cours', 'description')
    template_name = 'graph_school/graph_title_update.html'
    success_url = reverse_lazy('graph_school_detail')


class GraphSchoolDetailDeleteView(DeleteView):
    model = GraphDetail
    template_name = 'graph_school/graph_detail_delete.html'
    success_url = reverse_lazy('graph_school_detail')





