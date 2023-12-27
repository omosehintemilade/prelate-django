from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def deal_page_title(context):
    print(context)
    package = context["package"]
    return f"{package.deal_name} | Prelate Travels & Tours"
