# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.geographical_coordinates import GeographicalCoordinates
from lmf_server import util

from lmf_server.models.geographical_coordinates import GeographicalCoordinates  # noqa: E501

class LocalOrigin(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coordinate_id=None, point=None):  # noqa: E501
        """LocalOrigin - a model defined in OpenAPI

        :param coordinate_id: The coordinate_id of this LocalOrigin.  # noqa: E501
        :type coordinate_id: str
        :param point: The point of this LocalOrigin.  # noqa: E501
        :type point: GeographicalCoordinates
        """
        self.openapi_types = {
            'coordinate_id': str,
            'point': GeographicalCoordinates
        }

        self.attribute_map = {
            'coordinate_id': 'coordinateId',
            'point': 'point'
        }

        self._coordinate_id = coordinate_id
        self._point = point

    @classmethod
    def from_dict(cls, dikt) -> 'LocalOrigin':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LocalOrigin of this LocalOrigin.  # noqa: E501
        :rtype: LocalOrigin
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coordinate_id(self):
        """Gets the coordinate_id of this LocalOrigin.


        :return: The coordinate_id of this LocalOrigin.
        :rtype: str
        """
        return self._coordinate_id

    @coordinate_id.setter
    def coordinate_id(self, coordinate_id):
        """Sets the coordinate_id of this LocalOrigin.


        :param coordinate_id: The coordinate_id of this LocalOrigin.
        :type coordinate_id: str
        """

        self._coordinate_id = coordinate_id

    @property
    def point(self):
        """Gets the point of this LocalOrigin.


        :return: The point of this LocalOrigin.
        :rtype: GeographicalCoordinates
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this LocalOrigin.


        :param point: The point of this LocalOrigin.
        :type point: GeographicalCoordinates
        """

        self._point = point
