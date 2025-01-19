from home.models import Product, MostSellProduct

CARD_SESSION_ID = "cart"


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CARD_SESSION_ID)
        if not cart:
            cart = self.session[CARD_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for items in cart.values():
            if 'product_type' in items and items['product_type'] == 'mostsell':
                product = MostSellProduct.objects.get(id=int(items['id']))
            else:
                product = Product.objects.get(id=int(items['id']))
            items['product'] = product

            price = int(items['price'].replace(',', ''))
            items['total'] = int(items['quantity']) * price
            items['unique_id'] = self.unique_id_generator(product.id, items.get('product_type'))
            yield items

    def decrease(self, quantity, product):
        product_type = 'mostsell' if isinstance(product, MostSellProduct) else 'product'
        unique = self.unique_id_generator(product.id, product_type)

        if unique in self.cart:
            if self.cart[unique]['quantity'] > quantity:
                self.cart[unique]['quantity'] -= quantity
            else:
                del self.cart[unique]
            self.save()

    def items_count(self):
        return sum(item['quantity'] for item in self.cart.values())

    def unique_id_generator(self, id, product_type=None):

        if product_type == 'mostsell':
            return f'mostsell_{id}'
        return f'product_{id}'

    def add(self, quantity, product):
        product_type = 'mostsell' if isinstance(product, MostSellProduct) else 'product'
        unique = self.unique_id_generator(product.id, product_type)


        if product_type == 'mostsell':
            available_stock = product.storage_capacity
            current_quantity_in_cart = 0

            if unique in self.cart:
                current_quantity_in_cart = self.cart[unique]['quantity']


            if current_quantity_in_cart + int(quantity) > available_stock:
                return False


        if unique not in self.cart:
            self.cart[unique] = {
                'quantity': 0,
                'price': str(product.price),
                'id': str(product.id),
                'product_type': product_type
            }

        self.cart[unique]['quantity'] += int(quantity)
        self.save()
        return True

    def remove(self):
        del self.session[CARD_SESSION_ID]

    def total(self):
        cart = self.cart.values()
        total = sum(int(item["price"].replace(',', '')) * int(item['quantity']) for item in cart)
        return total

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def save(self):
        self.session.modified = True
