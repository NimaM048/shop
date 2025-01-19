import jdatetime
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=288, verbose_name= 'دسته بندی')




    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'




    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=288 , verbose_name= 'نام')



    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'




    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('نام محصول'))
    description = models.TextField(verbose_name=_('توضیحات'))
    price = models.CharField(max_length=100, verbose_name=_('قیمت'))
    discounted_price = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('قیمت تخفیف خورده'))
    discount_percentage = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('درصد تخفیف'))
    image = models.ImageField(upload_to='products/', verbose_name=_('تصویر'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ به روز رسانی'))
    is_active = models.BooleanField(default=True, verbose_name=_('فعال'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', null=True, blank=True, verbose_name=_('دسته بندی'))
    body_material = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('جنس بدنه'))
    ram_capacity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('ظرفیت رم'))
    battery = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('باطری'))
    color = models.ManyToManyField('Color', verbose_name=_('رنگ'))
    guaranty = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('گارانتی'))
    post_time = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('زمان ارسال'))
    storage_capacity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('ظرفیت حافظه'))
    processor = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('پردازنده'))
    processor_frequency = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('فرکانس پردازنده'))
    weight = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('وزن'))
    bluetooth_version = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('نسخه بلوتوث'))
    wifi_version = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('نسخه وای فای'))
    operating_system = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('سیستم عامل'))
    gpu = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('کارت گرافیک'))
    front_camera = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('دوربین جلو'))
    rear_camera = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('دوربین عقب'))
    is_existed = models.BooleanField(null=True, blank=True, verbose_name=_('موجود'))

    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')

    def __str__(self):
        return self.name











class MostSellProduct(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('نام محصول'))
    description = models.TextField(verbose_name=_('توضیحات'))
    price = models.CharField(max_length=100, verbose_name=_('قیمت'))
    discounted_price = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('قیمت تخفیف خورده'))
    discount_percentage = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('درصد تخفیف'))
    image = models.ImageField(upload_to='products/', verbose_name=_('تصویر'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ به روز رسانی'))
    is_active = models.BooleanField(default=True, verbose_name=_('فعال'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='most_products', null=True, blank=True, verbose_name=_('دسته بندی'))
    body_material = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('جنس بدنه'))
    ram_capacity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('ظرفیت رم'))
    battery = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('باطری'))
    color = models.ManyToManyField('Color', verbose_name=_('رنگ'))
    guaranty = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('گارانتی'))
    post_time = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('زمان ارسال'))
    storage_capacity = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('ظرفیت حافظه'))
    processor = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('پردازنده'))
    processor_frequency = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('فرکانس پردازنده'))
    weight = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('وزن'))
    bluetooth_version = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('نسخه بلوتوث'))
    wifi_version = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('نسخه وای فای'))
    operating_system = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('سیستم عامل'))
    gpu = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('کارت گرافیک'))
    front_camera = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('دوربین جلو'))
    rear_camera = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('دوربین عقب'))
    is_existed = models.BooleanField(null=True, blank=True, verbose_name=_('موجود'))

    class Meta:
        verbose_name = _('محصول پرفروش')
        verbose_name_plural = _('محصولات پرفروش')

    def __str__(self):
        return self.name




class LastProductOffer(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    image = models.ImageField(upload_to='products/', verbose_name='تصویر محصول')
    price = models.CharField(max_length=100, verbose_name='قیمت')
    discount_price = models.CharField(max_length=100, blank=True, null=True, verbose_name='قیمت تخفیف خورده')
    sales_count = models.PositiveIntegerField(default=0, verbose_name='تعداد فروش')
    satisfaction_percentage = models.PositiveIntegerField(default=0, verbose_name='درصد رضایت')
    countdown_end = models.DateTimeField(verbose_name='پایان شمارش معکوس')  # For the countdown timer
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='last_products', null=True, blank=True, verbose_name='دسته بندی')
    is_existed = models.BooleanField(null=True, blank=True, verbose_name='موجود')

    def get_discount_percentage(self):
        if self.discount_price:
            return int((1 - (float(self.discount_price) / float(self.price))) * 100)
        return None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پیشنهاد محصول آخر'
        verbose_name_plural = 'پیشنهادات محصولات آخر'



class CategoryBlog(models.Model):
    name = models.CharField(max_length=288, verbose_name='نام دسته بندی')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی بلاگ'
        verbose_name_plural = 'دسته بندی های بلاگ'


