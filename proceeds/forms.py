from django import forms

from proceeds.models import Filial, Locomotive, Year


class ProceedsForm(forms.Form):
    filial_choices = [([f.name, f.name]) for f in Filial.objects.all()]
    period_choices = [([y.year, y.year]) for y in Year.objects.all()]

    filial = forms.ChoiceField(choices=filial_choices, label='Филиал')
    locomotive_series = forms.ChoiceField(label='Серия локомотива')
    period_start = forms.ChoiceField(choices=period_choices, label='Начало периода')
    period_end = forms.ChoiceField(choices=period_choices, label='Конец периода')
