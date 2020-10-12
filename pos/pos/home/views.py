from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
def index(req):
	group = req.user.groups.first()
	return render(req, 'home/index.html')

