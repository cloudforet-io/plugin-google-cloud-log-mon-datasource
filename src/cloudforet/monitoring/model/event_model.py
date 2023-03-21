from schematics import Model
from schematics.types import ModelType, StringType, BaseType, DictType, IntType, BooleanType, UnionType


class Display(Model):
    pass


class MonitoredResource(Model):
    type = StringType()
    labels = DictType(StringType)


class HttpRequest(Model):
    request_method = StringType(deserialize_from='requestMethod')
    request_url = StringType(deserialize_from='requestUrl')
    request_size = StringType(deserialize_from='requestSize')
    status = IntType()
    response_size = StringType(deserialize_from='responseSize')
    user_agent = StringType(deserialize_from='userAgent')
    remote_ip = StringType(deserialize_from='remoteIp')
    server_ip = StringType(deserialize_from='serverIp')
    referer = StringType()
    latency = StringType()
    cache_lookup = BooleanType(deserialize_from='cacheLookup')
    cache_hit = BooleanType(deserialize_from='cacheHit')
    cache_validated_with_origin_server = BooleanType(deserialize_from='cacheValidatedWithOriginServer')
    cache_fill_bytes = StringType(deserialize_from='cacheFillBytes')
    protocol = StringType()


class LogEntryOperation(Model):
    id = StringType()
    producer = StringType()
    first = BooleanType()
    last = BooleanType()


class LogEntrySourceLocation(Model):
    file = StringType()
    function = StringType()
    line = StringType()


class LogSplit(Model):
    uid = StringType()
    index = IntType()
    total_splits = IntType(deserialize_from='totalSplits')


class Event(Model):
    insert_id = StringType(deserialize_from='insertId')
    log_name = StringType(deserialize_from='logName')
    resource = ModelType(MonitoredResource)
    timestamp = StringType()
    receive_timestamp = StringType(deserialize_from='receiveTimestamp')
    severity = StringType()
    http_request = ModelType(HttpRequest)
    labels = DictType(StringType)
    operation = ModelType(LogEntryOperation)
    trace = StringType()
    span_id = StringType(deserialize_from='spanId')
    trace_sampled = BooleanType(deserialize_from='traceSampled')
    source_location = ModelType(LogEntrySourceLocation, deserialize_from='sourceLocation')
    split = ModelType(LogSplit)
    proto_payload = BaseType(deserialize_from='protoPayload')
    display = ModelType(Display)

    class Options:
        serialize_when_none = False
