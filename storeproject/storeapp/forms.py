from django import forms
# from multiselectfield import MultiSelectField

# creating a form

from django.forms import ModelForm, NumberInput

from .models import Person, Courses
# from .models import Materials_provide

# class ClassNameForm(forms.ModelForm):



	# class Meta:
	# 	model = Materials_provide
	# 	fields = ['materials_provide', ]

# class CustomMMCF(forms.ModelMultipleChoiceField):
#     def label_from_instance(self,materials):
#         return  materials.name
# create a ModelForm





class  PersonCreationForm(forms.ModelForm):
	# specify the name of model to use
	MATERIAL_CATEGORIES = (
		('note book', 'Note Book'),
		('pens', 'Pens'),
		('highlighters', 'Highlighters'),
		('Ruler', 'Ruler'),
		('Stapler staples', 'Stapler staples'),
		('Glue', 'Glue'),
		('Scissors', 'Scissors'),
	)

	DOB = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	materials_provide=forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,
            choices = MATERIAL_CATEGORIES
    )

	# materials_provide = forms.ModelMultipleChoiceField(queryset=Materials_provide.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
	class Meta:
		model=Person
		fields = '__all__'





	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['courses'].queryset = Courses.objects.none()
		if 'department' in self.data:
			try:
				department_id = int(self.data.get('department'))
				self.fields['courses'].queryset = Courses.objects.filter(department_id=department_id).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['courses'].queryset = self.instance.department.courses_set.order_by('name')

#
