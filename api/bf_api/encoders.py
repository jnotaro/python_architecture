import datetime
from json import JSONEncoder
from typing import Any

from bf_shop.entities import BaseEntity, Client


class ApiJsonEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime.datetime, datetime.date)):
            serial = obj.isoformat()
            return serial

        if isinstance(obj, Client):
            return {"name": obj.name}

        if isinstance(obj, BaseEntity):
            return {key: value for key, value in vars(obj).items() if value is not None}

        return JSONEncoder.default(self, obj)
