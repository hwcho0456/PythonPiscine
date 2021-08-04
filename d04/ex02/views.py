from d04.settings import LOG
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .form import MyForm
from datetime import datetime

# Create your views here.
class Ex02(TemplateView):
    template_name = "ex02/index.html"
    def get(self, request):
        form = MyForm()
        history = []
        try:
            with open(LOG, 'r') as file:
                history = file.readlines() 
        except:
            pass
        return render(request, self.template_name, {'form': form, 'history': history})
    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            timestamp = datetime.now()
            with open(LOG, 'a') as file:
                file.write("{} {}\n".format(form.cleaned_data['text'], timestamp))
        return redirect('/ex02')