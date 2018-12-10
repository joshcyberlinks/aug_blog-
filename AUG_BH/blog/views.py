from django.shortcuts import render
from .models import Post
from blog.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


#our views.
def index(request):
	return render(request, 'blog/index.html', {})
def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			#Email the profile with the contact information
			template = get_template('contact_template.txt')
			context = {
				'contact_name': contact_name,
				'contact_name': contact_name,
				'form_content': form_content,
			}
			content = template.render(context)

			email =EmailMessage(
				"New contact form submission",
				content,
				"my website" + '',
				['hungrypy@gmail.com'],
				headers = {'Reply-to' : contact_email}
				)
			email.send()
			return redirect('contact')


	return render(request, 'blog/contact.html', {
		'form' : form_class
		})
def events(request):
	return render(request, 'blog/events.html', {})
def post1(request):
	return render(request, 'blog/post1.html', {})
def post2(request):
	return render(request, 'blog/post2.html', {})
def post3(request):
	return render(request, 'blog/post3.html', {})