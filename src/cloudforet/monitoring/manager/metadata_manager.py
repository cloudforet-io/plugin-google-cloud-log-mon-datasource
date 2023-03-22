import logging
from spaceone.core.manager import BaseManager
from cloudforet.monitoring.model.metadata.metadata import LogMetadata
from cloudforet.monitoring.model.metadata.metadata_dynamic_field import TextDyField, DateTimeDyField, EnumDyField, \
    MoreField

_LOGGER = logging.getLogger(__name__)


class MetadataManager(BaseManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def get_data_source_metadata():
        metadata = LogMetadata.set_fields(
            name='cloud-logging-table',
            fields=[
                MoreField.data_source('Event Name', 'log_name', options={
                    'layout': {
                        'name': 'Event Details',
                        'type': 'popup',
                        'options': {
                            'layout': {
                                'type': 'raw'
                            }
                        }
                    }
                }),
                EnumDyField.data_source('Severity', 'severity', default_badge={
                    'red.500': ['ALERT', 'EMERGENCY'],
                    'coral.500': ['ERROR', 'CRITICAL'],
                    'yellow.300': ['NOTICE', 'WARNING'],
                    'green.500': ['NOTICE'],
                    'gray.500': ['DEBUG', 'INFO'],
                    'black': ['DEFAULT']
                }),
                TextDyField.data_source('Method name', 'proto_payload.methodName'),
                TextDyField.data_source('User Name', 'proto_payload.authenticationInfo.principalEmail'),
                DateTimeDyField.data_source('Event Time', 'timestamp'),
            ]
        )
        return metadata
