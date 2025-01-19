from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.urls import reverse
from django.utils.html import format_html
from .models import Product, MostSellProduct, LastProductOffer, BlogPost, Contact, ContactInfo, AboutUs, FooterInfo, \
    Category, CategoryBlog, Color, UserAddress, DiscountCode, UserDiscountCode, Order, OrderItem





class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('is_active', 'category', 'created_at')


admin.site.register(Product, ProductAdmin)




from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('get_product_name', 'quantity', 'price')
    fields = ('get_product_name', 'quantity', 'price')

    def get_product_name(self, obj):
        return obj.content_object
    get_product_name.short_description = 'محصول'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_user_name',
        'total_price',
        'get_total_items',
        'is_paid',
        'status',
        'created_at',
        'view_order_items',
        'address_first_name',
        'address_last_name',
        'address_city',
        'address_province',
        'address_street',
        'address_phone',
        'address_building_info',
        'address_post_code',
    )
    list_filter = ('is_paid', 'status', 'created_at')
    search_fields = ('user__username', 'user__email', 'address__first_name', 'address__last_name', 'address__phone')
    inlines = (OrderItemInline,)
    actions = ['mark_as_paid', 'mark_as_processing', 'mark_as_shipped']

    fieldsets = (
        ('اطلاعات سفارش', {
            'fields': ('user', 'total_price', 'is_paid', 'status', 'created_at', 'updated_at')
        }),
        ('اطلاعات ارسال', {
            'fields': (
                'address',
                'address_phone',
                'address_building_info',
                'address_post_code',
            )
        }),
    )

    readonly_fields = (
        'created_at',
        'updated_at',
        'address_phone',
        'address_building_info',
        'address_post_code',
    )



    def get_total_items(self, obj):
        return obj.items.count()  # Assuming `items` is a related_name for order items
    get_total_items.short_description = 'تعداد محصولات'

    def view_order_items(self, obj):
        """
        Displays a clickable link to the related order items in the admin.
        """
        url = reverse('admin:home_orderitem_changelist') + f'?order__id__exact={obj.id}'
        return format_html('<a href="{}">مشاهده محصولات</a>', url)
    view_order_items.short_description = 'محصولات سفارش'

    def mark_as_paid(self, request, queryset):
        queryset.update(is_paid=True, status='processing')
    mark_as_paid.short_description = "علامت زدن سفارش‌های پرداخت شده"

    def mark_as_processing(self, request, queryset):
        queryset.update(status='processing')
    mark_as_processing.short_description = "علامت زدن سفارش‌های در حال پردازش"

    def mark_as_shipped(self, request, queryset):
        queryset.update(status='shipped')
    mark_as_shipped.short_description = "علامت زدن سفارش‌های ارسال شده"

    def address_phone(self, obj):
        return obj.address.phone if obj.address else 'N/A'
    address_phone.short_description = 'تلفن'

    def address_building_info(self, obj):
        return obj.address.building_info if obj.address else 'N/A'
    address_building_info.short_description = 'اطلاعات ساختمان'

    def address_post_code(self, obj):
        return obj.address.post_code if obj.address else 'N/A'
    address_post_code.short_description = 'کد پستی'

    def address_first_name(self, obj):
        return obj.address.first_name if obj.address else ''

    address_first_name.short_description = 'نام'

    def address_last_name(self, obj):
        return obj.address.last_name if obj.address else ''

    address_last_name.short_description = 'نام خانوادگی'

    def address_city(self, obj):
        return obj.address.city if obj.address else ''

    address_city.short_description = 'شهر'

    def address_province(self, obj):
        return obj.address.province if obj.address else ''

    address_province.short_description = 'استان'

    def address_street(self, obj):
        return obj.address.street if obj.address else ''

    address_street.short_description = 'خیابان'

    def address_phone(self, obj):
        return obj.address.phone if obj.address else ''

    address_phone.short_description = 'تلفن'

    def address_building_info(self, obj):
        return obj.address.building_info if obj.address else ''

    address_building_info.short_description = 'اطلاعات ساختمان'

    def address_post_code(self, obj):
        return obj.address.post_code if obj.address else ''

    address_post_code.short_description = 'کد پستی'

    def view_order_items(self, obj):
        """
        A method to display a clickable link to the OrderItems related to this order.
        """
        url = f"/admin/home/orderitem/?order__id__exact={obj.id}"
        return format_html('<a href="{}">مشاهده محصولات</a>', url)

    view_order_items.short_description = 'محصولات سفارش'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'get_product_name', 'quantity', 'price')
    list_filter = ('order__status',)
    search_fields = ('order__id', 'content_type__model', 'object_id')

    def get_product_name(self, obj):
        return obj.content_object
    get_product_name.short_description = 'محصول'

@admin.register(UserAddress)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'street', 'phone', 'user')
    search_fields = ('first_name', 'last_name', 'city', 'user__username')


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'percentage')
    search_fields = ('name',)
    list_filter = ('quantity',)

class UserDiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'discount_code')
    list_filter = ('user', 'discount_code')

admin.site.register(UserDiscountCode, UserDiscountCodeAdmin)



admin.site.register(Color)

class MostsellProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_active', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('is_active', 'category', 'created_at')


admin.site.register(MostSellProduct, MostsellProductAdmin)


admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(FooterInfo)
admin.site.register(Category)
admin.site.register(CategoryBlog)




@admin.register(LastProductOffer)
class LastProductOfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount_price', 'sales_count', 'satisfaction_percentage')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

