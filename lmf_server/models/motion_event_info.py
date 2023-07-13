# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.occurrence_info import OccurrenceInfo
from lmf_server import util

from lmf_server.models.occurrence_info import OccurrenceInfo  # noqa: E501

class MotionEventInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, linear_distance=None, occurrence_info=None, minimum_interval=None, maximum_interval=None, sampling_interval=None, reporting_duration=None, reporting_location_req=True):  # noqa: E501
        """MotionEventInfo - a model defined in OpenAPI

        :param linear_distance: The linear_distance of this MotionEventInfo.  # noqa: E501
        :type linear_distance: int
        :param occurrence_info: The occurrence_info of this MotionEventInfo.  # noqa: E501
        :type occurrence_info: OccurrenceInfo
        :param minimum_interval: The minimum_interval of this MotionEventInfo.  # noqa: E501
        :type minimum_interval: int
        :param maximum_interval: The maximum_interval of this MotionEventInfo.  # noqa: E501
        :type maximum_interval: int
        :param sampling_interval: The sampling_interval of this MotionEventInfo.  # noqa: E501
        :type sampling_interval: int
        :param reporting_duration: The reporting_duration of this MotionEventInfo.  # noqa: E501
        :type reporting_duration: int
        :param reporting_location_req: The reporting_location_req of this MotionEventInfo.  # noqa: E501
        :type reporting_location_req: bool
        """
        self.openapi_types = {
            'linear_distance': int,
            'occurrence_info': OccurrenceInfo,
            'minimum_interval': int,
            'maximum_interval': int,
            'sampling_interval': int,
            'reporting_duration': int,
            'reporting_location_req': bool
        }

        self.attribute_map = {
            'linear_distance': 'linearDistance',
            'occurrence_info': 'occurrenceInfo',
            'minimum_interval': 'minimumInterval',
            'maximum_interval': 'maximumInterval',
            'sampling_interval': 'samplingInterval',
            'reporting_duration': 'reportingDuration',
            'reporting_location_req': 'reportingLocationReq'
        }

        self._linear_distance = linear_distance
        self._occurrence_info = occurrence_info
        self._minimum_interval = minimum_interval
        self._maximum_interval = maximum_interval
        self._sampling_interval = sampling_interval
        self._reporting_duration = reporting_duration
        self._reporting_location_req = reporting_location_req

    @classmethod
    def from_dict(cls, dikt) -> 'MotionEventInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MotionEventInfo of this MotionEventInfo.  # noqa: E501
        :rtype: MotionEventInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def linear_distance(self):
        """Gets the linear_distance of this MotionEventInfo.

        Minimum straight line distance moved by a UE to trigger a motion event report.  # noqa: E501

        :return: The linear_distance of this MotionEventInfo.
        :rtype: int
        """
        return self._linear_distance

    @linear_distance.setter
    def linear_distance(self, linear_distance):
        """Sets the linear_distance of this MotionEventInfo.

        Minimum straight line distance moved by a UE to trigger a motion event report.  # noqa: E501

        :param linear_distance: The linear_distance of this MotionEventInfo.
        :type linear_distance: int
        """
        if linear_distance is None:
            raise ValueError("Invalid value for `linear_distance`, must not be `None`")  # noqa: E501
        if linear_distance is not None and linear_distance > 10000:  # noqa: E501
            raise ValueError("Invalid value for `linear_distance`, must be a value less than or equal to `10000`")  # noqa: E501
        if linear_distance is not None and linear_distance < 1:  # noqa: E501
            raise ValueError("Invalid value for `linear_distance`, must be a value greater than or equal to `1`")  # noqa: E501

        self._linear_distance = linear_distance

    @property
    def occurrence_info(self):
        """Gets the occurrence_info of this MotionEventInfo.


        :return: The occurrence_info of this MotionEventInfo.
        :rtype: OccurrenceInfo
        """
        return self._occurrence_info

    @occurrence_info.setter
    def occurrence_info(self, occurrence_info):
        """Sets the occurrence_info of this MotionEventInfo.


        :param occurrence_info: The occurrence_info of this MotionEventInfo.
        :type occurrence_info: OccurrenceInfo
        """

        self._occurrence_info = occurrence_info

    @property
    def minimum_interval(self):
        """Gets the minimum_interval of this MotionEventInfo.

        Minimum interval between event reports.  # noqa: E501

        :return: The minimum_interval of this MotionEventInfo.
        :rtype: int
        """
        return self._minimum_interval

    @minimum_interval.setter
    def minimum_interval(self, minimum_interval):
        """Sets the minimum_interval of this MotionEventInfo.

        Minimum interval between event reports.  # noqa: E501

        :param minimum_interval: The minimum_interval of this MotionEventInfo.
        :type minimum_interval: int
        """
        if minimum_interval is not None and minimum_interval > 32767:  # noqa: E501
            raise ValueError("Invalid value for `minimum_interval`, must be a value less than or equal to `32767`")  # noqa: E501
        if minimum_interval is not None and minimum_interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `minimum_interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._minimum_interval = minimum_interval

    @property
    def maximum_interval(self):
        """Gets the maximum_interval of this MotionEventInfo.

        Maximum interval between event reports.  # noqa: E501

        :return: The maximum_interval of this MotionEventInfo.
        :rtype: int
        """
        return self._maximum_interval

    @maximum_interval.setter
    def maximum_interval(self, maximum_interval):
        """Sets the maximum_interval of this MotionEventInfo.

        Maximum interval between event reports.  # noqa: E501

        :param maximum_interval: The maximum_interval of this MotionEventInfo.
        :type maximum_interval: int
        """
        if maximum_interval is not None and maximum_interval > 86400:  # noqa: E501
            raise ValueError("Invalid value for `maximum_interval`, must be a value less than or equal to `86400`")  # noqa: E501
        if maximum_interval is not None and maximum_interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `maximum_interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._maximum_interval = maximum_interval

    @property
    def sampling_interval(self):
        """Gets the sampling_interval of this MotionEventInfo.

        Maximum time interval between consecutive evaluations by a UE of a trigger event.  # noqa: E501

        :return: The sampling_interval of this MotionEventInfo.
        :rtype: int
        """
        return self._sampling_interval

    @sampling_interval.setter
    def sampling_interval(self, sampling_interval):
        """Sets the sampling_interval of this MotionEventInfo.

        Maximum time interval between consecutive evaluations by a UE of a trigger event.  # noqa: E501

        :param sampling_interval: The sampling_interval of this MotionEventInfo.
        :type sampling_interval: int
        """
        if sampling_interval is not None and sampling_interval > 3600:  # noqa: E501
            raise ValueError("Invalid value for `sampling_interval`, must be a value less than or equal to `3600`")  # noqa: E501
        if sampling_interval is not None and sampling_interval < 1:  # noqa: E501
            raise ValueError("Invalid value for `sampling_interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._sampling_interval = sampling_interval

    @property
    def reporting_duration(self):
        """Gets the reporting_duration of this MotionEventInfo.

        Maximum duration of event reporting.  # noqa: E501

        :return: The reporting_duration of this MotionEventInfo.
        :rtype: int
        """
        return self._reporting_duration

    @reporting_duration.setter
    def reporting_duration(self, reporting_duration):
        """Sets the reporting_duration of this MotionEventInfo.

        Maximum duration of event reporting.  # noqa: E501

        :param reporting_duration: The reporting_duration of this MotionEventInfo.
        :type reporting_duration: int
        """
        if reporting_duration is not None and reporting_duration > 8640000:  # noqa: E501
            raise ValueError("Invalid value for `reporting_duration`, must be a value less than or equal to `8640000`")  # noqa: E501
        if reporting_duration is not None and reporting_duration < 1:  # noqa: E501
            raise ValueError("Invalid value for `reporting_duration`, must be a value greater than or equal to `1`")  # noqa: E501

        self._reporting_duration = reporting_duration

    @property
    def reporting_location_req(self):
        """Gets the reporting_location_req of this MotionEventInfo.


        :return: The reporting_location_req of this MotionEventInfo.
        :rtype: bool
        """
        return self._reporting_location_req

    @reporting_location_req.setter
    def reporting_location_req(self, reporting_location_req):
        """Sets the reporting_location_req of this MotionEventInfo.


        :param reporting_location_req: The reporting_location_req of this MotionEventInfo.
        :type reporting_location_req: bool
        """

        self._reporting_location_req = reporting_location_req
