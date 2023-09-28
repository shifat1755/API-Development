from django.http import JsonResponse

def home_page(request):
    print('Home page is requested')
    jsonfile=[1,2,3,5]
    return JsonResponse(jsonfile,safe=False)