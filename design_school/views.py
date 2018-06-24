from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from design_school.forms import DesignDetailForm, DesignSetGetGroupsForm, DesignTitleForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from design_school.models import DesignDetail, DesignTitle, DesignSetGetGroups


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
    fields = ('title', 'coach', 'price', 'price_month', 'discount', 'mode', 'time_to_class', 'date_to_start', 'count_students','set_or_work')
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


def group(request, pk):
    edit = DesignSetGetGroups.objects.get(id=pk)
    det = DesignDetail.objects.get(design_detail=pk)
    if request.method == "POST":
        # design_det = DesignDetailForm(request.POST, instance=det)
        design_set_get = DesignSetGetGroupsForm(request.POST, instance=edit)
        if design_set_get.is_valid():
            design_set_get.save()
            # design_det.save()
            return redirect('design_school_detail')

    else:
        design_set_get = DesignSetGetGroupsForm(instance=edit)
        design_det = DesignDetail.objects.get(design_detail=pk)
    return render(request, 'design_school/group.html', {'design_det': design_det, 'design_set_get': design_set_get})


class DesignSchoolGroupDetView(ListView):
    model = DesignSetGetGroups
    fields = ('info_course', 'fio', 'date_add', 'phone', 'email', 'discount', 'note')
    template_name = 'design_school/group_det.html'
    context_object_name = 'group'

    def get_queryset(self):
        a = self.request.GET.get('info_course_id')
        design_det = DesignSetGetGroups.objects.all()
        print(a)

        return design_det









