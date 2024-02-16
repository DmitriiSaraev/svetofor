from django.shortcuts import render, redirect

from svetofors.forms import SetupPhaseSvetofor, SetupPhaseSvetoforModel
from svetofors.models import Svetofor


def index(request):
    svetofors = Svetofor.objects.all()

    form = SetupPhaseSvetoforModel()

    return render(request, 'index.html', context={'svetofors': svetofors})

def up_svetofor(request, svetofor_id):
    """Добавление товара в корзину"""

    svetofor = Svetofor.objects.get(pk=svetofor_id)
    print(svetofor_id)
    return redirect("svetofors:index", )