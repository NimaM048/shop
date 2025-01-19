from django.db import models

from account.models import User
from home.models import Product, MostSellProduct


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')
    most_sell_product = models.ForeignKey(MostSellProduct, null=True, blank=True, on_delete=models.CASCADE, related_name='comments', verbose_name='پرفروش ترین محصول')
    title = models.CharField(max_length=255, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    recommendation = models.CharField(max_length=3, choices=[('yes', 'بله'), ('no', 'خیر')], verbose_name='توصیه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_verified = models.BooleanField(default=False, verbose_name='تأیید شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        ordering = ['-created_at']