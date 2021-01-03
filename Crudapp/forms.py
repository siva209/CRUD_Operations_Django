from .models import Student
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean(self,*args,**kwargs):
        print("Is_valid")
        forms.ValidationError("Wrong details")
        return super(StudentForm,self).clean(*args,**kwargs)
