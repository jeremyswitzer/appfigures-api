
class AppFiguresUrlBuilder(object):
    def __init__(self, base_url):
        self._base_url = base_url
        
    def construct_url(self, *args):
        parts = [self._base_url]
        parts.extend(args)
        parts = [str(p).strip('/ ') for p in parts]
        url = '/'.join(parts)
        return url
        
        