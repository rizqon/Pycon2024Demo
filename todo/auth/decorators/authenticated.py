from auth.libraries.logto import client
from django.shortcuts import redirect
from functools import wraps
from django.urls import reverse

def authenticated(fetch_user_info: bool = False):
    def decorator(view_func):
        @wraps(view_func)
        async def wrapper(request, *args, **kwargs):
            # Check if the user is authenticated
            if client.isAuthenticated() is False:
                # If not, redirect to the login page
                return redirect(reverse('login'))

            # If the user is authenticated, fetch the user's information
            request.user_info = (
                await client.fetchUserInfo()
                if fetch_user_info
                else client.getIdTokenClaims()
            )

            # Call the view function
            return await view_func(request, *args, **kwargs)

        return wrapper

    return decorator
