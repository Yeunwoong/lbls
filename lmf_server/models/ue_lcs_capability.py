# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server import util


class UeLcsCapability(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lpp_support=True, ciot_optimisation=False):  # noqa: E501
        """UeLcsCapability - a model defined in OpenAPI

        :param lpp_support: The lpp_support of this UeLcsCapability.  # noqa: E501
        :type lpp_support: bool
        :param ciot_optimisation: The ciot_optimisation of this UeLcsCapability.  # noqa: E501
        :type ciot_optimisation: bool
        """
        self.openapi_types = {
            'lpp_support': bool,
            'ciot_optimisation': bool
        }

        self.attribute_map = {
            'lpp_support': 'lppSupport',
            'ciot_optimisation': 'ciotOptimisation'
        }

        self._lpp_support = lpp_support
        self._ciot_optimisation = ciot_optimisation

    @classmethod
    def from_dict(cls, dikt) -> 'UeLcsCapability':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeLcsCapability of this UeLcsCapability.  # noqa: E501
        :rtype: UeLcsCapability
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lpp_support(self):
        """Gets the lpp_support of this UeLcsCapability.


        :return: The lpp_support of this UeLcsCapability.
        :rtype: bool
        """
        return self._lpp_support

    @lpp_support.setter
    def lpp_support(self, lpp_support):
        """Sets the lpp_support of this UeLcsCapability.


        :param lpp_support: The lpp_support of this UeLcsCapability.
        :type lpp_support: bool
        """

        self._lpp_support = lpp_support

    @property
    def ciot_optimisation(self):
        """Gets the ciot_optimisation of this UeLcsCapability.


        :return: The ciot_optimisation of this UeLcsCapability.
        :rtype: bool
        """
        return self._ciot_optimisation

    @ciot_optimisation.setter
    def ciot_optimisation(self, ciot_optimisation):
        """Sets the ciot_optimisation of this UeLcsCapability.


        :param ciot_optimisation: The ciot_optimisation of this UeLcsCapability.
        :type ciot_optimisation: bool
        """

        self._ciot_optimisation = ciot_optimisation