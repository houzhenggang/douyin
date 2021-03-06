# coding: utf-8

"""
    企业号意向用户管理

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
"""

import pprint
import re  # noqa: F401

import six


class EnterpriseLeadsTagCreateBody(object):
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
        'tag_name': 'str'
    }

    attribute_map = {
        'tag_name': 'tag_name'
    }

    def __init__(self, tag_name=None):  # noqa: E501
        """EnterpriseLeadsTagCreateBody - a model defined in Swagger"""  # noqa: E501
        self._tag_name = None
        self.discriminator = None
        self.tag_name = tag_name

    @property
    def tag_name(self):
        """Gets the tag_name of this EnterpriseLeadsTagCreateBody.  # noqa: E501

        标签名称  # noqa: E501

        :return: The tag_name of this EnterpriseLeadsTagCreateBody.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this EnterpriseLeadsTagCreateBody.

        标签名称  # noqa: E501

        :param tag_name: The tag_name of this EnterpriseLeadsTagCreateBody.  # noqa: E501
        :type: str
        """
        if tag_name is None:
            raise ValueError("Invalid value for `tag_name`, must not be `None`")  # noqa: E501

        self._tag_name = tag_name

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
        if issubclass(EnterpriseLeadsTagCreateBody, dict):
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
        if not isinstance(other, EnterpriseLeadsTagCreateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
