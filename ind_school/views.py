from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ind_school.models import IndDetails


class IndSchoolDetail(ListView):
    model = IndDetails
    template_name = 'ind_school/ind_detail.html'
    context_object_name = 'data'


class IndSchoolCreateView(CreateView):
    model = IndDetails
    fields = ('title', 'coach', 'price', 'des_hours')
    template_name = 'ind_school/ind_detail_add.html'


class IndSchoolDetailUpdateView(UpdateView):
    model = IndDetails
    fields = ('title', 'coach', 'price', 'des_hours')
    template_name = 'ind_school/ind_detail_update.html'


class IndSchoolDetailDeleteView(DeleteView):
    model = IndDetails
    template_name = 'ind_school/ind_detail_delete.html'
    success_url = reverse_lazy('ind_school_detail')





