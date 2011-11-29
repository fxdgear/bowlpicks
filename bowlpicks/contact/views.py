from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import mail_admins, BadHeaderError
from django.template import Context
from django.template.loader import get_template


from bowlpicks.contact.forms import ContactForm


def contactview(request):
    name = request.POST.get('name', '')
    subject = request.POST.get('topic', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    if name and message and from_email:
        t = get_template('contact_message.txt')
        c = Context({'name': name, 'from_email': from_email, 'message': message})
        email_message = t.render(c)
        try:
            mail_admins(subject, email_message)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thankyou/')
    else:
        return render_to_response('contact/contacts.html', {'form': ContactForm()},
            RequestContext(request))

    return render_to_response('contact/contacts.html', {'form': ContactForm()},
        RequestContext(request))


def thankyou(request):
    return render_to_response('contact/thankyou.html', RequestContext(request))
