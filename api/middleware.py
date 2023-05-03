
class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        print(response)
        response['Access-Control-Allow-Origin'] = '*' # or specify a specific domain instead of '*'
        return response