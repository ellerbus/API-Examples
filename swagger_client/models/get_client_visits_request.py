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


class GetClientVisitsRequest(object):
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
        'client_associated_sites_offset': 'int',
        'cross_regional_lookup': 'bool',
        'end_date': 'datetime',
        'start_date': 'datetime',
        'unpaids_only': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'client_associated_sites_offset': 'ClientAssociatedSitesOffset',
        'cross_regional_lookup': 'CrossRegionalLookup',
        'end_date': 'EndDate',
        'start_date': 'StartDate',
        'unpaids_only': 'UnpaidsOnly',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, client_id=None, client_associated_sites_offset=None, cross_regional_lookup=None, end_date=None, start_date=None, unpaids_only=None, limit=None, offset=None):  # noqa: E501
        """GetClientVisitsRequest - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._client_associated_sites_offset = None
        self._cross_regional_lookup = None
        self._end_date = None
        self._start_date = None
        self._unpaids_only = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.client_id = client_id
        if client_associated_sites_offset is not None:
            self.client_associated_sites_offset = client_associated_sites_offset
        if cross_regional_lookup is not None:
            self.cross_regional_lookup = cross_regional_lookup
        if end_date is not None:
            self.end_date = end_date
        if start_date is not None:
            self.start_date = start_date
        if unpaids_only is not None:
            self.unpaids_only = unpaids_only
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def client_id(self):
        """Gets the client_id of this GetClientVisitsRequest.  # noqa: E501

        The ID of the requested client.  # noqa: E501

        :return: The client_id of this GetClientVisitsRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetClientVisitsRequest.

        The ID of the requested client.  # noqa: E501

        :param client_id: The client_id of this GetClientVisitsRequest.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_associated_sites_offset(self):
        """Gets the client_associated_sites_offset of this GetClientVisitsRequest.  # noqa: E501

        The number of sites to skip when returning the site associated with a client.  # noqa: E501

        :return: The client_associated_sites_offset of this GetClientVisitsRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_associated_sites_offset

    @client_associated_sites_offset.setter
    def client_associated_sites_offset(self, client_associated_sites_offset):
        """Sets the client_associated_sites_offset of this GetClientVisitsRequest.

        The number of sites to skip when returning the site associated with a client.  # noqa: E501

        :param client_associated_sites_offset: The client_associated_sites_offset of this GetClientVisitsRequest.  # noqa: E501
        :type: int
        """

        self._client_associated_sites_offset = client_associated_sites_offset

    @property
    def cross_regional_lookup(self):
        """Gets the cross_regional_lookup of this GetClientVisitsRequest.  # noqa: E501

        When `true`, indicates that past and scheduled client visits across all sites in the region are returned.<br />  When `false`, indicates that only visits at the current site are returned.  # noqa: E501

        :return: The cross_regional_lookup of this GetClientVisitsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cross_regional_lookup

    @cross_regional_lookup.setter
    def cross_regional_lookup(self, cross_regional_lookup):
        """Sets the cross_regional_lookup of this GetClientVisitsRequest.

        When `true`, indicates that past and scheduled client visits across all sites in the region are returned.<br />  When `false`, indicates that only visits at the current site are returned.  # noqa: E501

        :param cross_regional_lookup: The cross_regional_lookup of this GetClientVisitsRequest.  # noqa: E501
        :type: bool
        """

        self._cross_regional_lookup = cross_regional_lookup

    @property
    def end_date(self):
        """Gets the end_date of this GetClientVisitsRequest.  # noqa: E501

        The date past which class visits are not returned.  Default: **today’s date**  # noqa: E501

        :return: The end_date of this GetClientVisitsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this GetClientVisitsRequest.

        The date past which class visits are not returned.  Default: **today’s date**  # noqa: E501

        :param end_date: The end_date of this GetClientVisitsRequest.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def start_date(self):
        """Gets the start_date of this GetClientVisitsRequest.  # noqa: E501

        The date before which class visits are not returned.  Default: **the end date**  # noqa: E501

        :return: The start_date of this GetClientVisitsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this GetClientVisitsRequest.

        The date before which class visits are not returned.  Default: **the end date**  # noqa: E501

        :param start_date: The start_date of this GetClientVisitsRequest.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def unpaids_only(self):
        """Gets the unpaids_only of this GetClientVisitsRequest.  # noqa: E501

        When `true`, indicates that only visits that have not been paid for are returned.<br />  When `false`, indicates that all visits are returned, regardless of whether they have been paid for.<br />  Default: **false**  # noqa: E501

        :return: The unpaids_only of this GetClientVisitsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._unpaids_only

    @unpaids_only.setter
    def unpaids_only(self, unpaids_only):
        """Sets the unpaids_only of this GetClientVisitsRequest.

        When `true`, indicates that only visits that have not been paid for are returned.<br />  When `false`, indicates that all visits are returned, regardless of whether they have been paid for.<br />  Default: **false**  # noqa: E501

        :param unpaids_only: The unpaids_only of this GetClientVisitsRequest.  # noqa: E501
        :type: bool
        """

        self._unpaids_only = unpaids_only

    @property
    def limit(self):
        """Gets the limit of this GetClientVisitsRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetClientVisitsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetClientVisitsRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetClientVisitsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetClientVisitsRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetClientVisitsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetClientVisitsRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetClientVisitsRequest.  # noqa: E501
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
        if issubclass(GetClientVisitsRequest, dict):
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
        if not isinstance(other, GetClientVisitsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other