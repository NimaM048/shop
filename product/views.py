
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg
from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from home.models import Product, MostSellProduct, LastProductOffer, Category, Order, OrderItem, DiscountCode, \
    UserDiscountCode, UserAddress
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.views.generic import TemplateView
from product.card_models import Cart
from product.forms import DeliveryForm, CommentForm
from product.models import Comment


class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['colors'] = self.object.color.all()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = self.object
            comment.user = request.user
            comment.save()
            return redirect('product/product_detail.html', pk=self.object.pk)
        else:
            return self.render_to_response(self.get_context_data(form=form))

def comments_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.all().order_by('-created_at')
    average_rating = comments.aggregate(Avg('recommendation'))['recommendation__avg'] or 0
    return render(request, 'product/product_detail.html', {'comments': comments, 'average_rating': average_rating, 'product': product})


@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            messages.success(request, "نظر شما با موفقیت ثبت شد.")
            return redirect(request.path + f'?product_id={product_id}')
    else:
        form = CommentForm()

    return render(request, 'product/product_detail.html', {'form': form, 'product': product})






class MostProductDetailView(DetailView):
    template_name = 'product/mostsellproduct_detail.html'
    model = MostSellProduct

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        comments = Comment.objects.filter(most_sell_product=product).order_by('-created_at')  # Query comments related to MostSellProduct
        context.update({
            'colors': product.color.all(),
            'mostsellproduct': product,
            'comments': comments,
        })
        return context




@login_required
def add_mostsellproduct_comment(request, product_id):
    product = get_object_or_404(MostSellProduct, id=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.most_sell_product = product
            comment.save()
            messages.success(request, "نظر شما با موفقیت ثبت شد.")
            return redirect('product:most_product_detail', pk=product_id)
    else:
        form = CommentForm()

    return render(request, 'product:most_product_detail', {'form': form, 'mostsellproduct': product})

class AllProduct(TemplateView):
    template_name = 'product/all_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_filters = self.request.GET.getlist('category')
        search_query = self.request.GET.get('search', '')
        is_existed_filter = self.request.GET.get('is_existed')
        price_min = self.request.GET.get('price_min')
        price_max = self.request.GET.get('price_max')

        products = Product.objects.filter(is_active=True)
        most_sold_products = MostSellProduct.objects.filter(is_active=True)

        if category_filters and 'all' not in category_filters:
            products = products.filter(category__name__in=category_filters)
            most_sold_products = most_sold_products.filter(category__name__in=category_filters)

        if is_existed_filter:
            products = products.filter(is_existed=True)
            most_sold_products = most_sold_products.filter(is_existed=True)

        if price_min:
            products = products.filter(price__gte=price_min)
            most_sold_products = most_sold_products.filter(price__gte=price_min)

        if price_max:
            products = products.filter(price__lte=price_max)
            most_sold_products = most_sold_products.filter(price__lte=price_max)

        if search_query:
            products = products.filter(name__icontains=search_query)
            most_sold_products = most_sold_products.filter(name__icontains=search_query)

        paginator = Paginator(products, 10)
        page = self.request.GET.get('page')

        try:
            products_paginated = paginator.page(page)
        except PageNotAnInteger:
            products_paginated = paginator.page(1)
        except EmptyPage:
            products_paginated = paginator.page(paginator.num_pages)

        paginator_most_sold = Paginator(most_sold_products, 10)
        try:
            most_sold_products_paginated = paginator_most_sold.page(page)
        except PageNotAnInteger:
            most_sold_products_paginated = paginator_most_sold.page(1)
        except EmptyPage:
            most_sold_products_paginated = paginator_most_sold.page(paginator_most_sold.num_pages)

        context.update({
            'products': products_paginated,
            'most_sold_products': most_sold_products_paginated,
            'last_product_offers': LastProductOffer.objects.filter(countdown_end__gt=timezone.now()),
            'categories': Category.objects.all(),
            'selected_categories': category_filters,
            'search_query': search_query,
            'price_min': price_min,
            'price_max': price_max,
        })
        return context


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        if not cart.cart:
            return redirect('product:empty')
        if not request.user.is_authenticated:
            return redirect('user_login:login')
        return render(request, 'product/cart.html', {
            'cart': cart,
            'items_count': cart.items_count(),
            'total_price': cart.total(),
        })


class CartAddView(View):
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('user_login:login')

        product = get_object_or_404(Product, id=pk)
        quantity = int(request.POST.get('quantity', 1))
        cart = Cart(request)


        if not cart.add(quantity, product):
            messages.error(request, f"Only {product.storage_capacity} of this product is available in stock.")
            return redirect('product:cart_detail')


        return redirect('product:cart_detail')


class CartDeleteView(View):

    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)

        return redirect('product:cart_detail')


