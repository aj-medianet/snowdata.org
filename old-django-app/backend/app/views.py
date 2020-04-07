from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def account(request):
    return render(request, "account.html")

def api_quick_start(request):
    return render(request, "api-quick-start.html")

def api_documentation(request):
    return render(request, "api-documentation.html")

def api_pricing(request):
    return render(request, "api-pricing.html")