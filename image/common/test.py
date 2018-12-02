import json
from django.test.testcases import TestCase

from rest_framework.test import APIClient


# noinspection PyShadowingBuiltins
class JSONAPIClient(APIClient):
    def post(self, path, data=None, format='json', content_type=None,
             follow=False, **extra):
        response = super(JSONAPIClient, self).post(
            path, data=data, format=format, content_type=content_type,
            follow=follow, **extra
        )
        if response.status_code == 200:
            response.json = json.loads(response.content.decode('utf-8'))
        else:
            response.json = None

        return response

    def get(self, *args, **kwargs):
        response = super(JSONAPIClient, self).get(
            *args, **kwargs
        )
        if response.status_code == 200:
            response.json = json.loads(response.content.decode('utf-8'))
        else:
            response.json = None

        return response


class JSONAPITestCase(TestCase):
    client_class = JSONAPIClient

    @classmethod
    def setUpTestData(cls):
        pass

    def assertOK(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)
        self.assertEqual(response.json['code'], 'OK')

    def assertErrorCode(self, response, code):
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json)
        self.assertEqual(response.json['code'], code)
