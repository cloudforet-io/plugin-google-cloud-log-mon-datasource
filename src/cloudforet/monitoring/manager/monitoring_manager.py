import logging
from spaceone.core.manager import BaseManager
from cloudforet.monitoring.connector import CloudLoggingConnector
from cloudforet.monitoring.model.log_model import Event, Log
from cloudforet.monitoring.error.custom_error import ERROR_CONVERT_EVENT

_LOGGER = logging.getLogger(__name__)


class MonitoringManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list_logs(self, params):
        query = params.get('query', {})
        if not query:
            return Log({'results': []})

        cloud_logging_conn: CloudLoggingConnector = self.locator.get_connector('CloudLoggingConnector', **params)

        for logs in cloud_logging_conn.list_log_entries(params):

            event_vos = []
            for log in logs:
                if log.get('protoPayload'):
                    try:
                        event_vos.append(Event(log))
                    except Exception as e:
                        raise ERROR_CONVERT_EVENT(event=log, error=e)

            yield Log({'results': event_vos})
