from django.forms import ModelForm
from design_school.models import DesignSetGetGroups, DesignDetail, DesignTitle


class DesignDetailForm(ModelForm):
    class Meta:
        model = DesignDetail
        exclude = ['discount']

class DesignTitleForm(ModelForm):
    class Meta:
        model = DesignTitle
        fields = '__all__'



class DesignSetGetGroupsForm(ModelForm):
    class Meta:
        model = DesignSetGetGroups
        fields = '__all__'


