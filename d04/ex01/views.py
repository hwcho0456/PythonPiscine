from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404

# Create your views here.
class Ex01(TemplateView):
    def get(self, request, template):
        self.template_name = "ex01/{}.html".format(template)
        if self.template_name not in ["ex01/django.html", "ex01/display.html", "ex01/templates.html"]:
            raise Http404
        return render(request, self.template_name)