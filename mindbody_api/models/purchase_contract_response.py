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


class PurchaseContractResponse(object):
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
        'location_id': 'int',
        'contract_id': 'int',
        'client_contract_id': 'int'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'location_id': 'LocationId',
        'contract_id': 'ContractId',
        'client_contract_id': 'ClientContractId'
    }

    def __init__(self, client_id=None, location_id=None, contract_id=None, client_contract_id=None):  # noqa: E501
        """PurchaseContractResponse - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._location_id = None
        self._contract_id = None
        self._client_contract_id = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if location_id is not None:
            self.location_id = location_id
        if contract_id is not None:
            self.contract_id = contract_id
        if client_contract_id is not None:
            self.client_contract_id = client_contract_id

    @property
    def client_id(self):
        """Gets the client_id of this PurchaseContractResponse.  # noqa: E501

        The ID of the client who is purchasing the contract.  # noqa: E501

        :return: The client_id of this PurchaseContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this PurchaseContractResponse.

        The ID of the client who is purchasing the contract.  # noqa: E501

        :param client_id: The client_id of this PurchaseContractResponse.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def location_id(self):
        """Gets the location_id of this PurchaseContractResponse.  # noqa: E501

        The ID of the location where the contract is being purchased.  # noqa: E501

        :return: The location_id of this PurchaseContractResponse.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this PurchaseContractResponse.

        The ID of the location where the contract is being purchased.  # noqa: E501

        :param location_id: The location_id of this PurchaseContractResponse.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def contract_id(self):
        """Gets the contract_id of this PurchaseContractResponse.  # noqa: E501

        The ID of the general contract being purchased.  # noqa: E501

        :return: The contract_id of this PurchaseContractResponse.  # noqa: E501
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this PurchaseContractResponse.

        The ID of the general contract being purchased.  # noqa: E501

        :param contract_id: The contract_id of this PurchaseContractResponse.  # noqa: E501
        :type: int
        """

        self._contract_id = contract_id

    @property
    def client_contract_id(self):
        """Gets the client_contract_id of this PurchaseContractResponse.  # noqa: E501

        The ID of the specific contract being purchased by this specific client, not to be confused with the `ContractId`, which refers to a general contract that the business offers.  # noqa: E501

        :return: The client_contract_id of this PurchaseContractResponse.  # noqa: E501
        :rtype: int
        """
        return self._client_contract_id

    @client_contract_id.setter
    def client_contract_id(self, client_contract_id):
        """Sets the client_contract_id of this PurchaseContractResponse.

        The ID of the specific contract being purchased by this specific client, not to be confused with the `ContractId`, which refers to a general contract that the business offers.  # noqa: E501

        :param client_contract_id: The client_contract_id of this PurchaseContractResponse.  # noqa: E501
        :type: int
        """

        self._client_contract_id = client_contract_id

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
        if issubclass(PurchaseContractResponse, dict):
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
        if not isinstance(other, PurchaseContractResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other