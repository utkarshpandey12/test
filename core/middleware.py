import time
from datetime import datetime


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        now = datetime.now()
        start = time.time()

        response = self.get_response(request)

        duration = time.time() - start

        with open("request_logs.txt", "a") as file:
            file.write(
                f" duration : {duration},url : {request.path},method : {request.method}"
            )

        return response
