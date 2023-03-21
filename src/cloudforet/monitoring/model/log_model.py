from schematics import Model
from schematics.types import ModelType, ListType
from cloudforet.monitoring.model.event_model import Event


class Log(Model):
    results = ListType(ModelType(Event), default=[])
