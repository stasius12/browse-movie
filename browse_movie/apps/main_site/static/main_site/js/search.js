const user_input = $('.search-input');
const more_results_btn = $('.see-more-btn');
const endpoint = '/ajax-search/';
const delay_by_in_ms = 700;
let scheduled_function = false;

/*
var example_data = {
    "Title": "Star Wars: Episode IV - A New Hope",
    "Year": "1977",
    "Rated": "PG",
    "Released": "25 May 1977",
    "Runtime": "121 min",
    "Genre": "Action, Adventure, Fantasy, Sci-Fi",
    "Director": "George Lucas",
    "Writer": "George Lucas",
    "Actors": "Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing",
    "Plot": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.",
    "Language": "English",
    "Country": "USA",
    "Awards": "Won 6 Oscars. Another 52 wins & 28 nominations.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "8.6/10"
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": "93%"
        },
        {
            "Source": "Metacritic",
            "Value": "90/100"
        }
    ],
    "Metascore": "90",
    "imdbRating": "8.6",
    "imdbVotes": "1,170,893",
    "imdbID": "tt0076759",
    "Type": "movie",
    "DVD": "21 Sep 2004",
    "BoxOffice": "N/A",
    "Production": "20th Century Fox",
    "Website": "N/A",
    "Response": "True"
} */

function download_more_data() {
    $('.search-result').each(function(index, element) {
        $.getJSON(`http://www.omdbapi.com/?apikey=e4fbd650&i=${$(element).attr('id')}`)
            .done(function(response) {
                if (response.Response == 'True') {
                    $(element).find('.imdb-rating-inner').text(response.imdbRating);
                    $(element).find('.runtime').text(response.Runtime);
                    $(element).find('.genre').text(response.Genre);
                    $(element).find('.released').text(response.Released);
                    $(element).find('.country').text(`(${response.Country})`);
                }
            });
    });
}

let ajax_call = function(endpoint, req_params, replaceable, append) {
    $.getJSON(endpoint, req_params)
        .done(function(response) {
            if (response['search'] != '') {
                replaceable.fadeTo('fast', 0).promise().then(() => {
                    let html_content = response['html_content'];
                    let next_page = response['next_page'];
                    if (append && response['status']) {
                        $(`${html_content}`).appendTo(replaceable);
                        replaceable.fadeTo('fast', 1);
                        download_more_data();
                    } else {
                        replaceable.html(html_content);
                        replaceable.fadeTo('fast', 1);
                        download_more_data();
                    }
                    if (next_page) {
                        more_results_btn.parents('.row').show();
                        more_results_btn.data('next-page', next_page);
                    } else more_results_btn.parents('.row').hide();
                });
            }
        })
}

user_input.keyup(function() {
    const req_params = {
        q: $(this).val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function);
    }
    replaceable = $(this).next('.search-results');
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, req_params, replaceable, false);
});

more_results_btn.click(function() {
    const req_params = {
        q: user_input.val(),
        p: more_results_btn.data('next-page')
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function);
    }
    replaceable = user_input.next('.search-results');
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, req_params, replaceable, true);
});

