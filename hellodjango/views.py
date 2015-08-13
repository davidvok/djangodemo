from django.http import Http404, HttpResponse
#from django.template.loader import get_template
#from django.template import Context
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("Hello World!")

def current_datetime(request):
	now = datetime.datetime.now()
	#t = get_template('current_datetime.html')
	#html = t.render(Context({'current_date': now}))
	#html = "<html><body>It is now %s.</body></html>" % now
	return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		print "error"
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#html = "<html><body>In %d hour(s), it will be %s.</body></html>" % (offset, dt)
	#return HttpResponse(html)
	return render_to_response('hours_ahead.html',{'hour_offset': offset,'next_time': dt })

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
