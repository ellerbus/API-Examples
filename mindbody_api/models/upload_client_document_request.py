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

from mindbody_api.models.client_document import ClientDocument  # noqa: F401,E501


class UploadClientDocumentRequest(object):
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
        'file': 'ClientDocument'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'file': 'File'
    }

    def __init__(self, client_id=None, file=None):  # noqa: E501
        """UploadClientDocumentRequest - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._file = None
        self.discriminator = None

        self.client_id = client_id
        self.file = file

    @property
    def client_id(self):
        """Gets the client_id of this UploadClientDocumentRequest.  # noqa: E501

        The RSSID of the client for whom the document is to be uploaded.  # noqa: E501

        :return: The client_id of this UploadClientDocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this UploadClientDocumentRequest.

        The RSSID of the client for whom the document is to be uploaded.  # noqa: E501

        :param client_id: The client_id of this UploadClientDocumentRequest.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def file(self):
        """Gets the file of this UploadClientDocumentRequest.  # noqa: E501

        Contains information about the file to be uploaded.  # noqa: E501

        :return: The file of this UploadClientDocumentRequest.  # noqa: E501
        :rtype: ClientDocument
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this UploadClientDocumentRequest.

        Contains information about the file to be uploaded.  # noqa: E501

        :param file: The file of this UploadClientDocumentRequest.  # noqa: E501
        :type: ClientDocument
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

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
        if issubclass(UploadClientDocumentRequest, dict):
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
        if not isinstance(other, UploadClientDocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
