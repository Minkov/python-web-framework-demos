import logging

from exceptions_demos.web.views import AppException, internal_error, InternalErrorView


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            # fails silently
            # return RedirectView()
            logging.critical('Critical: I am Doncho')
            logging.error('Error: I am Doncho')
            logging.warning('Warning: I am Doncho')
            logging.info('Info: I am Doncho')
            logging.debug('Debug: I am Doncho')
            return InternalErrorView.as_view()(request)
            # return internal_error(request)

        return response

    return middleware
