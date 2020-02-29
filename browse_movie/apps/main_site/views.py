from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from .api_call import APICall
from .models import WatchList


@login_required
def home_page(request):
    if request.is_ajax() and 'imdbID' in request.POST:
        imdbID = request.POST['imdbID']
        watchlist, _ = WatchList.objects.get_or_create(user=request.user)
        if request.POST.get('action', None) == 'add':
            count = watchlist.add_movie(imdbID)
            html_response = render_to_string('main_site/watchlist_singlemovie_snippet.html', {
                'movie_id': imdbID
            })
            return JsonResponse({
                'status': count is not None,
                'count': count,
                'html_response': html_response,
            })
        else:
            count = watchlist.remove_movie(imdbID)
            return JsonResponse({
                'status': count is not None,
                'count': count,
                'movie_id': imdbID,
            })
    return render(request, 'main_site/home_page.html', {})


def ajax_search(request):
    if request.is_ajax():
        q = request.GET.get('q', None)
        p = request.GET.get('p', 1)
        if q is not None:
            call = APICall(search=q, page=p)
            results = {
                'results': call.get_results(),
                'user': request.user,
            }
            search_results = render_to_string('main_site/search_results_snippet.html', results)
            return JsonResponse({
                'status': call.response,
                'search': q,
                'html_content': search_results,
                'next_page': call.get_next_page()
            })
