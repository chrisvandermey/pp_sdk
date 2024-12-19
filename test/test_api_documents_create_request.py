# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: chris@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pp_sdk.models.api_documents_create_request import ApiDocumentsCreateRequest

class TestApiDocumentsCreateRequest(unittest.TestCase):
    """ApiDocumentsCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDocumentsCreateRequest:
        """Test ApiDocumentsCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDocumentsCreateRequest`
        """
        model = ApiDocumentsCreateRequest()
        if include_optional:
            return ApiDocumentsCreateRequest(
                title = '',
                body = '',
                type = '',
                publishing_state = 'PENDING_REVIEW',
                document_covering_period_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                document_covering_period_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                tags = [
                    ''
                    ],
                stakeholder_users = [
                    ''
                    ],
                program = ''
            )
        else:
            return ApiDocumentsCreateRequest(
                title = '',
                body = '',
                type = '',
        )
        """

    def testApiDocumentsCreateRequest(self):
        """Test ApiDocumentsCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()