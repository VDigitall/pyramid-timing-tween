import time
from pyramid.settings import asbool
import logging

log = logging.getLogger(__name__)


def timing_tween_factory(handler, registry):
    if asbool(registry.settings.get('do_timing')):
        # if timing support is enabled, return a wrapper
        def timing_tween(request):
            start = time.time()
            try:
                response = handler(request)
            finally:
                delta = time.time() - start
                log_info = {
                    'REQUEST_PROCESS_TIME': delta,
                    'REQUEST_METHOD': request.method,
                    'RESPONSE_CODE': response.status_code
                }
                log.debug('The request {REQUEST_METHOD} took '
                          '{REQUEST_PROCESS_TIME} seconds with status code '
                          '{RESPONSE_CODE}'.format(**log_info),
                          extra=log_info)
            return response
        return timing_tween
    # if timing support is not enabled, return the original
    # handler
    return handler


def includeme(config):
    log.info('Init timing tween factory')
    config.add_tween('timingtween.timingtween.tween.timing_tween_factory')
