from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView

from blog.forms import TextForm
from blog.models import Tweeter


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        tweets = Tweeter.objects.all()
        return {
            "tweets": tweets
        }


class TextView(TemplateView):
    template_name = 'texting.html'

    def dispatch(self, request, *args, **kwargs):
        form = TextForm()
        if request.method == 'POST':
            form = TextForm(request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect(reverse('home'))
        return render(request, self.template_name, {'form': form})
