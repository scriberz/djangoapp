from django import template
from menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu = Menu.objects.get(name=menu_name)
    items = MenuItem.objects.filter(menu=menu).select_related('parent').prefetch_related('children')

    menu_dict = {}
    for item in items:
        if not item.parent:
            menu_dict[item] = []
        else:
            if item.parent not in menu_dict:
                menu_dict[item.parent] = []
            menu_dict[item.parent].append(item)

    active_item = None
    for item in items:
        if item.get_absolute_url() == request.path:
            active_item = item
            break

    context['menu'] = menu_dict
    context['active_item'] = active_item
    return context
