# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server import util


class PeriodicEventInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, reporting_amount=None, reporting_interval=None):  # noqa: E501
        """PeriodicEventInfo - a model defined in OpenAPI

        :param reporting_amount: The reporting_amount of this PeriodicEventInfo.  # noqa: E501
        :type reporting_amount: int
        :param reporting_interval: The reporting_interval of this PeriodicEventInfo.  # noqa: E501
        :type reporting_interval: int
        """
        self.openapi_types = {
            'reporting_amount': int,
            'reporting_interval': int
        }

        self.attribute_map = {
            'reporting_amount': 'reportingAmount',
            'reporting_interval': 'reportingInterval'
        }

        self._reporting_amount = reporting_amount
        self._reporting_interval = reporting_interval

    @classmethod
    def from_dict(cls, dikt) -> 'PeriodicEventInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PeriodicEventInfo of this PeriodicEventInfo.  # noqa: E501
        :rtype: PeriodicEventInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reporting_amount(self):
        """Gets the reporting_amount of this PeriodicEventInfo.

        Number of required periodic event reports.  # noqa: E501

        :return: The reporting_amount of this PeriodicEventInfo.
        :rtype: int
        """
        return self._reporting_amount

    @reporting_amount.setter
    def reporting_amount(self, reporting_amount):
        """Sets the reporting_amount of this PeriodicEventInfo.

        Number of required periodic event reports.  # noqa: E501

        :param reporting_amount: The reporting_amount of this PeriodicEventInfo.
        :type reporting_amount: int
        """
        if reporting_amount is None:
            raise ValueError("Invalid value for `reporting_amount`, must not be `None`")  # noqa: E501
        if reporting_amount is not None and reporting_amount > 8639999:  # noqa: E501
            raise ValueError("Invalid value for `reporting_amount`, must be a value less than or equal to `8639999`")  # noqa: E501
        if reporting_amount is not None and reporting_amount < 1:  # noqa: E501
            raise ValueError("Invalid value for `reporting_amount`, must be a value greater than or equal to `1`")  # noqa: E501

        self._reporting_amount = reporting_amount

    @property
    def reporting_interval(self):
        """Gets the reporting_interval of this PeriodicEventInfo.

        Event reporting periodic interval.  # noqa: E501

        :return: The reporting_interval of this PeriodicEventInfo.
        :rtype: int
        """
        return self._reporting_interval

    @reporting_interval.setter
    def reporting_interval(self, reporting_interval):
        """Sets the reporting_interval of this PeriodicEventInfo.

        Event reporting periodic interval.  # noqa: E501

        :param reporting_interval: The reporting_interval of this PeriodicEventInfo.
        :type reporting_interval: int
        """
        if reporting_interval is None:
            raise ValueError("Invalid value for `reporting_interval`, must not be `None`")  # noqa: E501
        if reporting_interval is not None and reporting_interval > 8639999:  # noqa: E501
            raise ValueError("Invalid value for `reporting_interval`, must be a value less than or equal to `8639999`")  # noqa: E501
        if reporting_interval is not None and reporting_interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `reporting_interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._reporting_interval = reporting_interval
