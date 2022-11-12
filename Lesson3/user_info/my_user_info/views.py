from django.shortcuts import render


def get_client_ip(request, *args, **kwargs):
    ip = request.META('REMOTE_ADDR')
    # передаём текущий IP в шаблон через контекст (контекст это словарь)
    return render(request, 'templates/user_info.html', {'ip_address': ip})

