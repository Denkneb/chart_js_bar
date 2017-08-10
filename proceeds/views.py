from django.http import JsonResponse
from django.shortcuts import render

from proceeds.forms import ProceedsForm
from proceeds.models import Locomotive, Mileage


def view_proceeds(request):
    form = ProceedsForm(request.POST)

    if request.method == "POST":
        labels = []
        data = []
        filial = request.POST.get('filial', None)
        series = request.POST.get('series', None)
        period_start = request.POST.get('period_start', None)
        period_end = request.POST.get('period_end', None)

        for year in range(int(period_start), int(period_end) + 1):
            labels.append(str(year))

            if series == 'None':
                mileages_of_year = Mileage.objects.filter(filial__name=filial).filter(year__year=year)
                proceeds = []
                for mileage in mileages_of_year:
                    proceeds.append(mileage.mileage * Locomotive.objects.get(series=mileage.locomotive).rate)
                data.append(sum(proceeds))
            else:
                mileages_of_year = Mileage.objects.filter(filial__name=filial) \
                    .filter(locomotive__series=series).get(year__year=year)
                data.append(mileages_of_year.mileage * Locomotive.objects.get(series=series).rate)

        context = {
            'labels': labels,
            'data': data,
        }
        return JsonResponse(context)

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def get_selected(request):
    filial = request.GET.get('filial_name')
    locomotive_series = Locomotive.objects.filter(filial__name=filial)
    series = []
    for i in locomotive_series:
        series.append(i.series)
    context = {
        'series': series
    }
    return JsonResponse(context)
