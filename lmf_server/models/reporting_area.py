# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.ecgi import Ecgi
from lmf_server.models.ncgi import Ncgi
from lmf_server.models.reporting_area_type import ReportingAreaType
from lmf_server.models.tai import Tai
from lmf_server import util

from lmf_server.models.ecgi import Ecgi  # noqa: E501
from lmf_server.models.ncgi import Ncgi  # noqa: E501
from lmf_server.models.reporting_area_type import ReportingAreaType  # noqa: E501
from lmf_server.models.tai import Tai  # noqa: E501

class ReportingArea(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, area_type=None, tai=None, ecgi=None, ncgi=None):  # noqa: E501
        """ReportingArea - a model defined in OpenAPI

        :param area_type: The area_type of this ReportingArea.  # noqa: E501
        :type area_type: ReportingAreaType
        :param tai: The tai of this ReportingArea.  # noqa: E501
        :type tai: Tai
        :param ecgi: The ecgi of this ReportingArea.  # noqa: E501
        :type ecgi: Ecgi
        :param ncgi: The ncgi of this ReportingArea.  # noqa: E501
        :type ncgi: Ncgi
        """
        self.openapi_types = {
            'area_type': ReportingAreaType,
            'tai': Tai,
            'ecgi': Ecgi,
            'ncgi': Ncgi
        }

        self.attribute_map = {
            'area_type': 'areaType',
            'tai': 'tai',
            'ecgi': 'ecgi',
            'ncgi': 'ncgi'
        }

        self._area_type = area_type
        self._tai = tai
        self._ecgi = ecgi
        self._ncgi = ncgi

    @classmethod
    def from_dict(cls, dikt) -> 'ReportingArea':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ReportingArea of this ReportingArea.  # noqa: E501
        :rtype: ReportingArea
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_type(self):
        """Gets the area_type of this ReportingArea.


        :return: The area_type of this ReportingArea.
        :rtype: ReportingAreaType
        """
        return self._area_type

    @area_type.setter
    def area_type(self, area_type):
        """Sets the area_type of this ReportingArea.


        :param area_type: The area_type of this ReportingArea.
        :type area_type: ReportingAreaType
        """
        #if area_type is None:
        #    raise ValueError("Invalid value for `area_type`, must not be `None`")  # noqa: E501

        self._area_type = area_type

    @property
    def tai(self):
        """Gets the tai of this ReportingArea.


        :return: The tai of this ReportingArea.
        :rtype: Tai
        """
        return self._tai

    @tai.setter
    def tai(self, tai):
        """Sets the tai of this ReportingArea.


        :param tai: The tai of this ReportingArea.
        :type tai: Tai
        """

        self._tai = tai

    @property
    def ecgi(self):
        """Gets the ecgi of this ReportingArea.


        :return: The ecgi of this ReportingArea.
        :rtype: Ecgi
        """
        return self._ecgi

    @ecgi.setter
    def ecgi(self, ecgi):
        """Sets the ecgi of this ReportingArea.


        :param ecgi: The ecgi of this ReportingArea.
        :type ecgi: Ecgi
        """

        self._ecgi = ecgi

    @property
    def ncgi(self):
        """Gets the ncgi of this ReportingArea.


        :return: The ncgi of this ReportingArea.
        :rtype: Ncgi
        """
        return self._ncgi

    @ncgi.setter
    def ncgi(self, ncgi):
        """Sets the ncgi of this ReportingArea.


        :param ncgi: The ncgi of this ReportingArea.
        :type ncgi: Ncgi
        """

        self._ncgi = ncgi
