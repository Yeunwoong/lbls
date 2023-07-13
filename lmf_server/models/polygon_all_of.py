# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.geographical_coordinates import GeographicalCoordinates
from lmf_server import util

from lmf_server.models.geographical_coordinates import GeographicalCoordinates  # noqa: E501

class PolygonAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, point_list=None):  # noqa: E501
        """PolygonAllOf - a model defined in OpenAPI

        :param point_list: The point_list of this PolygonAllOf.  # noqa: E501
        :type point_list: List[GeographicalCoordinates]
        """
        self.openapi_types = {
            'point_list': List[GeographicalCoordinates]
        }

        self.attribute_map = {
            'point_list': 'pointList'
        }

        self._point_list = point_list

    @classmethod
    def from_dict(cls, dikt) -> 'PolygonAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Polygon_allOf of this PolygonAllOf.  # noqa: E501
        :rtype: PolygonAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def point_list(self):
        """Gets the point_list of this PolygonAllOf.

        List of points.  # noqa: E501

        :return: The point_list of this PolygonAllOf.
        :rtype: List[GeographicalCoordinates]
        """
        return self._point_list

    @point_list.setter
    def point_list(self, point_list):
        """Sets the point_list of this PolygonAllOf.

        List of points.  # noqa: E501

        :param point_list: The point_list of this PolygonAllOf.
        :type point_list: List[GeographicalCoordinates]
        """
        if point_list is None:
            raise ValueError("Invalid value for `point_list`, must not be `None`")  # noqa: E501
        if point_list is not None and len(point_list) > 15:
            raise ValueError("Invalid value for `point_list`, number of items must be less than or equal to `15`")  # noqa: E501
        if point_list is not None and len(point_list) < 3:
            raise ValueError("Invalid value for `point_list`, number of items must be greater than or equal to `3`")  # noqa: E501

        self._point_list = point_list