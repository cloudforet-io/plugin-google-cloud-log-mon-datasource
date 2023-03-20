import copy
import logging
from spaceone.core.manager import BaseManager


class MonitoringManager(BaseManager):
    def __init__(self, transaction):
        super().__init__(transaction)
