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

from pp_sdk.models.api_chat_upload_file200_response import ApiChatUploadFile200Response

class TestApiChatUploadFile200Response(unittest.TestCase):
    """ApiChatUploadFile200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiChatUploadFile200Response:
        """Test ApiChatUploadFile200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiChatUploadFile200Response`
        """
        model = ApiChatUploadFile200Response()
        if include_optional:
            return ApiChatUploadFile200Response(
                message = '',
                filename = '',
                doc_id = ''
            )
        else:
            return ApiChatUploadFile200Response(
        )
        """

    def testApiChatUploadFile200Response(self):
        """Test ApiChatUploadFile200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()