class CartUpdateQuantityView(View):
    def get(self, request, id, action, product_type):
        cart = Cart(request)


        unique_id = cart.unique_id_generator(id, product_type)
        if unique_id not in cart.cart:
            return redirect('product:cart_detail')

        item = cart.cart[unique_id]


        if product_type == 'mostsell':
            product = get_object_or_404(MostSellProduct, id=id)
        else:
            product = get_object_or_404(Product, id=id)


        if action == 'increment':
            cart.add(1, product)
        elif action == 'decrement':
            cart.decrease(1, product)

        return redirect('product:cart_detail')


class CartAddMostSellProductView(View):
    def post(self, request, pk):
        most_sell_product = get_object_or_404(MostSellProduct, id=pk)


        if most_sell_product.storage_capacity <= 0:
            messages.error(request, "این محصول در حال حاضر موجود نیست")
            return redirect('product:cart_detail')

        quantity = request.POST.get('quantity', 1)
        cart = Cart(request)
        cart.add(quantity, most_sell_product)

        return redirect('product:cart_detail')





class CartEmptyView(TemplateView):
    template_name = 'product/cart-empty.html'





class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        form = DeliveryForm()

        addresses = UserAddress.objects.filter(user=request.user)

        return render(request, 'product/order.html', {
            'order': order,
            'form': form,
            'addresses': addresses
        })

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)

        selected_address_id = request.POST.get('address')

        if selected_address_id:

            address = get_object_or_404(UserAddress, id=selected_address_id, user=request.user)
            order.address = address
            order.save()
            messages.success(request, 'آدرس شما با موفقیت ثبت شد!')
        else:

            form = DeliveryForm(request.POST)
            if form.is_valid():
                user_address = UserAddress.objects.create(
                    user=request.user,
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    province=form.cleaned_data['province'],
                    city=form.cleaned_data['city'],
                    street=form.cleaned_data['street_details'],
                    building_info=form.cleaned_data['unit_details'],
                    phone=form.cleaned_data['phone'],
                    post_code=form.cleaned_data['postal_code'],
                    mail_ticket=form.cleaned_data.get('additional_notes', ''),
                )
                order.address = user_address
                order.save()
                messages.success(request, 'آدرس شما با موفقیت ثبت شد!')

        return redirect('product:order_detail', order.id)


class OrderCreationView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())

        for item in cart:

            if item['product_type'] == 'mostsell':
                product = MostSellProduct.objects.get(id=int(item['id']))
            else:
                product = Product.objects.get(id=int(item['id']))

            quantity_in_cart = item['quantity']


            if quantity_in_cart > product.storage_capacity:
                messages.error(request, f"محصول {product.name} بیش از موجودی انبار درخواست شده است.")
                return redirect('product:cart_detail')

            price = Decimal(item['price'].replace(',', ''))
            content_type = ContentType.objects.get_for_model(product)


            OrderItem.objects.create(
                order=order,
                content_type=content_type,
                object_id=product.id,
                quantity=quantity_in_cart,
                price=price
            )


        cart.remove()


        return redirect('product:order_detail', order.id)



class ApplyDiscountView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        code = request.POST.get('discount_code')

        try:
            discount_code = DiscountCode.objects.get(name=code)
        except DiscountCode.DoesNotExist:
            messages.error(request, 'کد وارد شده نا معتبر است.')
            return JsonResponse({'success': False, 'message': 'کد وارد شده نا معتبر است.'}, status=400)

        if discount_code.quantity == 0:
            messages.error(request, 'این کد تخفیف استفاده شده است.')
            return JsonResponse({'success': False, 'message': 'این کد تخفیف استفاده شده است.'}, status=400)

        if UserDiscountCode.objects.filter(user=request.user, discount_code=discount_code).exists():
            messages.error(request, 'شما یکبار از این کد استفاده کرده اید.')
            return JsonResponse({'success': False, 'message': 'شما یکبار از این کد استفاده کرده اید.'}, status=400)


        discount_amount = discount_code.percentage * order.total_price / 100
        order.total_price -= discount_amount
        order.save()

        discount_code.quantity -= 1
        discount_code.save()

        UserDiscountCode.objects.create(user=request.user, discount_code=discount_code)

        messages.success(request, 'کد تخفیف با موفقیت اعمال شد!')
        return JsonResponse({
            'success': True,
            'discount_amount': int(discount_amount),
            'total_price': int(order.total_price),
        })
