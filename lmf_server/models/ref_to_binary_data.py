# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server import util


class RefToBinaryData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, content_id=None):  # noqa: E501
        """RefToBinaryData - a model defined in OpenAPI

        :param content_id: The content_id of this RefToBinaryData.  # noqa: E501
        :type content_id: str
        """
        self.openapi_types = {
            'content_id': str
        }

        self.attribute_map = {
            'content_id': 'contentId'
        }

        self._content_id = content_id

    @classmethod
    def from_dict(cls, dikt) -> 'RefToBinaryData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RefToBinaryData of this RefToBinaryData.  # noqa: E501
        :rtype: RefToBinaryData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def content_id(self):
        """Gets the content_id of this RefToBinaryData.

        This IE shall contain the value of the Content-ID header of the referenced binary body part.   # noqa: E501

        :return: The content_id of this RefToBinaryData.
        :rtype: str
        """
        return self._content_id

    @content_id.setter
    def content_id(self, content_id):
        """Sets the content_id of this RefToBinaryData.

        This IE shall contain the value of the Content-ID header of the referenced binary body part.   # noqa: E501

        :param content_id: The content_id of this RefToBinaryData.
        :type content_id: str
        """
        if content_id is None:
            raise ValueError("Invalid value for `content_id`, must not be `None`")  # noqa: E501

        self._content_id = content_id