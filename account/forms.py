from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from account.models import User, Profile
from django.utils.translation import gettext_lazy as _

class OtpForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "placeholder:text-right text-sm block w-full rounded-md border border-gray-300 px-3 py-3 font-normal text-gray-700 outline-none transition-all focus:border-blue-500 focus:outline-none",
            'placeholder': "شماره تماس خود را وارد کنید"
        }),
        validators=[RegexValidator(
            regex=r'^\d{10,11}$',
            message='شماره تماس باید 10 یا 11 رقم باشد',
            code='invalid_phone_number'
        )]
    )



class CheckOtp(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "placeholder:text-right text-sm block w-full rounded-md border border-gray-300 px-3 py-3 font-normal text-gray-700 outline-none transition-all focus:border-blue-500 focus:outline-none",
            'placeholder': "کد را وارد کنید"
        }),
        validators=[RegexValidator(
            regex=r'^\d{4}$',
            message='کد وارد شده باید 4 رقمی باشد',
            code='invalid_otp_code'
        )]
    )




class FormRegister(forms.Form):
    fullname = forms.CharField(label='نام کاربری', max_length=150)  # Persian label
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)  # Persian label
    password_confirm = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput)  # Persian label
    phone = forms.CharField(label='شماره تلفن', max_length=11)  # Persian label

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')

        if not fullname.isalnum():
            raise ValidationError("نام کاربری باید فقط شامل حروف و اعداد باشد.")
        if User.objects.filter(fullname=fullname).exists():
            raise ValidationError("نام کاربری وارد شده قبلا ثبت شده است.")
        return fullname

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')


        if len(phone) != 11 or not phone.isdigit():
            raise ValidationError(_("لطفا شماره تماس معتبر وارد کنید."))


        if User.objects.filter(phone=phone).exists():
            raise ValidationError(_("این شماره تماس قبلاً ثبت شده است."))

        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "رمز عبور با تایید رمز عبور مطابقت ندارد.")

    def __init__(self, *args, **kwargs):
        super(FormRegister, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                                                       'class': 'placeholder:text-right text-sm block w-full rounded-md border border-gray-300 px-3 py-3 font-normal text-gray-700 outline-none transition-all focus:border-blue-500 focus:outline-none'})



class FormLogin(forms.Form):
    fullname = forms.CharField(label='نام کاربری', max_length=150)
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    phone = forms.CharField(label='شماره تلفن', max_length=11, required=False)

    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'placeholder:text-right text-sm block w-full rounded-md border border-gray-300 px-3 py-3 font-normal text-gray-700 outline-none transition-all focus:border-blue-500 focus:outline-none'
            })

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        phone = cleaned_data.get('phone')
        fullname = cleaned_data.get('fullname')


        if phone and not self.validate_phone(phone):
            self.add_error('phone', "شماره تلفن معتبر نیست.")


        if phone and fullname:
            try:
                user = User.objects.get(phone=phone, fullname=fullname)
                if not user.check_password(password):
                    self.add_error('password', "رمز عبور اشتباه است.")  # Password is incorrect
            except User.DoesNotExist:
                self.add_error('phone', "شماره تلفن یا نام کاربری اشتباه است.")

        return cleaned_data

    def validate_phone(self, phone):

        if len(phone) != 11 or not phone.isdigit() or not phone.startswith('09'):
            return False
        return True




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'gender', 'about_me', 'profile_picture']
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4}),
        }