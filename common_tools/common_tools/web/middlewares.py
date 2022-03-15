import time


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        request.profile = {
            'name': 'Doncho',
        }
        start_time = time.time()
        # Connect with Django pipeline
        response = get_response(request, *args, **kwargs)

        end_time = time.time()

        print(f'{request.path} executed in {end_time - start_time}s')

        return response

    return middleware


def last_viewed_books_middleware(get_response):
    def middleware(request, *args, **kwargs):
        # if request.path != ...:
        #     return get_response(request, *args, **kwargs)
        request.books = request.session.get('last_viewed_books', [])
        return get_response(request, *args, **kwargs)

    return middleware

# def active_user_middleware(get_response):
#     def middleware(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             friends = request.user.friends
#             alert_user_online(friends, user)
#     return middleware
