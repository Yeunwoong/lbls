# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.horizontal_velocity import HorizontalVelocity
from lmf_server.models.horizontal_velocity_with_uncertainty import HorizontalVelocityWithUncertainty
from lmf_server.models.horizontal_with_vertical_velocity import HorizontalWithVerticalVelocity
from lmf_server.models.horizontal_with_vertical_velocity_and_uncertainty import HorizontalWithVerticalVelocityAndUncertainty
from lmf_server.models.vertical_direction import VerticalDirection
from lmf_server import util

from lmf_server.models.horizontal_velocity import HorizontalVelocity  # noqa: E501
from lmf_server.models.horizontal_velocity_with_uncertainty import HorizontalVelocityWithUncertainty  # noqa: E501
from lmf_server.models.horizontal_with_vertical_velocity import HorizontalWithVerticalVelocity  # noqa: E501
from lmf_server.models.horizontal_with_vertical_velocity_and_uncertainty import HorizontalWithVerticalVelocityAndUncertainty  # noqa: E501
from lmf_server.models.vertical_direction import VerticalDirection  # noqa: E501

class VelocityEstimate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, h_speed=None, bearing=None, v_speed=None, v_direction=None, h_uncertainty=None, v_uncertainty=None):  # noqa: E501
        """VelocityEstimate - a model defined in OpenAPI

        :param h_speed: The h_speed of this VelocityEstimate.  # noqa: E501
        :type h_speed: float
        :param bearing: The bearing of this VelocityEstimate.  # noqa: E501
        :type bearing: int
        :param v_speed: The v_speed of this VelocityEstimate.  # noqa: E501
        :type v_speed: float
        :param v_direction: The v_direction of this VelocityEstimate.  # noqa: E501
        :type v_direction: VerticalDirection
        :param h_uncertainty: The h_uncertainty of this VelocityEstimate.  # noqa: E501
        :type h_uncertainty: float
        :param v_uncertainty: The v_uncertainty of this VelocityEstimate.  # noqa: E501
        :type v_uncertainty: float
        """
        self.openapi_types = {
            'h_speed': float,
            'bearing': int,
            'v_speed': float,
            'v_direction': VerticalDirection,
            'h_uncertainty': float,
            'v_uncertainty': float
        }

        self.attribute_map = {
            'h_speed': 'hSpeed',
            'bearing': 'bearing',
            'v_speed': 'vSpeed',
            'v_direction': 'vDirection',
            'h_uncertainty': 'hUncertainty',
            'v_uncertainty': 'vUncertainty'
        }

        self._h_speed = h_speed
        self._bearing = bearing
        self._v_speed = v_speed
        self._v_direction = v_direction
        self._h_uncertainty = h_uncertainty
        self._v_uncertainty = v_uncertainty

    @classmethod
    def from_dict(cls, dikt) -> 'VelocityEstimate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VelocityEstimate of this VelocityEstimate.  # noqa: E501
        :rtype: VelocityEstimate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def h_speed(self):
        """Gets the h_speed of this VelocityEstimate.

        Indicates value of horizontal speed.  # noqa: E501

        :return: The h_speed of this VelocityEstimate.
        :rtype: float
        """
        return self._h_speed

    @h_speed.setter
    def h_speed(self, h_speed):
        """Sets the h_speed of this VelocityEstimate.

        Indicates value of horizontal speed.  # noqa: E501

        :param h_speed: The h_speed of this VelocityEstimate.
        :type h_speed: float
        """
        if h_speed is None:
            raise ValueError("Invalid value for `h_speed`, must not be `None`")  # noqa: E501
        if h_speed is not None and h_speed > 2047:  # noqa: E501
            raise ValueError("Invalid value for `h_speed`, must be a value less than or equal to `2047`")  # noqa: E501
        if h_speed is not None and h_speed < 0:  # noqa: E501
            raise ValueError("Invalid value for `h_speed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._h_speed = h_speed

    @property
    def bearing(self):
        """Gets the bearing of this VelocityEstimate.

        Indicates value of angle.  # noqa: E501

        :return: The bearing of this VelocityEstimate.
        :rtype: int
        """
        return self._bearing

    @bearing.setter
    def bearing(self, bearing):
        """Sets the bearing of this VelocityEstimate.

        Indicates value of angle.  # noqa: E501

        :param bearing: The bearing of this VelocityEstimate.
        :type bearing: int
        """
        if bearing is None:
            raise ValueError("Invalid value for `bearing`, must not be `None`")  # noqa: E501
        if bearing is not None and bearing > 360:  # noqa: E501
            raise ValueError("Invalid value for `bearing`, must be a value less than or equal to `360`")  # noqa: E501
        if bearing is not None and bearing < 0:  # noqa: E501
            raise ValueError("Invalid value for `bearing`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bearing = bearing

    @property
    def v_speed(self):
        """Gets the v_speed of this VelocityEstimate.

        Indicates value of vertical speed.  # noqa: E501

        :return: The v_speed of this VelocityEstimate.
        :rtype: float
        """
        return self._v_speed

    @v_speed.setter
    def v_speed(self, v_speed):
        """Sets the v_speed of this VelocityEstimate.

        Indicates value of vertical speed.  # noqa: E501

        :param v_speed: The v_speed of this VelocityEstimate.
        :type v_speed: float
        """
        if v_speed is None:
            raise ValueError("Invalid value for `v_speed`, must not be `None`")  # noqa: E501
        if v_speed is not None and v_speed > 255:  # noqa: E501
            raise ValueError("Invalid value for `v_speed`, must be a value less than or equal to `255`")  # noqa: E501
        if v_speed is not None and v_speed < 0:  # noqa: E501
            raise ValueError("Invalid value for `v_speed`, must be a value greater than or equal to `0`")  # noqa: E501

        self._v_speed = v_speed

    @property
    def v_direction(self):
        """Gets the v_direction of this VelocityEstimate.


        :return: The v_direction of this VelocityEstimate.
        :rtype: VerticalDirection
        """
        return self._v_direction

    @v_direction.setter
    def v_direction(self, v_direction):
        """Sets the v_direction of this VelocityEstimate.


        :param v_direction: The v_direction of this VelocityEstimate.
        :type v_direction: VerticalDirection
        """
        if v_direction is None:
            raise ValueError("Invalid value for `v_direction`, must not be `None`")  # noqa: E501

        self._v_direction = v_direction

    @property
    def h_uncertainty(self):
        """Gets the h_uncertainty of this VelocityEstimate.

        Indicates value of speed uncertainty.  # noqa: E501

        :return: The h_uncertainty of this VelocityEstimate.
        :rtype: float
        """
        return self._h_uncertainty

    @h_uncertainty.setter
    def h_uncertainty(self, h_uncertainty):
        """Sets the h_uncertainty of this VelocityEstimate.

        Indicates value of speed uncertainty.  # noqa: E501

        :param h_uncertainty: The h_uncertainty of this VelocityEstimate.
        :type h_uncertainty: float
        """
        if h_uncertainty is None:
            raise ValueError("Invalid value for `h_uncertainty`, must not be `None`")  # noqa: E501
        if h_uncertainty is not None and h_uncertainty > 255:  # noqa: E501
            raise ValueError("Invalid value for `h_uncertainty`, must be a value less than or equal to `255`")  # noqa: E501
        if h_uncertainty is not None and h_uncertainty < 0:  # noqa: E501
            raise ValueError("Invalid value for `h_uncertainty`, must be a value greater than or equal to `0`")  # noqa: E501

        self._h_uncertainty = h_uncertainty

    @property
    def v_uncertainty(self):
        """Gets the v_uncertainty of this VelocityEstimate.

        Indicates value of speed uncertainty.  # noqa: E501

        :return: The v_uncertainty of this VelocityEstimate.
        :rtype: float
        """
        return self._v_uncertainty

    @v_uncertainty.setter
    def v_uncertainty(self, v_uncertainty):
        """Sets the v_uncertainty of this VelocityEstimate.

        Indicates value of speed uncertainty.  # noqa: E501

        :param v_uncertainty: The v_uncertainty of this VelocityEstimate.
        :type v_uncertainty: float
        """
        if v_uncertainty is None:
            raise ValueError("Invalid value for `v_uncertainty`, must not be `None`")  # noqa: E501
        if v_uncertainty is not None and v_uncertainty > 255:  # noqa: E501
            raise ValueError("Invalid value for `v_uncertainty`, must be a value less than or equal to `255`")  # noqa: E501
        if v_uncertainty is not None and v_uncertainty < 0:  # noqa: E501
            raise ValueError("Invalid value for `v_uncertainty`, must be a value greater than or equal to `0`")  # noqa: E501

        self._v_uncertainty = v_uncertainty
