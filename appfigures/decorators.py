def exception_check(fn):
    def wrapper(self, *args, **kwargs):
        result = fn(self, *args, **kwargs)
        if "status" in result:
            import sys, errors
            ex = errors.EXCEPTIONS[result["status"]]
            raise ex, ex(result["message"], result["additional"], result["reference"]), sys.exc_info()[2]
        return result
    return wrapper
