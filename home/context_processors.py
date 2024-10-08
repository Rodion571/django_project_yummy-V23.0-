from .models import FooterItems


def footer_items(request):

    context = {}
    items = FooterItems.objects.all()

    for item in items:
        if item.item_title == 'Address':
            context['address'] = item
        elif item.item_title == 'Reservations':
            context['reservations'] = item



    return {
        'footer_items': context
    }