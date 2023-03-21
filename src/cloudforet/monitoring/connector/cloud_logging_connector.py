import logging
from cloudforet.monitoring.libs.google_cloud_connector import GoogleCloudConnector

_LOGGER = logging.getLogger(__name__)


class CloudLoggingConnector(GoogleCloudConnector):
    google_client_service = 'logging'
    version = 'v2'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list_log_entries(self, params):
        print(params)
        query = params['query']
        start = params['start']
        end = params['end']

        _query = {
            'filter': self._generate_logging_filter(query, start, end),
            'orderBy': 'timestamp desc'
        }
        print(_query)
        request = self.client.entries().list(**_query)

        logs = []
        while request is not None:
            response = request.execute()
            logs = [log for log in response.get('entries', [])]
            request = self.client.entries().list_next(previous_request=request, previous_response=response)
        return logs

    @staticmethod
    def _generate_logging_filter(query, start, end):
        logging_filter = ''
        log_filters = query.get('filters', [])
        for log_filter in log_filters:
            _filter = []
            resource_type = log_filter.get('resource_type')
            labels = log_filter.get('labels', {})
            if resource_type:
                _filter.append(f'resource.type={resource_type}')
            if labels:
                for key, value in labels.items():
                    _filter.append(f'{key}={value}')
            if logging_filter:
                logging_filter += f' OR ({" AND ".join(_filter)})'
            else:
                logging_filter += f'({" AND ".join(_filter)})'

        if logging_filter:
            logging_filter += f' AND timestamp >= "{start}" AND timestamp <= "{end}"'
        else:
            logging_filter += f'timestamp >= "{start}" AND timestamp <= "{end}"'

        return logging_filter
