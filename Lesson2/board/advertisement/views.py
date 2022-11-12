from django.shortcuts import render
from django.http import HttpResponse


# представление принимает объект на вход и возвращает HttpResponse на выходе
def advertisement_list(request, *args, **kwargs):
    advertisemens = ['Спиздил все курсы Skillbox, и ни о чём не жалею!',
                     'Вадим Шандрынов',
                     'Пиздюк в очках',
                     'Бородатый пиздюк в очках',
                     'Тип без очков очках',
                     'Неприятный тип по HTML']
    # функция render параметр запроса - request, берёт шаблон advertisement_list и возвращает объект HttpResponse
    # в словарь можно передать переменные для использования в шаблоне
    # (ключ - название списка, значение - список объявлений)
    return render(request, 'advertisement/advertisement_list.html ', {'advertisements': advertisemens})


def advertisement_snatch(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_snatch.html ', {})


def advertisement_Vadim(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_Vadim.html ', {})

def advertisement_pizduk(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_pizduk.html ', {})


def advertisement_pizduk_s_borodoy(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_pizduk_s_borodoy.html ', {})


def advertisement_tip(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_tip.html ', {})


def advertisement_not_like(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_not_like.html ', {})