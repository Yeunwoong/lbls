# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.gad_shape import GADShape
from lmf_server.models.geographical_coordinates import GeographicalCoordinates
from lmf_server.models.supported_gad_shapes import SupportedGADShapes
from lmf_server import util

from lmf_server.models.gad_shape import GADShape  # noqa: E501
from lmf_server.models.geographical_coordinates import GeographicalCoordinates  # noqa: E501
from lmf_server.models.supported_gad_shapes import SupportedGADShapes  # noqa: E501

class PointUncertaintyCircle(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, shape=None, point=None, uncertainty=None):  # noqa: E501
        """PointUncertaintyCircle - a model defined in OpenAPI

        :param shape: The shape of this PointUncertaintyCircle.  # noqa: E501
        :type shape: SupportedGADShapes
        :param point: The point of this PointUncertaintyCircle.  # noqa: E501
        :type point: GeographicalCoordinates
        :param uncertainty: The uncertainty of this PointUncertaintyCircle.  # noqa: E501
        :type uncertainty: float
        """
        self.openapi_types = {
            'shape': SupportedGADShapes,
            'point': GeographicalCoordinates,
            'uncertainty': float
        }

        self.attribute_map = {
            'shape': 'shape',
            'point': 'point',
            'uncertainty': 'uncertainty'
        }

        self._shape = shape
        self._point = point
        self._uncertainty = uncertainty

    @classmethod
    def from_dict(cls, dikt) -> 'PointUncertaintyCircle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PointUncertaintyCircle of this PointUncertaintyCircle.  # noqa: E501
        :rtype: PointUncertaintyCircle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shape(self):
        """Gets the shape of this PointUncertaintyCircle.


        :return: The shape of this PointUncertaintyCircle.
        :rtype: SupportedGADShapes
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this PointUncertaintyCircle.


        :param shape: The shape of this PointUncertaintyCircle.
        :type shape: SupportedGADShapes
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def point(self):
        """Gets the point of this PointUncertaintyCircle.


        :return: The point of this PointUncertaintyCircle.
        :rtype: GeographicalCoordinates
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this PointUncertaintyCircle.


        :param point: The point of this PointUncertaintyCircle.
        :type point: GeographicalCoordinates
        """
        if point is None:
            raise ValueError("Invalid value for `point`, must not be `None`")  # noqa: E501

        self._point = point

    @property
    def uncertainty(self):
        """Gets the uncertainty of this PointUncertaintyCircle.

        Indicates value of uncertainty.  # noqa: E501

        :return: The uncertainty of this PointUncertaintyCircle.
        :rtype: float
        """
        return self._uncertainty

    @uncertainty.setter
    def uncertainty(self, uncertainty):
        """Sets the uncertainty of this PointUncertaintyCircle.

        Indicates value of uncertainty.  # noqa: E501

        :param uncertainty: The uncertainty of this PointUncertaintyCircle.
        :type uncertainty: float
        """
        if uncertainty is None:
            raise ValueError("Invalid value for `uncertainty`, must not be `None`")  # noqa: E501
        if uncertainty is not None and uncertainty < 0:  # noqa: E501
            raise ValueError("Invalid value for `uncertainty`, must be a value greater than or equal to `0`")  # noqa: E501

        self._uncertainty = uncertainty
