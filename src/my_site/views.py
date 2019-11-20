from django.shortcuts import render

def home_page(request):
	title = "Hi, I'm Eric. Welcome to my site/portfolio."
	message = "Use the link at the top to see some of my projects."
	context = {
		"title" : title,
		"message" : message
		}
	return render(request, "home.html", context)

def about_view(request):
	message = "The tools used to build this site were: Python, Django, Bootstrap, JQuery, CSS, HTML, and JavaScript."
	context = {"message" : message}
	return render(request, "about.html", context)