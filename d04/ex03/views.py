from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Ex03(TemplateView):
    template_name = 'ex03/index.html'
    def get(self, request):
        self.context = {
            "shade": ["{:02X}".format(int(i*255/50)) for i in range(50,0,-1)]
        }
        return render(request, self.template_name, self.context)
