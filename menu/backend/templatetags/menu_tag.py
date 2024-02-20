from django import template
from backend.models import Menu

# Экземпляр Library для регистрации тегов
register = template.Library()


# Регистрируем тег и подключаем шаблон menu.html
@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    menu_sections = Menu.objects.filter(level=1)
    return {
        'menu_sections': menu_sections,
    }
