from rest_framework import status
from rest_framework.response import Response


class CommonResponseUtil:
    @staticmethod
    def response_not_found(message='Not found.'):
        return Response({
            "detail": message,
            "status_code": 404
        }, status=status.HTTP_404_NOT_FOUND)
