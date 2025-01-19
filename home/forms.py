# forms.py
from django import forms
from .models import Contact, AboutUs


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'subscribe_to_newsletter']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام', 'class': ' peer text-right block min-h-[auto] w-full rounded border border-zinc-300 bg-transparent py-2 px-3 leading-6 outline-none'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل', 'class': 'peer text-right block min-h-[auto] w-full rounded border border-zinc-300 bg-transparent py-2 px-3 leading-6 outline-none'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'متن پیام',
                'class': 'peer block min-h-[auto] w-full rounded border border-zinc-300 bg-transparent py-[0.32rem] px-3 leading-[1.6] outline-none',
                'rows': 4,
                'style': 'resize: none;'
            }),
            'subscribe_to_newsletter': forms.CheckboxInput(attrs={'class': 'relative w-4'}),
        }


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'content', 'order']


