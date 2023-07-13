# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server import util


class LcsQosClass(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """LcsQosClass - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'LcsQosClass':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LcsQosClass of this LcsQosClass.  # noqa: E501
        :rtype: LcsQosClass
        """
        return util.deserialize_model(dikt, cls)
