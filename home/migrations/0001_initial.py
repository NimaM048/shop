# Generated by Django 5.1.3 on 2025-01-19 19:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('content', models.TextField(verbose_name='محتوا')),
                ('order', models.IntegerField(default=0, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=288, verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=288, verbose_name='نام دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی بلاگ',
                'verbose_name_plural': 'دسته بندی های بلاگ',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=288, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('message', models.TextField(verbose_name='پیام')),
                ('subscribe_to_newsletter', models.BooleanField(default=False, verbose_name='اشتراک در خبرنامه')),
            ],
            options={
                'verbose_name': 'تماس',
                'verbose_name_plural': 'تماس ها',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='شماره تلفن')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('working_hours', models.CharField(max_length=50, verbose_name='ساعات کاری')),
                ('address', models.TextField(verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'اطلاعات تماس',
                'verbose_name_plural': 'اطلاعات تماس',
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='نام کد تخفیف')),
                ('percentage', models.SmallIntegerField(default=0, verbose_name='درصد تخفیف')),
                ('quantity', models.SmallIntegerField(default=1, verbose_name='تعداد قابل استفاده')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کدهای تخفیف',
            },
        ),
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='شماره تلفن')),
            ],
            options={
                'verbose_name': 'اطلاعات فوتر',
                'verbose_name_plural': 'اطلاعات فوتر',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان بلاگ')),
                ('image', models.ImageField(upload_to='blog/images/', verbose_name='تصویر بلاگ')),
                ('content', models.TextField(verbose_name='محتوای بلاگ')),
                ('publish_date', models.DateField(verbose_name='تاریخ انتشار')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس بلاگ')),
                ('Introduction', models.TextField(blank=True, null=True, verbose_name='معرفی')),
                ('Introduction_tow', models.TextField(blank=True, null=True, verbose_name='معرفی دو')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='home.categoryblog', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پست بلاگ',
                'verbose_name_plural': 'پست های بلاگ',
            },
        ),
        migrations.CreateModel(
            name='LastProductOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام محصول')),
                ('description', models.TextField(verbose_name='توضیحات محصول')),
                ('image', models.ImageField(upload_to='products/', verbose_name='تصویر محصول')),
                ('price', models.CharField(max_length=100, verbose_name='قیمت')),
                ('discount_price', models.CharField(blank=True, max_length=100, null=True, verbose_name='قیمت تخفیف خورده')),
                ('sales_count', models.PositiveIntegerField(default=0, verbose_name='تعداد فروش')),
                ('satisfaction_percentage', models.PositiveIntegerField(default=0, verbose_name='درصد رضایت')),
                ('countdown_end', models.DateTimeField(verbose_name='پایان شمارش معکوس')),
                ('is_existed', models.BooleanField(blank=True, null=True, verbose_name='موجود')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_products', to='home.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پیشنهاد محصول آخر',
                'verbose_name_plural': 'پیشنهادات محصولات آخر',
            },
        ),
        migrations.CreateModel(
            name='MostSellProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام محصول')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.CharField(max_length=100, verbose_name='قیمت')),
                ('discounted_price', models.CharField(blank=True, max_length=100, null=True, verbose_name='قیمت تخفیف خورده')),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('image', models.ImageField(upload_to='products/', verbose_name='تصویر')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('body_material', models.CharField(blank=True, max_length=255, null=True, verbose_name='جنس بدنه')),
                ('ram_capacity', models.PositiveIntegerField(blank=True, null=True, verbose_name='ظرفیت رم')),
                ('battery', models.CharField(blank=True, max_length=255, null=True, verbose_name='باطری')),
                ('guaranty', models.CharField(blank=True, max_length=255, null=True, verbose_name='گارانتی')),
                ('post_time', models.CharField(blank=True, max_length=255, null=True, verbose_name='زمان ارسال')),
                ('storage_capacity', models.PositiveIntegerField(blank=True, null=True, verbose_name='ظرفیت حافظه')),
                ('processor', models.CharField(blank=True, max_length=255, null=True, verbose_name='پردازنده')),
                ('processor_frequency', models.CharField(blank=True, max_length=255, null=True, verbose_name='فرکانس پردازنده')),
                ('weight', models.CharField(blank=True, max_length=255, null=True, verbose_name='وزن')),
                ('bluetooth_version', models.CharField(blank=True, max_length=255, null=True, verbose_name='نسخه بلوتوث')),
                ('wifi_version', models.CharField(blank=True, max_length=255, null=True, verbose_name='نسخه وای فای')),
                ('operating_system', models.CharField(blank=True, max_length=255, null=True, verbose_name='سیستم عامل')),
                ('gpu', models.CharField(blank=True, max_length=255, null=True, verbose_name='کارت گرافیک')),
                ('front_camera', models.CharField(blank=True, max_length=255, null=True, verbose_name='دوربین جلو')),
                ('rear_camera', models.CharField(blank=True, max_length=255, null=True, verbose_name='دوربین عقب')),
                ('is_existed', models.BooleanField(blank=True, null=True, verbose_name='موجود')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='most_products', to='home.category', verbose_name='دسته بندی')),
                ('color', models.ManyToManyField(to='home.color', verbose_name='رنگ')),
            ],
            options={
                'verbose_name': 'محصول پرفروش',
                'verbose_name_plural': 'محصولات پرفروش',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='قیمت کل')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده')),
                ('status', models.CharField(choices=[('pending', 'در انتظار'), ('processing', 'در حال پردازش'), ('shipped', 'ارسال شده'), ('delivered', 'تحویل داده شده'), ('cancelled', 'لغو شده')], default='pending', max_length=20, verbose_name='وضعیت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارش ها',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='شناسه شیء')),
                ('quantity', models.PositiveIntegerField(verbose_name='تعداد')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='نوع محتوا')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='home.order', verbose_name='سفارش')),
            ],
            options={
                'verbose_name': 'اقلام سفارس',
                'verbose_name_plural': 'اقلام سفارس',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام محصول')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.CharField(max_length=100, verbose_name='قیمت')),
                ('discounted_price', models.CharField(blank=True, max_length=100, null=True, verbose_name='قیمت تخفیف خورده')),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True, verbose_name='درصد تخفیف')),
                ('image', models.ImageField(upload_to='products/', verbose_name='تصویر')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ به روز رسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('body_material', models.CharField(blank=True, max_length=255, null=True, verbose_name='جنس بدنه')),
                ('ram_capacity', models.PositiveIntegerField(blank=True, null=True, verbose_name='ظرفیت رم')),
                ('battery', models.CharField(blank=True, max_length=255, null=True, verbose_name='باطری')),
                ('guaranty', models.CharField(blank=True, max_length=255, null=True, verbose_name='گارانتی')),
                ('post_time', models.CharField(blank=True, max_length=255, null=True, verbose_name='زمان ارسال')),
                ('storage_capacity', models.PositiveIntegerField(blank=True, null=True, verbose_name='ظرفیت حافظه')),
                ('processor', models.CharField(blank=True, max_length=255, null=True, verbose_name='پردازنده')),
                ('processor_frequency', models.CharField(blank=True, max_length=255, null=True, verbose_name='فرکانس پردازنده')),
                ('weight', models.CharField(blank=True, max_length=255, null=True, verbose_name='وزن')),
                ('bluetooth_version', models.CharField(blank=True, max_length=255, null=True, verbose_name='نسخه بلوتوث')),
                ('wifi_version', models.CharField(blank=True, max_length=255, null=True, verbose_name='نسخه وای فای')),
                ('operating_system', models.CharField(blank=True, max_length=255, null=True, verbose_name='سیستم عامل')),
                ('gpu', models.CharField(blank=True, max_length=255, null=True, verbose_name='کارت گرافیک')),
                ('front_camera', models.CharField(blank=True, max_length=255, null=True, verbose_name='دوربین جلو')),
                ('rear_camera', models.CharField(blank=True, max_length=255, null=True, verbose_name='دوربین عقب')),
                ('is_existed', models.BooleanField(blank=True, null=True, verbose_name='موجود')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='home.category', verbose_name='دسته بندی')),
                ('color', models.ManyToManyField(to='home.color', verbose_name='رنگ')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام')),
                ('last_name', models.CharField(max_length=100, verbose_name='نام خانوادگی')),
                ('province', models.CharField(max_length=100, verbose_name='استان')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('street', models.CharField(max_length=255, verbose_name='خیابان')),
                ('building_info', models.CharField(max_length=255, verbose_name='اطلاعات ساختمان')),
                ('phone', models.CharField(max_length=15, verbose_name='تلفن')),
                ('post_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('mail_ticket', models.TextField(blank=True, null=True, verbose_name='توضیحات اضافی')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس کاربر',
                'verbose_name_plural': 'آدرس\u200cهای کاربران',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.useraddress', verbose_name='آدرس'),
        ),
        migrations.CreateModel(
            name='UserDiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.discountcode', verbose_name='کد تخفیف')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کد تخفیف کاربر',
                'verbose_name_plural': 'کدهای تخفیف کاربران',
                'unique_together': {('user', 'discount_code')},
            },
        ),
    ]
