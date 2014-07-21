from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
import logging
from forms import PasteForm
from django.template.context import RequestContext

from api.models import Snippet, User
# I have no idea what I'm doingggg.
def home(request):
    if request.method == 'POST':
        logging.info(request.POST)
        print request.POST
        form = PasteForm(request.POST)
        if form.is_valid():
            guest = User.objects.get_or_create(username='guest')[0]
            Snippet.objects.create(owner=guest,title=request.POST['title'],
                                   language=request.POST['language'],code=request.POST['snippet'])

            return HttpResponseRedirect(reverse('home'))
    else:
        form = PasteForm()
    template = "paste.html"
    return render_to_response(template,{'form': form},
        context_instance=RequestContext(request))
