from django.shortcuts import render
from .models import Proj
# Create your views here.

def projects_page(request):
	qs = Proj.objects.all()
	proj_1 = qs[0]
	proj_2 = qs[1]
	proj_3 = qs[2]
	proj_4 = qs[3]
	proj_5 = qs[4]
	proj_6 = qs[5]
	context = {
	'project_list' : qs,
	'proj_1' : proj_1,
	'proj_2' : proj_2,
	'proj_3' : proj_3,
	'proj_4' : proj_4,
	'proj_5' : proj_5,
	'proj_6' : proj_6,
	}
	return render(request, "proj/grid.html", context)