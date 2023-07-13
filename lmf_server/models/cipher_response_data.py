# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.data_availability import DataAvailability
from lmf_server import util

from lmf_server.models.data_availability import DataAvailability  # noqa: E501

class CipherResponseData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data_availability=None):  # noqa: E501
        """CipherResponseData - a model defined in OpenAPI

        :param data_availability: The data_availability of this CipherResponseData.  # noqa: E501
        :type data_availability: DataAvailability
        """
        self.openapi_types = {
            'data_availability': DataAvailability
        }

        self.attribute_map = {
            'data_availability': 'dataAvailability'
        }

        self._data_availability = data_availability

    @classmethod
    def from_dict(cls, dikt) -> 'CipherResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CipherResponseData of this CipherResponseData.  # noqa: E501
        :rtype: CipherResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_availability(self):
        """Gets the data_availability of this CipherResponseData.


        :return: The data_availability of this CipherResponseData.
        :rtype: DataAvailability
        """
        return self._data_availability

    @data_availability.setter
    def data_availability(self, data_availability):
        """Sets the data_availability of this CipherResponseData.


        :param data_availability: The data_availability of this CipherResponseData.
        :type data_availability: DataAvailability
        """
        if data_availability is None:
            raise ValueError("Invalid value for `data_availability`, must not be `None`")  # noqa: E501

        self._data_availability = data_availability
