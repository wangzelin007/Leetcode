import traceback
# from oslo_log import log as logging
# LOG = logging.getLogger(__name__)
# LOG.error('[module] [func] failed, e= {}'.format(traceback.format_exc()))
print('[module] [func] failed, e= {}'.format(traceback.format_exc()))

def fun_name():
    import sys
    print(sys._getframe().f_code.co_name)
z = fun_name
z()