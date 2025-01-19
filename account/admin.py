from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User, Otp, UserSession, NewsMessage, Profile


class UserCreationForm(forms.ModelForm):


    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تایید گذرواژه", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone",]

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):


    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["phone", "password", "is_admin"]


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ["phone" ,"email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["fullname",]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent', 'created_at')
    search_fields = ('user__username', 'ip_address')

admin.site.register(UserSession, UserSessionAdmin)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Otp)

@admin.register(NewsMessage)
class NewsMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'body')
    search_fields = ('title', 'body')
    list_filter = ('date',)
