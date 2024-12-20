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

from pp_sdk.models.api_prds_partial_update_request import ApiPrdsPartialUpdateRequest

class TestApiPrdsPartialUpdateRequest(unittest.TestCase):
    """ApiPrdsPartialUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiPrdsPartialUpdateRequest:
        """Test ApiPrdsPartialUpdateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiPrdsPartialUpdateRequest`
        """
        model = ApiPrdsPartialUpdateRequest()
        if include_optional:
            return ApiPrdsPartialUpdateRequest(
                title = '',
                description = '',
                body = '',
                status = 'DRAFT',
                due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                tags = [
                    ''
                    ],
                stakeholder_users = [
                    ''
                    ],
                programs = [
                    ''
                    ]
            )
        else:
            return ApiPrdsPartialUpdateRequest(
        )
        """

    def testApiPrdsPartialUpdateRequest(self):
        """Test ApiPrdsPartialUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
