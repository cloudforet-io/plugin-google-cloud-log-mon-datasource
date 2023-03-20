import logging
from cloudforet.monitoring.libs.google_connector import GoogleConnector

_LOGGER = logging.getLogger(__name__)


class CloudTrailConnector(GoogleConnector):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
