$(document).ready(function() {
    function refresh_watchlist() {
        $('.watchlist-singlemovie').each(function(index, element) {
            $.getJSON(`http://www.omdbapi.com/?apikey=e4fbd650&i=${$(element).attr('id')}`)
                .done(function(response) {
                    if (response.Response == 'True') {
                        $(element).find('.watchlist-title').text(response.Title);
                    }
                });
        });
    }
    function bookmark_change(imdbID, element, action) {
        let reverse_action = (action == 'add') ? 'remove' : 'add';
        console.log(reverse_action);
        $.post("./", {
            action: action,
            imdbID: imdbID, //$(element).parents('.search-result').attr('id'),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        })
            .done(function(data) {
                if (data.status) {
                    if (action == 'add') $(`${data.html_response}`).appendTo($('#watchlist-modal .modal-body'));
                    else $(`.watchlist-singlemovie[id=${data.movie_id}]`).remove();
                    refresh_watchlist();
                    $('#watchlist-count').fadeTo('fast', 0).promise().then(() => {
                        $('#watchlist-count .badge').text(data.count);
                        $('#watchlist-count').fadeTo('fast', 1);
                    });
                    element.fadeTo('fast', 0).promise().then(() => {
                        $(element).toggleClass('bookmark-remove').toggleClass('bookmark-add');
                        $(element).find('img').attr('src', `/static/main_site/bookmark_${reverse_action}e.png`);
                        element.fadeTo('fast', 1);
                    });
                }
            });
    }
    refresh_watchlist();

    $('body').on('click', '.bookmark-add', function() {
        bookmark_change($(this).parents('.search-result').attr('id'), $(this), 'add');
    });
    $('body').on('click', '.bookmark-remove', function() {
        bookmark_change($(this).parents('.search-result').attr('id'), $(this), 'remove');
    });
    $('body').on('click', '.remove-from-watchlist', function() {
        let id = $(this).parents('.watchlist-singlemovie').attr('id');
        let el = $(`.search-result[id=${id}]`).find('.bookmark-remove');
        bookmark_change(id, el, 'remove');
    });
});