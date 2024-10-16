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

from openapi_client.models.goal import Goal

class TestGoal(unittest.TestCase):
    """Goal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Goal:
        """Test Goal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Goal`
        """
        model = Goal()
        if include_optional:
            return Goal(
                id = '',
                name = '0',
                goal_language = '0',
                description = '',
                why_it_matters = '',
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                original_due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                current_due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                prd = [
                    openapi_client.models.prd.PRD(
                        id = '', 
                        title = '0', 
                        programs = [
                            openapi_client.models.program_base.ProgramBase(
                                id = '', 
                                name = '0', )
                            ], 
                        description = '', 
                        body = '', 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'DRAFT', 
                        tags = [
                            openapi_client.models.tag.Tag(
                                id = '', 
                                tag = '0', )
                            ], 
                        owner_user = openapi_client.models.user_base.UserBase(
                            id = '', 
                            email = '0', 
                            first_name = '', 
                            last_name = '', ), 
                        stakeholder_users = [
                            openapi_client.models.user_base.UserBase(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', )
                            ], 
                        created_by = , 
                        organization = openapi_client.models.organization.Organization(
                            id = '', 
                            name = '0', ), )
                    ],
                owner_users = '',
                program = '',
                program_dependent_goals = [
                    openapi_client.models.program.Program(
                        id = '', 
                        name = '0', 
                        description = '', 
                        principal_users = [
                            openapi_client.models.user.User(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', 
                                is_active = True, 
                                is_staff = True, 
                                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                organization = openapi_client.models.organization.Organization(
                                    id = '', 
                                    name = '0', ), 
                                address = openapi_client.models.address.Address(
                                    street_address = '0', 
                                    city = '0', 
                                    state = '0', 
                                    postal_code = '0', 
                                    country = '0', ), 
                                user_facts = openapi_client.models.user_facts.User facts(), 
                                walkthrough_status = openapi_client.models.walkthrough_status.Walkthrough status(), )
                            ], 
                        stakeholder_users = [
                            openapi_client.models.user.User(
                                id = '', 
                                email = '0', 
                                first_name = '', 
                                last_name = '', 
                                is_active = True, 
                                is_staff = True, 
                                date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                user_facts = openapi_client.models.user_facts.User facts(), 
                                walkthrough_status = openapi_client.models.walkthrough_status.Walkthrough status(), )
                            ], 
                        parent = '', 
                        tags = [
                            openapi_client.models.tag.Tag(
                                id = '', 
                                tag = '0', )
                            ], 
                        created_by = , 
                        created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        organization = openapi_client.models.organization.Organization(
                            id = '', 
                            name = '0', ), )
                    ],
                stakeholders_users = [
                    openapi_client.models.user.User(
                        id = '', 
                        email = '0', 
                        first_name = '', 
                        last_name = '', 
                        is_active = True, 
                        is_staff = True, 
                        date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        organization = openapi_client.models.organization.Organization(
                            id = '', 
                            name = '0', ), 
                        address = openapi_client.models.address.Address(
                            street_address = '0', 
                            city = '0', 
                            state = '0', 
                            postal_code = '0', 
                            country = '0', ), 
                        user_facts = openapi_client.models.user_facts.User facts(), 
                        walkthrough_status = openapi_client.models.walkthrough_status.Walkthrough status(), )
                    ],
                tags = [
                    openapi_client.models.tag.Tag(
                        id = '', 
                        tag = '0', )
                    ],
                version = -2147483648,
                version_summary = '',
                created_by = openapi_client.models.user.User(
                    id = '', 
                    email = '0', 
                    first_name = '', 
                    last_name = '', 
                    is_active = True, 
                    is_staff = True, 
                    date_joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_login = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    organization = openapi_client.models.organization.Organization(
                        id = '', 
                        name = '0', ), 
                    address = openapi_client.models.address.Address(
                        street_address = '0', 
                        city = '0', 
                        state = '0', 
                        postal_code = '0', 
                        country = '0', ), 
                    user_facts = openapi_client.models.user_facts.User facts(), 
                    walkthrough_status = openapi_client.models.walkthrough_status.Walkthrough status(), ),
                organization = ''
            )
        else:
            return Goal(
                name = '0',
                goal_language = '0',
        )
        """

    def testGoal(self):
        """Test Goal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
