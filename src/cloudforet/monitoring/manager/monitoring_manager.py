import copy
import logging
from spaceone.core.manager import BaseManager

from cloudforet.monitoring.connector import CloudLoggingConnector


class MonitoringManager(BaseManager):
    def __init__(self, transaction):
        super().__init__(transaction)

    def list_logs(self, params):
        cloud_logging_conn: CloudLoggingConnector = self.locator.get_connector(CloudLoggingConnector, **params)

        logs = cloud_logging_conn.list_log_entries(params)
        print(logs)
