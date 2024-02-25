from . models import *
def menu_click(request):
    links=Category.objects.all()
    return dict(links=links)