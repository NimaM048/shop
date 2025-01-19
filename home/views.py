
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from home.forms import ContactForm
from home.models import Product, MostSellProduct, LastProductOffer, BlogPost, ContactInfo, AboutUs, Category


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['product'] = MostSellProduct.objects.all()
        context['producted'] = LastProductOffer.objects.all()
        context['blog_posts'] = BlogPost.objects.all()
        context['category'] = Category.objects.all()
        return context



class ContactUsView(TemplateView):
    template_name = 'home/contact-us.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        contact_info = ContactInfo.objects.first() 
        return render(request, self.template_name, {'form': form, 'contact_info': contact_info})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'پیام شما با موفقیت ثبت شد!'}, status=200)
            return redirect('home:contactus')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'errors': form.errors}, status=400)
        return render(request, self.template_name, {'form': form})



class AboutUsView(TemplateView):
    template_name = 'home/about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us_sections'] = AboutUs.objects.all()
        return context



class QSView(TemplateView):

    template_name = 'home/faq.html'


class RulesView(TemplateView):

    template_name = 'home/rules.html'