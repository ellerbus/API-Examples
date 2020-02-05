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


class Service(object):
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
        'price': 'float',
        'online_price': 'float',
        'tax_included': 'float',
        'program_id': 'int',
        'tax_rate': 'float',
        'product_id': 'float',
        'id': 'str',
        'name': 'str',
        'count': 'int'
    }

    attribute_map = {
        'price': 'Price',
        'online_price': 'OnlinePrice',
        'tax_included': 'TaxIncluded',
        'program_id': 'ProgramId',
        'tax_rate': 'TaxRate',
        'product_id': 'ProductId',
        'id': 'Id',
        'name': 'Name',
        'count': 'Count'
    }

    def __init__(self, price=None, online_price=None, tax_included=None, program_id=None, tax_rate=None, product_id=None, id=None, name=None, count=None):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501

        self._price = None
        self._online_price = None
        self._tax_included = None
        self._program_id = None
        self._tax_rate = None
        self._product_id = None
        self._id = None
        self._name = None
        self._count = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if online_price is not None:
            self.online_price = online_price
        if tax_included is not None:
            self.tax_included = tax_included
        if program_id is not None:
            self.program_id = program_id
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if product_id is not None:
            self.product_id = product_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if count is not None:
            self.count = count

    @property
    def price(self):
        """Gets the price of this Service.  # noqa: E501

        The cost of the pricing option when sold at a physical location.  # noqa: E501

        :return: The price of this Service.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Service.

        The cost of the pricing option when sold at a physical location.  # noqa: E501

        :param price: The price of this Service.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def online_price(self):
        """Gets the online_price of this Service.  # noqa: E501

        The cost of the pricing option when sold online.  # noqa: E501

        :return: The online_price of this Service.  # noqa: E501
        :rtype: float
        """
        return self._online_price

    @online_price.setter
    def online_price(self, online_price):
        """Sets the online_price of this Service.

        The cost of the pricing option when sold online.  # noqa: E501

        :param online_price: The online_price of this Service.  # noqa: E501
        :type: float
        """

        self._online_price = online_price

    @property
    def tax_included(self):
        """Gets the tax_included of this Service.  # noqa: E501

        The amount of tax included in the price, if inclusive pricing is enabled.  # noqa: E501

        :return: The tax_included of this Service.  # noqa: E501
        :rtype: float
        """
        return self._tax_included

    @tax_included.setter
    def tax_included(self, tax_included):
        """Sets the tax_included of this Service.

        The amount of tax included in the price, if inclusive pricing is enabled.  # noqa: E501

        :param tax_included: The tax_included of this Service.  # noqa: E501
        :type: float
        """

        self._tax_included = tax_included

    @property
    def program_id(self):
        """Gets the program_id of this Service.  # noqa: E501

        The ID of the program that this pricing option applies to.  # noqa: E501

        :return: The program_id of this Service.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this Service.

        The ID of the program that this pricing option applies to.  # noqa: E501

        :param program_id: The program_id of this Service.  # noqa: E501
        :type: int
        """

        self._program_id = program_id

    @property
    def tax_rate(self):
        """Gets the tax_rate of this Service.  # noqa: E501

        The tax rate applied to the pricing option. This field is populated only when you include a `LocationID` in the request.  # noqa: E501

        :return: The tax_rate of this Service.  # noqa: E501
        :rtype: float
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """Sets the tax_rate of this Service.

        The tax rate applied to the pricing option. This field is populated only when you include a `LocationID` in the request.  # noqa: E501

        :param tax_rate: The tax_rate of this Service.  # noqa: E501
        :type: float
        """

        self._tax_rate = tax_rate

    @property
    def product_id(self):
        """Gets the product_id of this Service.  # noqa: E501

        The unique ID of the pricing option.  # noqa: E501

        :return: The product_id of this Service.  # noqa: E501
        :rtype: float
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Service.

        The unique ID of the pricing option.  # noqa: E501

        :param product_id: The product_id of this Service.  # noqa: E501
        :type: float
        """

        self._product_id = product_id

    @property
    def id(self):
        """Gets the id of this Service.  # noqa: E501

        The barcode ID of the pricing option.  # noqa: E501

        :return: The id of this Service.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Service.

        The barcode ID of the pricing option.  # noqa: E501

        :param id: The id of this Service.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Service.  # noqa: E501

        The name of the pricing option.  # noqa: E501

        :return: The name of this Service.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Service.

        The name of the pricing option.  # noqa: E501

        :param name: The name of this Service.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def count(self):
        """Gets the count of this Service.  # noqa: E501

        The initial count of usages available for the pricing option.  # noqa: E501

        :return: The count of this Service.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Service.

        The initial count of usages available for the pricing option.  # noqa: E501

        :param count: The count of this Service.  # noqa: E501
        :type: int
        """

        self._count = count

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
        if issubclass(Service, dict):
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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other