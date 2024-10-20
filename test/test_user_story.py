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

from openapi_client.models.user_story import UserStory

class TestUserStory(unittest.TestCase):
    """UserStory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserStory:
        """Test UserStory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserStory`
        """
        model = UserStory()
        if include_optional:
            return UserStory(
                id = '',
                prd = '',
                as_a = '',
                i_want_to = '',
                so_that = '',
                freetext_override = '',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'RED',
                priority = '',
                tags = [
                    openapi_client.models.tag.Tag(
                        id = '', 
                        tag = '0', )
                    ],
                created_by = openapi_client.models.user_base.UserBase(
                    id = '', 
                    email = '0', 
                    first_name = '', 
                    last_name = '', ),
                organization = openapi_client.models.organization.Organization(
                    id = '', 
                    name = '0', )
            )
        else:
            return UserStory(
                prd = '',
        )
        """

    def testUserStory(self):
        """Test UserStory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
