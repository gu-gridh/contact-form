from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    """
    /contact
    - If headless frontend with e.g. Vue is used, return a 404
    - If templates are used, serve Django form
    """
    if getattr(settings, 'USE_HEADLESS_FRONTEND', False):
        return HttpResponseNotFound("Handled by frontend.")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'gridh_contact_forms/contact_form.html', {
                'form': ContactForm(), 'success': True
            })
        return render(request, 'gridh_contact_forms/contact_form.html',
                      {'form': form})

    return render(request, 'gridh_contact_forms/contact_form.html',
                  {'form': ContactForm()})


def contact_template_only_view(request):
    """
    /pages/contact.html — always renders template version
    """
    form = ContactForm()
    return render(request, 'gridh_contact_forms/contact_form.html',
                  {'form': form})
