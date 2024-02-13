from django.shortcuts import render

from svetofors.forms import SetupPhaseSvetofor


def index(request):
    if request.method == 'POST':
        form = SetupPhaseSvetofor(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = SetupPhaseSvetofor()

    return render(request, 'index.html', context={'form': form})


