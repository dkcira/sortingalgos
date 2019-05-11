# https://www.quora.com/How-do-you-measure-the-time-taken-by-a-function-to-execute-in-Python
import time

ENVIRONMENT_NAME = 'development'
# ENVIRONMENT_NAME = 'production'

def audit(func):
    """decorator to log information before and
    after a function execution.

    :param callable func: function.

    :returns: function result."""
    def decorator(*args, **kwargs):
        """
        decorates the given function and
        logs it's behavior and returns the
        function's result every time that
        function gets called.

        :param object args: function arguments.
        :param object kwargs: function keyword arguments.

        :returns: function result.
        """
        if 'development' not in ENVIRONMENT_NAME:
            return func(*args, **kwargs)

        start_time = time.time()
        try:
            # do some logging here.
            return func(*args, **kwargs)

        except Exception as ex:
            # do some error logging here.
            raise ex
        finally:
            end_time = time.time()
            print('duration of function call {name}: {seconds} sec'.format(
                name=func.__name__.upper(),
                seconds=((end_time - start_time) * 1000)))
                # do some logging here.
    return decorator
