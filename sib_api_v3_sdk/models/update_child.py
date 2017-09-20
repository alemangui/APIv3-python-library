# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  | 

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateChild(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'company_name': 'str',
        'password': 'str',
        'ips': 'list[int]'
    }

    attribute_map = {
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'company_name': 'companyName',
        'password': 'password',
        'ips': 'ips'
    }

    def __init__(self, email=None, first_name=None, last_name=None, company_name=None, password=None, ips=None):
        """
        UpdateChild - a model defined in Swagger
        """

        self._email = None
        self._first_name = None
        self._last_name = None
        self._company_name = None
        self._password = None
        self._ips = None

        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if company_name is not None:
          self.company_name = company_name
        if password is not None:
          self.password = password
        if ips is not None:
          self.ips = ips

    @property
    def email(self):
        """
        Gets the email of this UpdateChild.
        New Email address to update the child account

        :return: The email of this UpdateChild.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UpdateChild.
        New Email address to update the child account

        :param email: The email of this UpdateChild.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this UpdateChild.
        New First name to use to update the child account

        :return: The first_name of this UpdateChild.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UpdateChild.
        New First name to use to update the child account

        :param first_name: The first_name of this UpdateChild.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this UpdateChild.
        New Last name to use to update the child account

        :return: The last_name of this UpdateChild.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UpdateChild.
        New Last name to use to update the child account

        :param last_name: The last_name of this UpdateChild.
        :type: str
        """

        self._last_name = last_name

    @property
    def company_name(self):
        """
        Gets the company_name of this UpdateChild.
        New Company name to use to update the child account

        :return: The company_name of this UpdateChild.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this UpdateChild.
        New Company name to use to update the child account

        :param company_name: The company_name of this UpdateChild.
        :type: str
        """

        self._company_name = company_name

    @property
    def password(self):
        """
        Gets the password of this UpdateChild.
        New password for the child account to login

        :return: The password of this UpdateChild.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateChild.
        New password for the child account to login

        :param password: The password of this UpdateChild.
        :type: str
        """

        self._password = password

    @property
    def ips(self):
        """
        Gets the ips of this UpdateChild.

        :return: The ips of this UpdateChild.
        :rtype: list[int]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """
        Sets the ips of this UpdateChild.

        :param ips: The ips of this UpdateChild.
        :type: list[int]
        """

        self._ips = ips

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UpdateChild):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other