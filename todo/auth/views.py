from django.shortcuts import render, redirect
from .libraries.logto import client
from django.conf import settings

# Create your views here.
async def login(request):
    # Ask Logto to redirect back to the callback view
    # after the user has signed in
    url = await client.signIn(
        redirectUri=settings.LOGTO['redirect_uri']
    )

    # Redirect the user to the Logto login page
    return redirect(url)

async def logout(request):
    # Get the URL for the logout page
    url = await client.signOut(
        # Redirect back to the root of the website
        # after the user has signed out
        postLogoutRedirectUri=settings.LOGTO['logout_uri']
    )

    # Redirect the user to the logout page
    return redirect(url)

async def callback(request):
    absolute_uri = request.build_absolute_uri()

    try:
        # Process the response from the Logto callback
        await client.handleSignInCallback(absolute_uri)
    except Exception as e:
        # If there is an error, raise it
        raise e
    
    # Redirect the user to the root of the website
    return redirect('index')
