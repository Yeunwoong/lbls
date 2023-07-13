# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server import util


class CipheringDataSet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ciphering_set_id=None, ciphering_key=None, c0=None, lte_pos_sib_types=None, nr_pos_sib_types=None, validity_start_time=None, validity_duration=None, tai_list=None):  # noqa: E501
        """CipheringDataSet - a model defined in OpenAPI

        :param ciphering_set_id: The ciphering_set_id of this CipheringDataSet.  # noqa: E501
        :type ciphering_set_id: int
        :param ciphering_key: The ciphering_key of this CipheringDataSet.  # noqa: E501
        :type ciphering_key: str
        :param c0: The c0 of this CipheringDataSet.  # noqa: E501
        :type c0: str
        :param lte_pos_sib_types: The lte_pos_sib_types of this CipheringDataSet.  # noqa: E501
        :type lte_pos_sib_types: str
        :param nr_pos_sib_types: The nr_pos_sib_types of this CipheringDataSet.  # noqa: E501
        :type nr_pos_sib_types: str
        :param validity_start_time: The validity_start_time of this CipheringDataSet.  # noqa: E501
        :type validity_start_time: datetime
        :param validity_duration: The validity_duration of this CipheringDataSet.  # noqa: E501
        :type validity_duration: int
        :param tai_list: The tai_list of this CipheringDataSet.  # noqa: E501
        :type tai_list: str
        """
        self.openapi_types = {
            'ciphering_set_id': int,
            'ciphering_key': str,
            'c0': str,
            'lte_pos_sib_types': str,
            'nr_pos_sib_types': str,
            'validity_start_time': datetime,
            'validity_duration': int,
            'tai_list': str
        }

        self.attribute_map = {
            'ciphering_set_id': 'cipheringSetID',
            'ciphering_key': 'cipheringKey',
            'c0': 'c0',
            'lte_pos_sib_types': 'ltePosSibTypes',
            'nr_pos_sib_types': 'nrPosSibTypes',
            'validity_start_time': 'validityStartTime',
            'validity_duration': 'validityDuration',
            'tai_list': 'taiList'
        }

        self._ciphering_set_id = ciphering_set_id
        self._ciphering_key = ciphering_key
        self._c0 = c0
        self._lte_pos_sib_types = lte_pos_sib_types
        self._nr_pos_sib_types = nr_pos_sib_types
        self._validity_start_time = validity_start_time
        self._validity_duration = validity_duration
        self._tai_list = tai_list

    @classmethod
    def from_dict(cls, dikt) -> 'CipheringDataSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CipheringDataSet of this CipheringDataSet.  # noqa: E501
        :rtype: CipheringDataSet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ciphering_set_id(self):
        """Gets the ciphering_set_id of this CipheringDataSet.

        Ciphering Data Set Identifier.  # noqa: E501

        :return: The ciphering_set_id of this CipheringDataSet.
        :rtype: int
        """
        return self._ciphering_set_id

    @ciphering_set_id.setter
    def ciphering_set_id(self, ciphering_set_id):
        """Sets the ciphering_set_id of this CipheringDataSet.

        Ciphering Data Set Identifier.  # noqa: E501

        :param ciphering_set_id: The ciphering_set_id of this CipheringDataSet.
        :type ciphering_set_id: int
        """
        if ciphering_set_id is None:
            raise ValueError("Invalid value for `ciphering_set_id`, must not be `None`")  # noqa: E501
        if ciphering_set_id is not None and ciphering_set_id > 65535:  # noqa: E501
            raise ValueError("Invalid value for `ciphering_set_id`, must be a value less than or equal to `65535`")  # noqa: E501
        if ciphering_set_id is not None and ciphering_set_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `ciphering_set_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._ciphering_set_id = ciphering_set_id

    @property
    def ciphering_key(self):
        """Gets the ciphering_key of this CipheringDataSet.

        Ciphering Key.  # noqa: E501

        :return: The ciphering_key of this CipheringDataSet.
        :rtype: str
        """
        return self._ciphering_key

    @ciphering_key.setter
    def ciphering_key(self, ciphering_key):
        """Sets the ciphering_key of this CipheringDataSet.

        Ciphering Key.  # noqa: E501

        :param ciphering_key: The ciphering_key of this CipheringDataSet.
        :type ciphering_key: str
        """
        if ciphering_key is None:
            raise ValueError("Invalid value for `ciphering_key`, must not be `None`")  # noqa: E501

        self._ciphering_key = ciphering_key

    @property
    def c0(self):
        """Gets the c0 of this CipheringDataSet.

        First component of the initial ciphering counter.  # noqa: E501

        :return: The c0 of this CipheringDataSet.
        :rtype: str
        """
        return self._c0

    @c0.setter
    def c0(self, c0):
        """Sets the c0 of this CipheringDataSet.

        First component of the initial ciphering counter.  # noqa: E501

        :param c0: The c0 of this CipheringDataSet.
        :type c0: str
        """
        if c0 is None:
            raise ValueError("Invalid value for `c0`, must not be `None`")  # noqa: E501

        self._c0 = c0

    @property
    def lte_pos_sib_types(self):
        """Gets the lte_pos_sib_types of this CipheringDataSet.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :return: The lte_pos_sib_types of this CipheringDataSet.
        :rtype: str
        """
        return self._lte_pos_sib_types

    @lte_pos_sib_types.setter
    def lte_pos_sib_types(self, lte_pos_sib_types):
        """Sets the lte_pos_sib_types of this CipheringDataSet.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :param lte_pos_sib_types: The lte_pos_sib_types of this CipheringDataSet.
        :type lte_pos_sib_types: str
        """

        self._lte_pos_sib_types = lte_pos_sib_types

    @property
    def nr_pos_sib_types(self):
        """Gets the nr_pos_sib_types of this CipheringDataSet.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :return: The nr_pos_sib_types of this CipheringDataSet.
        :rtype: str
        """
        return self._nr_pos_sib_types

    @nr_pos_sib_types.setter
    def nr_pos_sib_types(self, nr_pos_sib_types):
        """Sets the nr_pos_sib_types of this CipheringDataSet.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :param nr_pos_sib_types: The nr_pos_sib_types of this CipheringDataSet.
        :type nr_pos_sib_types: str
        """

        self._nr_pos_sib_types = nr_pos_sib_types

    @property
    def validity_start_time(self):
        """Gets the validity_start_time of this CipheringDataSet.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The validity_start_time of this CipheringDataSet.
        :rtype: datetime
        """
        return self._validity_start_time

    @validity_start_time.setter
    def validity_start_time(self, validity_start_time):
        """Sets the validity_start_time of this CipheringDataSet.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param validity_start_time: The validity_start_time of this CipheringDataSet.
        :type validity_start_time: datetime
        """
        if validity_start_time is None:
            raise ValueError("Invalid value for `validity_start_time`, must not be `None`")  # noqa: E501

        self._validity_start_time = validity_start_time

    @property
    def validity_duration(self):
        """Gets the validity_duration of this CipheringDataSet.

        Validity Duration of the Ciphering Data Set.  # noqa: E501

        :return: The validity_duration of this CipheringDataSet.
        :rtype: int
        """
        return self._validity_duration

    @validity_duration.setter
    def validity_duration(self, validity_duration):
        """Sets the validity_duration of this CipheringDataSet.

        Validity Duration of the Ciphering Data Set.  # noqa: E501

        :param validity_duration: The validity_duration of this CipheringDataSet.
        :type validity_duration: int
        """
        if validity_duration is None:
            raise ValueError("Invalid value for `validity_duration`, must not be `None`")  # noqa: E501
        if validity_duration is not None and validity_duration > 65535:  # noqa: E501
            raise ValueError("Invalid value for `validity_duration`, must be a value less than or equal to `65535`")  # noqa: E501
        if validity_duration is not None and validity_duration < 1:  # noqa: E501
            raise ValueError("Invalid value for `validity_duration`, must be a value greater than or equal to `1`")  # noqa: E501

        self._validity_duration = validity_duration

    @property
    def tai_list(self):
        """Gets the tai_list of this CipheringDataSet.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :return: The tai_list of this CipheringDataSet.
        :rtype: str
        """
        return self._tai_list

    @tai_list.setter
    def tai_list(self, tai_list):
        """Sets the tai_list of this CipheringDataSet.

        string with format 'bytes' as defined in OpenAPI  # noqa: E501

        :param tai_list: The tai_list of this CipheringDataSet.
        :type tai_list: str
        """

        self._tai_list = tai_list
