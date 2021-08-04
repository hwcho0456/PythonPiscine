from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Ex00(TemplateView):
    template_name = 'ex00/index.html'
    def get(self, request):
        return render(request, self.template_name)