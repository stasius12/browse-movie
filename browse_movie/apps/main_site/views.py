from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .api_call import APICall


@login_required
def home_page(request):
    return render(request, 'main_site/home_page.html', {})


def ajax_search(request):
    if request.is_ajax():
        q = request.GET.get('q', None)
        p = request.GET.get('p', 1)
        if q is not None:
            call = APICall(search=q, page=p)
            results = {'results': call.get_results()}
            search_results = render_to_string('main_site/search_results_snippet.html', results)
            return JsonResponse({
                'status': call.response,
                'search': q,
                'html_content': search_results,
                'next_page': call.get_next_page()
            })
