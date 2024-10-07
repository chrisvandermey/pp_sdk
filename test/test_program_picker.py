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
import datetime

from pp_sdk.models.program_picker import ProgramPicker  # noqa: E501

class TestProgramPicker(unittest.TestCase):
    """ProgramPicker unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProgramPicker:
        """Test ProgramPicker
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProgramPicker`
        """
        model = ProgramPicker()  # noqa: E501
        if include_optional:
            return ProgramPicker(
                id = '',
                name = '0',
                description = '0'
            )
        else:
            return ProgramPicker(
        )
        """

    def testProgramPicker(self):
        """Test ProgramPicker"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()