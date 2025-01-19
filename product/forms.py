from django import forms
from home.models import UserAddress
from product.models import Comment


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['first_name', 'last_name', 'province', 'city', 'street', 'building_info', 'phone', 'post_code', 'mail_ticket']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-300 focus:outline-none'}),
            'last_name': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-300 focus:outline-none'}),
            'province': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-500 focus:outline-none'}),
            'city': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-500 focus:outline-none'}),
            'street': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-300 focus:outline-none'}),
            'building_info': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-300 focus:outline-none'}),
            'phone': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-300 focus:outline-none'}),
            'post_code': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-300 focus:outline-none'}),
            'mail_ticket': forms.Textarea(attrs={'placeholder': 'نکات مهم درباره تحویل محصول', 'cols': 30, 'rows': 7, 'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all focus:border-blue-400 focus:outline-none'})
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'product', 'most_sell_product', 'created_at', 'is_verified']