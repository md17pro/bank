from django import forms

from shop.models import Person, Course


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        # fields = '__all__'
        fields = ('name','dob','age','gender','phone','mail','address','department','course','purpose','debit_notebook', 'pen', 'exam_papers')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')

# class DetailForm(forms.ModelForm):
#     class Meta:
#         model = Details
#         fields = '__all__'
