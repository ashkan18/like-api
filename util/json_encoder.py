import json
import datetime
from time import mktime

__author__ = 'Ashkan'


class LikeAPIJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)

