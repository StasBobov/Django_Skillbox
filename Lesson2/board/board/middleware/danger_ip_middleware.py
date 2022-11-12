# не даёт зайти с запрещённого ip
from django.core.exceptions import PermissionDenied


class DangerIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = []
        ip = request.META['REMOTE_ADDR']
        if ip in allowed_ips:
            raise PermissionDenied

        response = self.get_response(request)

        return response