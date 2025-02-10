from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authienticated:
            if not request.path.startswith('/admin/'):
                profile = request.user.userprofile
                if not all([profile.contact_info,profile.address,profile.organization_name]):
                    messages.warning(request, 'Please complete your profile!')
                    return redirect(reverse('complete_profile'))
                
        response = self.get_response(request)

        return response