
from django.contrib.auth import get_user_model
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from account.models import NewsMessage
from home.models import FooterInfo, Category, Order, Product
from product.card_models import Cart


def footer(request):
   footer = FooterInfo.objects.all()
   category = Category.objects.all()


   return {'footer':footer, 'category':category}


def search_context(request):
   search_query = request.GET.get('search', '')
   return {
      'search_query': search_query,
   }


User = get_user_model()


def cart_context(request):
   cart = Cart(request)
   return {
      'cart': cart,
      'items_count': cart.items_count(),
      'total_price': cart.total(),
   }


def message_count(request):
   if request.user.is_authenticated:

      order_count = Order.objects.filter(user=request.user).count()

      news_count = NewsMessage.objects.count()


      total_messages = order_count + news_count

      return {'message_count': total_messages}

   return {'message_count': 0}


def product_comments_context(request):
   product_id = request.GET.get('product_id') or request.POST.get('product_id')
   if not product_id:
      return {}

   try:
      product = get_object_or_404(Product, id=product_id)
      comments = product.comments.all().order_by('-created_at')
      average_rating = comments.aggregate(Avg('recommendation'))['recommendation__avg'] or 0

      return {
         'comments': comments,
         'average_rating': average_rating,
         'product': product,
      }
   except Product.DoesNotExist:
      return {}
