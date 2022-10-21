from django import template
register = template.Library()

@register.filter(name='number_group') 
def has_group(number, number_group):
    if len(str(number)) <=6:
        num = str(number)[:-3] + ' '+str(number)[-3:]
    else:
        num = str(number)[:-6] +' '+str(number)[-6:-3] + ' '+str(number)[-3:]
    return num 