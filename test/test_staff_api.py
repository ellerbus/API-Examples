# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.staff_api import StaffApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStaffApi(unittest.TestCase):
    """StaffApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.staff_api.StaffApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_staff_get_staff(self):
        """Test case for staff_get_staff

        Get staff members at a site.  # noqa: E501
        """
        pass

    def test_staff_get_staff_permissions(self):
        """Test case for staff_get_staff_permissions

        Get configured staff permissions for a staff member.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()