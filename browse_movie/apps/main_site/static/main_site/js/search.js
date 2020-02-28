const user_input = $('.search-input');
const endpoint = '/ajax-search/';
const delay_by_in_ms = 700;
let scheduled_function = false;

let ajax_call = function(endpoint, req_params, replaceable) {
    $.getJSON(endpoint, req_params)
        .done(function(response) {
            replaceable.fadeTo('fast', 0).promise().then(() => {
                console.log(response['html_content']);
                replaceable.html(response['html_content']);
                replaceable.fadeTo('fast', 1);
            })
        })
}

user_input.keyup(function() {
    console.log('aa');
    const req_params = {
        q: $(this).val()
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function);
    }
    replaceable = $(this).next('.search-results');
    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, req_params, replaceable);
});
