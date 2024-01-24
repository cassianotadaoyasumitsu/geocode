import re
from logging import Filter


class GeocodeLogFilter(Filter):
    def filter(self, record):
        if "GET /geocode/json" in record.getMessage() and "200" in record.getMessage() and "cached" not in record.getMessage():
            pattern = r'key=([^&]*)'
            replacement = 'key=****'
            record.msg = re.sub(pattern, replacement, record.msg)
            if record.args:
                record.args = tuple(re.sub(pattern, replacement, str(arg)) for arg in record.args)
            return True
        return False
