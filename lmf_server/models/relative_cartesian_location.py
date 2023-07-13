# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server import util


class RelativeCartesianLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None, y=None, z=None):  # noqa: E501
        """RelativeCartesianLocation - a model defined in OpenAPI

        :param x: The x of this RelativeCartesianLocation.  # noqa: E501
        :type x: float
        :param y: The y of this RelativeCartesianLocation.  # noqa: E501
        :type y: float
        :param z: The z of this RelativeCartesianLocation.  # noqa: E501
        :type z: float
        """
        self.openapi_types = {
            'x': float,
            'y': float,
            'z': float
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'z': 'z'
        }

        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def from_dict(cls, dikt) -> 'RelativeCartesianLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RelativeCartesianLocation of this RelativeCartesianLocation.  # noqa: E501
        :rtype: RelativeCartesianLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this RelativeCartesianLocation.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The x of this RelativeCartesianLocation.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this RelativeCartesianLocation.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param x: The x of this RelativeCartesianLocation.
        :type x: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this RelativeCartesianLocation.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The y of this RelativeCartesianLocation.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this RelativeCartesianLocation.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param y: The y of this RelativeCartesianLocation.
        :type y: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def z(self):
        """Gets the z of this RelativeCartesianLocation.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :return: The z of this RelativeCartesianLocation.
        :rtype: float
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this RelativeCartesianLocation.

        string with format 'float' as defined in OpenAPI.  # noqa: E501

        :param z: The z of this RelativeCartesianLocation.
        :type z: float
        """

        self._z = z
