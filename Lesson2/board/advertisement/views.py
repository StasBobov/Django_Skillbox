from django.shortcuts import render
from django.http import HttpResponse


# представление принимает объект на вход и возвращает HttpResponse на выходе
def advertisement_list(request, *args, **kwargs):
    list_1 = ['One', 'Two', 'Three']
    list_2 = ['4', '5', '6']
    list_3 = ['Семь', 'Восемь', 'Девять']
    advertisemens = ['Спиздил все курсы Skillbox, и ни о чём не жалею!',
                     'Вадим Шандрынов',
                     'Пиздюк в очках',
                     'Бородатый пиздюк в очках',
                     'Тип без очков очках',
                     'Неприятный тип по HTML',
                     'Contacts',
                     'About Us']
    # функция render параметр запроса - request, берёт шаблон advertisement_list и возвращает объект HttpResponse
    # в словарь можно передать переменные для использования в шаблоне
    # (ключ - название списка, значение - список объявлений)
    return render(request, 'advertisement/advertisement_list.html ',
                  {'advertisements': advertisemens, 'list_1': list_1, 'list_2': list_2, 'list_3': list_3})


def regions(request, *args, **kwargs):
    regions = ['Москва', 'Московская область', 'республика Алтай', 'Вологодская область']
    return render(request, 'advertisement/regions.html ', {'regions': regions})


def categories(request, *args, **kwargs):
    categories = ['личные вещи', 'транспорт', 'хобби', 'отдых']
    return render(request, 'advertisement/categories.html ', {'categories': categories})


def about(request, *args, **kwargs):
    about = ['Кто мы: Бесплатные объявления', 'Наша работа: Бесплатные объявления в вашем городе!']
    return render(request, 'advertisement/about.html ', {'about': about})


def contacts(request, *args, **kwargs):
    contacts = ['Контактный телефон: 8-800-708-19-45', 'email: sales@company.com']
    return render(request, 'advertisement/contacts.html ', {'contacts': contacts})


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