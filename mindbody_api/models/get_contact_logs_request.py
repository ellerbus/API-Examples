# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetContactLogsRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'client_id': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'staff_ids': 'list[int]',
        'show_system_generated': 'bool',
        'type_ids': 'list[int]',
        'subtype_ids': 'list[int]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'staff_ids': 'StaffIds',
        'show_system_generated': 'ShowSystemGenerated',
        'type_ids': 'TypeIds',
        'subtype_ids': 'SubtypeIds',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, client_id=None, start_date=None, end_date=None, staff_ids=None, show_system_generated=None, type_ids=None, subtype_ids=None, limit=None, offset=None):  # noqa: E501
        """GetContactLogsRequest - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._start_date = None
        self._end_date = None
        self._staff_ids = None
        self._show_system_generated = None
        self._type_ids = None
        self._subtype_ids = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.client_id = client_id
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if staff_ids is not None:
            self.staff_ids = staff_ids
        if show_system_generated is not None:
            self.show_system_generated = show_system_generated
        if type_ids is not None:
            self.type_ids = type_ids
        if subtype_ids is not None:
            self.subtype_ids = subtype_ids
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def client_id(self):
        """Gets the client_id of this GetContactLogsRequest.  # noqa: E501

        The ID of the client whose contact logs are being requested.  # noqa: E501

        :return: The client_id of this GetContactLogsRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetContactLogsRequest.

        The ID of the client whose contact logs are being requested.  # noqa: E501

        :param client_id: The client_id of this GetContactLogsRequest.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def start_date(self):
        """Gets the start_date of this GetContactLogsRequest.  # noqa: E501

        Filters the results to contact logs created on or after this date.<br />  Default: **the current date**  # noqa: E501

        :return: The start_date of this GetContactLogsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetContactLogsRequest.

        Filters the results to contact logs created on or after this date.<br />  Default: **the current date**  # noqa: E501

        :param start_date: The start_date of this GetContactLogsRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this GetContactLogsRequest.  # noqa: E501

        Filters the results to contact logs created before this date.<br />  Default: **the start date**  # noqa: E501

        :return: The end_date of this GetContactLogsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetContactLogsRequest.

        Filters the results to contact logs created before this date.<br />  Default: **the start date**  # noqa: E501

        :param end_date: The end_date of this GetContactLogsRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def staff_ids(self):
        """Gets the staff_ids of this GetContactLogsRequest.  # noqa: E501

        Filters the results to return contact logs assigned to one or more staff IDs.  # noqa: E501

        :return: The staff_ids of this GetContactLogsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._staff_ids

    @staff_ids.setter
    def staff_ids(self, staff_ids):
        """Sets the staff_ids of this GetContactLogsRequest.

        Filters the results to return contact logs assigned to one or more staff IDs.  # noqa: E501

        :param staff_ids: The staff_ids of this GetContactLogsRequest.  # noqa: E501
        :type: list[int]
        """

        self._staff_ids = staff_ids

    @property
    def show_system_generated(self):
        """Gets the show_system_generated of this GetContactLogsRequest.  # noqa: E501

        When `true`, system-generated contact logs are returned in the results.<br />  Default: **false**  # noqa: E501

        :return: The show_system_generated of this GetContactLogsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._show_system_generated

    @show_system_generated.setter
    def show_system_generated(self, show_system_generated):
        """Sets the show_system_generated of this GetContactLogsRequest.

        When `true`, system-generated contact logs are returned in the results.<br />  Default: **false**  # noqa: E501

        :param show_system_generated: The show_system_generated of this GetContactLogsRequest.  # noqa: E501
        :type: bool
        """

        self._show_system_generated = show_system_generated

    @property
    def type_ids(self):
        """Gets the type_ids of this GetContactLogsRequest.  # noqa: E501

        Filters the results to contact logs assigned one or more of these type IDs.  # noqa: E501

        :return: The type_ids of this GetContactLogsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._type_ids

    @type_ids.setter
    def type_ids(self, type_ids):
        """Sets the type_ids of this GetContactLogsRequest.

        Filters the results to contact logs assigned one or more of these type IDs.  # noqa: E501

        :param type_ids: The type_ids of this GetContactLogsRequest.  # noqa: E501
        :type: list[int]
        """

        self._type_ids = type_ids

    @property
    def subtype_ids(self):
        """Gets the subtype_ids of this GetContactLogsRequest.  # noqa: E501

        Filters the results to contact logs assigned one or more of these subtype IDs.  # noqa: E501

        :return: The subtype_ids of this GetContactLogsRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._subtype_ids

    @subtype_ids.setter
    def subtype_ids(self, subtype_ids):
        """Sets the subtype_ids of this GetContactLogsRequest.

        Filters the results to contact logs assigned one or more of these subtype IDs.  # noqa: E501

        :param subtype_ids: The subtype_ids of this GetContactLogsRequest.  # noqa: E501
        :type: list[int]
        """

        self._subtype_ids = subtype_ids

    @property
    def limit(self):
        """Gets the limit of this GetContactLogsRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetContactLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetContactLogsRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetContactLogsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetContactLogsRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetContactLogsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetContactLogsRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetContactLogsRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetContactLogsRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetContactLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
