from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .api_call import APICall



def home_page(request):
    return render(request, 'main_site/home_page.html', {})


def ajax_search(request):
    if request.is_ajax():
        q = request.GET.get('q', None)
        if q is not None:
            call = APICall(search=q)
            # results = {'results': ['ala', 'ma', 'kota']}
            results = {
                'results': call.get_data()
            }
            search_results = render_to_string('main_site/search_results_snippet.html', results)
            return JsonResponse({
                'html_content': search_results
            })