class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان بلاگ')
    image = models.ImageField(upload_to='blog/images/', verbose_name='تصویر بلاگ')
    content = models.TextField(verbose_name='محتوای بلاگ')
    publish_date = models.DateField(verbose_name='تاریخ انتشار')
    slug = models.SlugField(unique=True, verbose_name='آدرس بلاگ')
    category = models.ForeignKey(CategoryBlog, on_delete=models.CASCADE, related_name='blogs', null=True, blank=True, verbose_name='دسته بندی')
    Introduction = models.TextField(null=True, blank=True, verbose_name='معرفی')
    Introduction_tow = models.TextField(null=True, blank=True, verbose_name='معرفی دو')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"

    def get_publish_date_shamsi(self):
        shamsi_date = jdatetime.date.fromgregorian(date=self.publish_date)
        return shamsi_date.strftime('%Y/%m/%d')

    class Meta:
        verbose_name = 'پست بلاگ'
        verbose_name_plural = 'پست های بلاگ'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(verbose_name='پیام')
    subscribe_to_newsletter = models.BooleanField(default=False, verbose_name='اشتراک در خبرنامه')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = 'تماس ها'


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=20, verbose_name='شماره تلفن')
    email = models.EmailField(verbose_name='ایمیل')
    working_hours = models.CharField(max_length=50, verbose_name='ساعات کاری')
    address = models.TextField(verbose_name='آدرس')

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'


class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    content = models.TextField(verbose_name='محتوا')
    order = models.IntegerField(default=0, verbose_name='ترتیب')

    class Meta:
        ordering = ['order']
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'


class FooterInfo(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name='آدرس')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    phone = models.IntegerField(null=True, blank=True, verbose_name='شماره تلفن')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'اطلاعات فوتر'
        verbose_name_plural = 'اطلاعات فوتر'

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', null=True, blank=True, verbose_name="کاربر")
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    street = models.CharField(max_length=255, verbose_name="خیابان")
    building_info = models.CharField(max_length=255, verbose_name="اطلاعات ساختمان")
    phone = models.CharField(max_length=15, verbose_name="تلفن")
    post_code = models.CharField(max_length=10, verbose_name="کد پستی")
    mail_ticket = models.TextField(blank=True, null=True, verbose_name="توضیحات اضافی")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.city}, {self.street}"

    class Meta:
        verbose_name = "آدرس کاربر"
        verbose_name_plural = "آدرس‌های کاربران"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", verbose_name="کاربر")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="قیمت کل")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده")
    address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="آدرس")



    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('processing', 'در حال پردازش'),
        ('shipped', 'ارسال شده'),
        ('delivered', 'تحویل داده شده'),
        ('cancelled', 'لغو شده'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="وضعیت")

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    def __str__(self):
        return f"سفارش #{self.id} برای {self.get_user_name()} - مبلغ: {self.total_price}"

    def get_user_name(self):
        if hasattr(self.user, 'get_full_name'):
            return self.user.get_full_name()
        return self.user.fullname

    def get_full_address(self):
        if self.address:
            return f"{self.address.first_name} {self.address.last_name}, {self.address.street}, {self.address.city}, {self.address.province}, {self.address.post_code}"
        return "بدون آدرس"

    def get_contact_info(self):
        # Now fetching the phone number from the related UserAddress model
        return self.address.phone if self.address else "بدون تلفن"

    def get_order_items(self):
        return ", ".join([f"{item.content_object} (x{item.quantity})" for item in self.items.all()])

    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())

    def save(self, *args, **kwargs):
        if self.pk:
            original = Order.objects.get(pk=self.pk)

            if not original.is_paid and self.is_paid:
                self.status = 'processing'
                self.update_inventory()

        super().save(*args, **kwargs)

    def update_inventory(self):
        for item in self.items.all():
            product = item.content_object

            if isinstance(product, Product) and product.storage_capacity:
                product.storage_capacity -= item.quantity
                if product.storage_capacity < 0:
                    raise ValueError(f"موجودی کافی برای {product.name} وجود ندارد")
                product.save()

            elif isinstance(product, MostSellProduct) and product.storage_capacity:
                product.storage_capacity -= item.quantity
                if product.storage_capacity < 0:
                    raise ValueError(f"موجودی کافی برای {product.name} وجود ندارد")
                product.save()







class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="سفارش")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="نوع محتوا")
    object_id = models.PositiveIntegerField(verbose_name="شناسه شیء")
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(verbose_name="تعداد")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")

    def __str__(self):
        return f"{self.quantity} x {self.content_object} در {self.order}"



    class Meta:
        verbose_name =  'اقلام سفارس'
        verbose_name_plural = verbose_name



class DiscountCode(models.Model):
    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "کدهای تخفیف"

    name = models.CharField(max_length=10, unique=True, verbose_name="نام کد تخفیف")
    percentage = models.SmallIntegerField(default=0, verbose_name="درصد تخفیف")
    quantity = models.SmallIntegerField(default=1, verbose_name="تعداد قابل استفاده")

    def __str__(self):
        return self.name


class UserDiscountCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    discount_code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE, verbose_name="کد تخفیف")

    class Meta:
        unique_together = ('user', 'discount_code')
        verbose_name = "کد تخفیف کاربر"
        verbose_name_plural = "کدهای تخفیف کاربران"

    def __str__(self):
        return f"{self.user} - {self.discount_code}"







