from django.shortcuts import redirect

class UserTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Check the user type and restrict access based on it
            user_type = request.user.user_type
            if user_type == 'admin':
                return self.get_response(request)
            else:
                # Redirect to an unauthorized page or raise a PermissionDenied exception
                return redirect('unauthorized_access')

        return self.get_response(request)
