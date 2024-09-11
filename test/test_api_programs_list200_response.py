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

from pp_sdk.models.api_programs_list200_response import ApiProgramsList200Response

class TestApiProgramsList200Response(unittest.TestCase):
    """ApiProgramsList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiProgramsList200Response:
        """Test ApiProgramsList200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiProgramsList200Response`
        """
        model = ApiProgramsList200Response()
        if include_optional:
            return ApiProgramsList200Response(
                count = 56,
                next = '',
                previous = '',
                results = [
                    pp_sdk.models.program.Program(
                        id = '', 
                        name = '0', 
                        description = '', 
                        charter = '', 
                        principal_users = [
                            pp_sdk.models.user.User(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', 
                                is_active = True, 
                                is_staff = True, 
                                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                organization = pp_sdk.models.organization.Organization(
                                    id = '', 
                                    name = '0', ), 
                                address = pp_sdk.models.address.Address(
                                    street_address = '0', 
                                    city = '0', 
                                    state = '0', 
                                    postal_code = '0', 
                                    country = '0', ), 
                                user_facts = pp_sdk.models.user_facts.User facts(), 
                                walkthrough_status = pp_sdk.models.walkthrough_status.Walkthrough status(), )
                            ], 
                        stakeholder_users = [
                            pp_sdk.models.user.User(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', 
                                is_active = True, 
                                is_staff = True, 
                                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                user_facts = pp_sdk.models.user_facts.User facts(), 
                                walkthrough_status = pp_sdk.models.walkthrough_status.Walkthrough status(), )
                            ], 
                        parent = '', 
                        tags = [
                            pp_sdk.models.tag.Tag(
                                id = '', 
                                tag = '0', )
                            ], 
                        created_by = , 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        organization = pp_sdk.models.organization.Organization(
                            id = '', 
                            name = '0', ), )
                    ]
            )
        else:
            return ApiProgramsList200Response(
                count = 56,
                results = [
                    pp_sdk.models.program.Program(
                        id = '', 
                        name = '0', 
                        description = '', 
                        charter = '', 
                        principal_users = [
                            pp_sdk.models.user.User(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', 
                                is_active = True, 
                                is_staff = True, 
                                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                organization = pp_sdk.models.organization.Organization(
                                    id = '', 
                                    name = '0', ), 
                                address = pp_sdk.models.address.Address(
                                    street_address = '0', 
                                    city = '0', 
                                    state = '0', 
                                    postal_code = '0', 
                                    country = '0', ), 
                                user_facts = pp_sdk.models.user_facts.User facts(), 
                                walkthrough_status = pp_sdk.models.walkthrough_status.Walkthrough status(), )
                            ], 
                        stakeholder_users = [
                            pp_sdk.models.user.User(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', 
                                is_active = True, 
                                is_staff = True, 
                                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                user_facts = pp_sdk.models.user_facts.User facts(), 
                                walkthrough_status = pp_sdk.models.walkthrough_status.Walkthrough status(), )
                            ], 
                        parent = '', 
                        tags = [
                            pp_sdk.models.tag.Tag(
                                id = '', 
                                tag = '0', )
                            ], 
                        created_by = , 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        organization = pp_sdk.models.organization.Organization(
                            id = '', 
                            name = '0', ), )
                    ],
        )
        """

    def testApiProgramsList200Response(self):
        """Test ApiProgramsList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
