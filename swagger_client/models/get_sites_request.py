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


class GetSitesRequest(object):
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
        'site_ids': 'list[int]',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'site_ids': 'SiteIds',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, site_ids=None, limit=None, offset=None):  # noqa: E501
        """GetSitesRequest - a model defined in Swagger"""  # noqa: E501

        self._site_ids = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if site_ids is not None:
            self.site_ids = site_ids
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def site_ids(self):
        """Gets the site_ids of this GetSitesRequest.  # noqa: E501

        List of the requested site IDs. When omitted, returns all sites that the source has access to.  # noqa: E501

        :return: The site_ids of this GetSitesRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._site_ids

    @site_ids.setter
    def site_ids(self, site_ids):
        """Sets the site_ids of this GetSitesRequest.

        List of the requested site IDs. When omitted, returns all sites that the source has access to.  # noqa: E501

        :param site_ids: The site_ids of this GetSitesRequest.  # noqa: E501
        :type: list[int]
        """

        self._site_ids = site_ids

    @property
    def limit(self):
        """Gets the limit of this GetSitesRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetSitesRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetSitesRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetSitesRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetSitesRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetSitesRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetSitesRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetSitesRequest.  # noqa: E501
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
        if issubclass(GetSitesRequest, dict):
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
        if not isinstance(other, GetSitesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other