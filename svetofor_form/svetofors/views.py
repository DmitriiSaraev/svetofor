from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from svetofors.forms import SetupPhaseSvetofor, SetupPhaseSvetoforModel
from svetofors.models import Svetofor


def index(request):
    svetofors = Svetofor.objects.all()
    form = SetupPhaseSvetoforModel

    if request.method == 'POST':
        form = SetupPhaseSvetoforModel(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        form.save()
        return render(request, 'index.html', context={'svetofors': svetofors,
                                                      'form': form})


    return render(request, 'index.html', context={'svetofors': svetofors,
                                                  'form': form})


def up_svetofor(request, svetofor_id):
    if request.method == 'POST':
        ip_address = request.POST.get(
            'ip_address')  # получить значение поля ip_address
        local = request.POST.get('local')  # получить значение поля local
        protocol = request.POST.get(
            'protocol')  # получить значение поля protocol
        print(ip_address, local, protocol)

        # Здесь вы можете использовать полученные данные, сохранить их в базу данных или выполнять другие операции

    svetofor = Svetofor.objects.get(pk=svetofor_id)
    print(svetofor_id)
    return redirect("svetofors:index")


def empty_model(request):
    svetofors = Svetofor()

    forms = []

    for i in range(3):
        forms.append(SetupPhaseSvetoforModel(prefix=str(i)))
    # forms = [SetupPhaseSvetoforModel(prefix=str(i)) for i in range(3)]

    return render(request, 'empty_model.html', {'forms': forms})




def up_svetofor_empty(request):
    if request.method == 'POST':
        form = SetupPhaseSvetoforModel(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect('')  # Перенаправление на страницу успеха
    else:
        return HttpResponseRedirect('')

