from django.shortcuts import render, render_to_response
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    return render(request, "main/home.html")




def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]

    logger.debug(form_data[0]['subject'])
    logger.debug(form_data[1]['sender'])
    logger.debug(form_data[2]['message'])

    send_mail(form_data[0]['subject'], form_data[2]['message'],form_data[1]['sender'], ['johnnycamby@gmail.com'], fail_silently=False)
    return form_data



class ContactWizard(SessionWizardView):
    template_name = 'contact/contactForm.html'
    # **kwargs keyword arguments
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)

        return render('contact/done.html', {'form_data' : form_data})
        #return render_to_response('contact/done.html', {'form_data' : form_data})



