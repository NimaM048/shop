
from random import randint
from uuid import uuid4
import ghasedakpack as ghasedakpack
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic.base import  TemplateView
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import  login
from django.views import View
from khayyam import JalaliDatetime
from account.forms import OtpForm, CheckOtp, FormRegister, FormLogin, ProfileForm
from account.models import User, Otp, NewsMessage, Profile
from home.models import Order, UserAddress
from product.forms import DeliveryForm

SMS = ghasedakpack.Ghasedak("449b0c736047db369720dc24a2fbea59178da5123627d6eae4279dd142aeb10")


def register_pass(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('fullname')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')


            if password != password_confirm:
                messages.error(request, "رمز عبور و تأیید آن یکسان نیستند.")
                return redirect('user_register:register')


            if User.objects.filter(phone=phone).exists():
                messages.error(request, "این شماره تلفن قبلاً ثبت شده است.")
                return redirect('user_register:register')


            try:
                user = User.objects.create_user(
                    phone=phone,
                    fullname=fullname,
                    password=password
                )
                user.save()
                login(request, user)
                messages.success(request, "ثبت‌نام با موفقیت انجام شد!")
                return redirect('home:home')

            except Exception as e:
                messages.error(request, f"خطایی در ایجاد حساب کاربری رخ داد: {e}")
                return redirect('user_register:register')

        else:
            messages.error(request, "لطفاً اطلاعات وارد شده را بررسی کنید.")
            return render(request, 'account/password.html', {'form': form})

    form = FormRegister()
    return render(request, 'account/password.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():

            fullname = form.cleaned_data.get('fullname')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')


            try:
                user = User.objects.get(phone=phone, fullname=fullname)
                if user.check_password(password):
                    login(request, user)  # Log the user in
                    messages.success(request, "ورود با موفقیت انجام شد.")
                    return redirect('home:home')
                else:
                    messages.error(request, "رمز عبور اشتباه است.")
            except User.DoesNotExist:
                messages.error(request, "کاربری با این مشخصات پیدا نشد.")
        else:
            messages.error(request, "لطفاً اطلاعات وارد شده را بررسی کنید.")
    else:
        form = FormLogin()

    return render(request, 'account/password_login.html', {'form': form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')





# Register View
class Register(View):
    def get(self, request):
        form = OtpForm()
        return render(request, 'account/login-register.html', context={"form": form})

    def post(self, request):
        form = OtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            phone = cd["phone"]


            try:
                randcode = randint(1000, 9999)
                token = str(uuid4())
                SMS.verification({'receptor': phone, 'type': '1', 'template': 'randcode', 'param1': randcode})
                Otp.objects.create(phone=phone, code=randcode, token=token)
                print(f"OTP for {phone}: {randcode}")
                return redirect(reverse("user_login:verification") + f'?token={token}')
            except Exception as e:

                form.add_error('phone', f"خطایی در ارسال کد تایید رخ داده است. لطفاً دوباره تلاش کنید. {e}")
        else:

            form.add_error('phone', "اطلاعات وارد شده نامعتبر است. لطفاً شماره تماس خود را به درستی وارد کنید.")

        return render(request, 'account/login-register.html', context={'form': form})




class CheckOtpView(View):
    def get(self, request):
        form = CheckOtp()
        return render(request, 'account/otp.html', context={"form": form})

    def post(self, request):
        token = request.GET.get('token')
        if not token:
            return HttpResponse("Token is missing.", status=400)

        form = CheckOtp(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                otp = Otp.objects.get(code=cd['code'], token=token)
                if otp.is_expired():
                    form.add_error('code', "کد وارد شده منقضی شده است.")
                else:
                    user, is_created = User.objects.get_or_create(phone=otp.phone)
                    login(request, user)
                    otp.delete()
                    return redirect('/')
            except Otp.DoesNotExist:
                form.add_error('code', "کد وارد شده صحیح نمی‌باشد.")
        else:
            form.add_error('code', "فرم دارای خطا است. لطفاً مجدداً تلاش کنید.")

        return render(request, 'account/otp.html', context={'form': form})








class ProfileView(View):

    def get(self, request):
        user = request.user


        paid_orders = Order.objects.filter(user=user, is_paid=True)
        unpaid_orders = Order.objects.filter(user=user, is_paid=False)
        cancelled_orders = Order.objects.filter(user=user, status='cancelled')


        total_orders = Order.objects.filter(user=user).count()
        delivered_orders = Order.objects.filter(user=user, status='delivered').count()

        context = {
            'paid_orders': paid_orders,
            'unpaid_orders': unpaid_orders,
            'cancelled_orders': cancelled_orders,
            'total_orders': total_orders,
            'delivered_orders': delivered_orders,
        }

        return render(request, 'account/profile.html', context)


class AddressProfile(TemplateView):
    template_name = 'account/profile-address.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = UserAddress.objects.filter(user=self.request.user)
        context['form'] = DeliveryForm()
        return context

    def post(self, request, *args, **kwargs):

        delete_address_id = request.POST.get('delete_address_id')
        if delete_address_id:
            try:
                address_to_delete = UserAddress.objects.get(id=delete_address_id, user=request.user)
                address_to_delete.delete()
                return redirect('user_login:address_profile')
            except UserAddress.DoesNotExist:
                raise Http404("Address not found.")


        address_id = request.POST.get('address_id')
        address_instance = None

        if address_id:
            try:
                address_instance = UserAddress.objects.get(id=address_id, user=request.user)
            except UserAddress.DoesNotExist:
                raise Http404("Address not found.")

        form = DeliveryForm(request.POST, instance=address_instance)
        if form.is_valid():
            if address_instance:
                form.save()
            else:
                new_address = form.save(commit=False)
                new_address.user = request.user
                new_address.save()

            return redirect('user_login:address_profile')

        return render(request, self.template_name, {'form': form})



class ProfileMessage(TemplateView):
    template_name = "account/profile-messages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user


        orders = Order.objects.filter(user=user).order_by('-created_at')
        order_messages = [
            {
                "title": "ثبت سفارش",
                "date": JalaliDatetime(order.created_at).strftime("%d %B %Y"),
                "body": f"سفارش شما در وضعیت '{order.get_status_display()}' است.",
                "date_link": "#",
                "detail_link": f"/orders/{order.id}/details/",
            }
            for order in orders
        ]


        news_messages = [
            {
                "title": news.title,
                "date": JalaliDatetime(news.date).strftime("%d %B %Y"),
                "body": news.body,
                "detail_link": news.detail_link or "#",
            }
            for news in NewsMessage.objects.all().order_by('-date')
        ]


        context["messages"] = order_messages + news_messages
        return context





class ProfileOrderUserView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile-order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=self.request.user).order_by('-created_at')
        return context


class ProfilePersonalView(TemplateView):
    template_name = 'account/profile-personal-info.html'

    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:

            profile = Profile(user=request.user)
            profile.save()

        form = ProfileForm(instance=profile)
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:

            profile = Profile(user=request.user)

        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_login:personal_profile')
        return self.render_to_response({'form': form})