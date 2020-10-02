from django.forms import ModelForm

from . import models

class Prod(ModelForm):
	class Meta:
		model=models.Prod
		exclude=[]