from django.core.exceptions import PermissionDenied


# вызываемый класс, вызывается автоматически из списка Middleware в файле settings.py
class FilterIPMiddleware:
    # так как запускается последней, то в ней запускается функция представления get_response
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1']
        # получаем из запроса ip адрес
        ip = request.META['REMOTE_ADDR']
        # with open('bug.txt', 'w') as f:
        #     f.write(ip)
        if ip not in allowed_ips:
            # если ip адрес не подходит, то возвращаем ответ с кодом ошибки 403
            raise PermissionDenied

        response = self.get_response(request)

        return response



