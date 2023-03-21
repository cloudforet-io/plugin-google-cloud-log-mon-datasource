import logging
from spaceone.core.manager import BaseManager
from cloudforet.monitoring.model.data_source_response_model import DataSourceMetadata
from cloudforet.monitoring.manager.metadata_manager import MetadataManager
from cloudforet.monitoring.connector.cloud_logging_connector import CloudLoggingConnector
from cloudforet.monitoring.conf.monitoring_conf import *

_LOGGER = logging.getLogger(__name__)


class DataSourceManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def init(params):
        options = params['options']
        meta_manager = MetadataManager()
        response_model = DataSourceMetadata({'_metadata': meta_manager.get_data_source_metadata()}, strict=False)
        return response_model.to_primitive()

    def verify(self, params):
        cloud_logging_connector: CloudLoggingConnector = self.locator.get_connector(CloudLoggingConnector, **params)
        cloud_logging_connector.verify()
