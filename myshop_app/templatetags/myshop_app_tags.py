from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_header_menu(context):

    user = context['request'].user
    username = user.get_short_name() if not user.is_anonymous else ""

    about = {'title': 'About', 'url': 'myshop_app:about'}
    products = {'title': 'Products', 'url': 'myshop_app:products'}
    cart = {'title': 'Cart', 'url': 'myshop_app:cart'}
    add_product = {'title': 'Add', 'url': 'myshop_app:add_product'}
    login = {'title': 'Login', 'url': 'users_app:login'}
    logout = {'title': f'Logout({username})', 'url': 'users_app:logout'}

    menu_base = [about, products, cart]

    if user.is_anonymous:
        return [*menu_base, login]
    elif user.is_staff:
        return [*menu_base, add_product, logout]
    else:
        return [*menu_base, logout]