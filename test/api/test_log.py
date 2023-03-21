import json
import os
import unittest

from spaceone.core.unittest.runner import RichTestRunner
from spaceone.tester import TestCase, print_json

GOOGLE_APPLICATION_CREDENTIALS_PATH = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', None)

if GOOGLE_APPLICATION_CREDENTIALS_PATH is None:
    print("""
        ##################################################
        # ERROR 
        #
        # Configure your GCP credential first for test
        # https://console.cloud.google.com/apis/credentials

        ##################################################
        example)

        export GOOGLE_APPLICATION_CREDENTIALS="<PATH>" 
    """)
    exit


def _get_credentials():
    with open(GOOGLE_APPLICATION_CREDENTIALS_PATH) as json_file:
        json_data = json.load(json_file)
        return json_data


class TestLog(TestCase):

    def test_init(self):
        v_info = self.monitoring.DataSource.init({'options': {}})
        print_json(v_info)

    def test_verify(self):
        schema = ''
        options = {
        }
        secret_data = _get_credentials()
        self.monitoring.DataSource.verify({'schema': schema, 'options': options, 'secret_data': secret_data})

    def test_log_list(self):
        secret_data = _get_credentials()

        params = {
            'options': {},
            'secret_data': secret_data,
            'query': {
                'resource_id': '969092xxxxx',
                'name': 'projects/bluese-cloudone-20200113',
                'filter': [
                    {
                        'resource_type': 'gce_instance',
                        'labels': [
                            {
                                'key': 'resource.labels.instance_id',
                                'value': '969092xxxxx'
                            }
                        ]
                    }
                ]
            },
            'start': '2023-03-21T00:00:00Z',
            'end': '2023-03-21T23:00:00Z'
        }

        resource_stream = self.monitoring.Log.list(params)

        for res in resource_stream:
            print_json(res)


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
