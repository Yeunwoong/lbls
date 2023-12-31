# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from lmf_server.models.base_model_ import Model
from lmf_server.models.civic_address import CivicAddress
from lmf_server.models.geographic_area import GeographicArea
from lmf_server.models.gnss_positioning_method_and_usage import GnssPositioningMethodAndUsage
from lmf_server.models.local_area import LocalArea
from lmf_server.models.minor_location_qo_s import MinorLocationQoS
from lmf_server.models.positioning_method_and_usage import PositioningMethodAndUsage
from lmf_server.models.reported_event_type import ReportedEventType
from lmf_server.models.termination_cause import TerminationCause
from lmf_server.models.velocity_estimate import VelocityEstimate
import re
from lmf_server import util

from lmf_server.models.civic_address import CivicAddress  # noqa: E501
from lmf_server.models.geographic_area import GeographicArea  # noqa: E501
from lmf_server.models.gnss_positioning_method_and_usage import GnssPositioningMethodAndUsage  # noqa: E501
from lmf_server.models.local_area import LocalArea  # noqa: E501
from lmf_server.models.minor_location_qo_s import MinorLocationQoS  # noqa: E501
from lmf_server.models.positioning_method_and_usage import PositioningMethodAndUsage  # noqa: E501
from lmf_server.models.reported_event_type import ReportedEventType  # noqa: E501
from lmf_server.models.termination_cause import TerminationCause  # noqa: E501
from lmf_server.models.velocity_estimate import VelocityEstimate  # noqa: E501
import re  # noqa: E501

class EventNotifyData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, reported_event_type=None, supi=None, gpsi=None, hgmlc_call_back_uri=None, ldr_reference=None, lir_reference=None, location_estimate=None, age_of_location_estimate=None, timestamp_of_location_estimate=None, civic_address=None, local_location_estimate=None, positioning_data_list=None, gnss_positioning_data_list=None, serving_lm_fidentification=None, termination_cause=None, velocity_estimate=None, altitude=None, achieved_qos=None, supported_features=None):  # noqa: E501
        """EventNotifyData - a model defined in OpenAPI

        :param reported_event_type: The reported_event_type of this EventNotifyData.  # noqa: E501
        :type reported_event_type: ReportedEventType
        :param supi: The supi of this EventNotifyData.  # noqa: E501
        :type supi: str
        :param gpsi: The gpsi of this EventNotifyData.  # noqa: E501
        :type gpsi: str
        :param hgmlc_call_back_uri: The hgmlc_call_back_uri of this EventNotifyData.  # noqa: E501
        :type hgmlc_call_back_uri: str
        :param ldr_reference: The ldr_reference of this EventNotifyData.  # noqa: E501
        :type ldr_reference: str
        :param lir_reference: The lir_reference of this EventNotifyData.  # noqa: E501
        :type lir_reference: str
        :param location_estimate: The location_estimate of this EventNotifyData.  # noqa: E501
        :type location_estimate: GeographicArea
        :param age_of_location_estimate: The age_of_location_estimate of this EventNotifyData.  # noqa: E501
        :type age_of_location_estimate: int
        :param timestamp_of_location_estimate: The timestamp_of_location_estimate of this EventNotifyData.  # noqa: E501
        :type timestamp_of_location_estimate: datetime
        :param civic_address: The civic_address of this EventNotifyData.  # noqa: E501
        :type civic_address: CivicAddress
        :param local_location_estimate: The local_location_estimate of this EventNotifyData.  # noqa: E501
        :type local_location_estimate: LocalArea
        :param positioning_data_list: The positioning_data_list of this EventNotifyData.  # noqa: E501
        :type positioning_data_list: List[PositioningMethodAndUsage]
        :param gnss_positioning_data_list: The gnss_positioning_data_list of this EventNotifyData.  # noqa: E501
        :type gnss_positioning_data_list: List[GnssPositioningMethodAndUsage]
        :param serving_lm_fidentification: The serving_lm_fidentification of this EventNotifyData.  # noqa: E501
        :type serving_lm_fidentification: str
        :param termination_cause: The termination_cause of this EventNotifyData.  # noqa: E501
        :type termination_cause: TerminationCause
        :param velocity_estimate: The velocity_estimate of this EventNotifyData.  # noqa: E501
        :type velocity_estimate: VelocityEstimate
        :param altitude: The altitude of this EventNotifyData.  # noqa: E501
        :type altitude: float
        :param achieved_qos: The achieved_qos of this EventNotifyData.  # noqa: E501
        :type achieved_qos: MinorLocationQoS
        :param supported_features: The supported_features of this EventNotifyData.  # noqa: E501
        :type supported_features: str
        """
        self.openapi_types = {
            'reported_event_type': ReportedEventType,
            'supi': str,
            'gpsi': str,
            'hgmlc_call_back_uri': str,
            'ldr_reference': str,
            'lir_reference': str,
            'location_estimate': GeographicArea,
            'age_of_location_estimate': int,
            'timestamp_of_location_estimate': datetime,
            'civic_address': CivicAddress,
            'local_location_estimate': LocalArea,
            'positioning_data_list': List[PositioningMethodAndUsage],
            'gnss_positioning_data_list': List[GnssPositioningMethodAndUsage],
            'serving_lm_fidentification': str,
            'termination_cause': TerminationCause,
            'velocity_estimate': VelocityEstimate,
            'altitude': float,
            'achieved_qos': MinorLocationQoS,
            'supported_features': str
        }

        self.attribute_map = {
            'reported_event_type': 'reportedEventType',
            'supi': 'supi',
            'gpsi': 'gpsi',
            'hgmlc_call_back_uri': 'hgmlcCallBackURI',
            'ldr_reference': 'ldrReference',
            'lir_reference': 'lirReference',
            'location_estimate': 'locationEstimate',
            'age_of_location_estimate': 'ageOfLocationEstimate',
            'timestamp_of_location_estimate': 'timestampOfLocationEstimate',
            'civic_address': 'civicAddress',
            'local_location_estimate': 'localLocationEstimate',
            'positioning_data_list': 'positioningDataList',
            'gnss_positioning_data_list': 'gnssPositioningDataList',
            'serving_lm_fidentification': 'servingLMFidentification',
            'termination_cause': 'terminationCause',
            'velocity_estimate': 'velocityEstimate',
            'altitude': 'altitude',
            'achieved_qos': 'achievedQos',
            'supported_features': 'supportedFeatures'
        }

        self._reported_event_type = reported_event_type
        self._supi = supi
        self._gpsi = gpsi
        self._hgmlc_call_back_uri = hgmlc_call_back_uri
        self._ldr_reference = ldr_reference
        self._lir_reference = lir_reference
        self._location_estimate = location_estimate
        self._age_of_location_estimate = age_of_location_estimate
        self._timestamp_of_location_estimate = timestamp_of_location_estimate
        self._civic_address = civic_address
        self._local_location_estimate = local_location_estimate
        self._positioning_data_list = positioning_data_list
        self._gnss_positioning_data_list = gnss_positioning_data_list
        self._serving_lm_fidentification = serving_lm_fidentification
        self._termination_cause = termination_cause
        self._velocity_estimate = velocity_estimate
        self._altitude = altitude
        self._achieved_qos = achieved_qos
        self._supported_features = supported_features

    @classmethod
    def from_dict(cls, dikt) -> 'EventNotifyData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventNotifyData of this EventNotifyData.  # noqa: E501
        :rtype: EventNotifyData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def reported_event_type(self):
        """Gets the reported_event_type of this EventNotifyData.


        :return: The reported_event_type of this EventNotifyData.
        :rtype: ReportedEventType
        """
        return self._reported_event_type

    @reported_event_type.setter
    def reported_event_type(self, reported_event_type):
        """Sets the reported_event_type of this EventNotifyData.


        :param reported_event_type: The reported_event_type of this EventNotifyData.
        :type reported_event_type: ReportedEventType
        """
        if reported_event_type is None:
            raise ValueError("Invalid value for `reported_event_type`, must not be `None`")  # noqa: E501

        self._reported_event_type = reported_event_type

    @property
    def supi(self):
        """Gets the supi of this EventNotifyData.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :return: The supi of this EventNotifyData.
        :rtype: str
        """
        return self._supi

    @supi.setter
    def supi(self, supi):
        """Sets the supi of this EventNotifyData.

        String identifying a Supi that shall contain either an IMSI, a network specific identifier, a Global Cable Identifier (GCI) or a Global Line Identifier (GLI) as specified in clause  2.2A of 3GPP TS 23.003. It shall be formatted as follows  - for an IMSI \"imsi-<imsi>\", where <imsi> shall be formatted according to clause 2.2    of 3GPP TS 23.003 that describes an IMSI.  - for a network specific identifier \"nai-<nai>, where <nai> shall be formatted    according to clause 28.7.2 of 3GPP TS 23.003 that describes an NAI.  - for a GCI \"gci-<gci>\", where <gci> shall be formatted according to clause 28.15.2    of 3GPP TS 23.003.  - for a GLI \"gli-<gli>\", where <gli> shall be formatted according to clause 28.16.2 of    3GPP TS 23.003.To enable that the value is used as part of an URI, the string shall    only contain characters allowed according to the \"lower-with-hyphen\" naming convention    defined in 3GPP TS 29.501.   # noqa: E501

        :param supi: The supi of this EventNotifyData.
        :type supi: str
        """
        #if supi is not None and not re.search(r'^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$', supi):  # noqa: E501
        #    raise ValueError("Invalid value for `supi`, must be a follow pattern or equal to `/^(imsi-[0-9]{5,15}|nai-.+|gci-.+|gli-.+|.+)$/`")  # noqa: E501

        self._supi = supi

    @property
    def gpsi(self):
        """Gets the gpsi of this EventNotifyData.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :return: The gpsi of this EventNotifyData.
        :rtype: str
        """
        return self._gpsi

    @gpsi.setter
    def gpsi(self, gpsi):
        """Sets the gpsi of this EventNotifyData.

        String identifying a Gpsi shall contain either an External Id or an MSISDN.  It shall be formatted as follows -External Identifier= \"extid-'extid', where 'extid'  shall be formatted according to clause 19.7.2 of 3GPP TS 23.003 that describes an  External Identifier.    # noqa: E501

        :param gpsi: The gpsi of this EventNotifyData.
        :type gpsi: str
        """
        #if gpsi is not None and not re.search(r'^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$', gpsi):  # noqa: E501
        #    raise ValueError("Invalid value for `gpsi`, must be a follow pattern or equal to `/^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$/`")  # noqa: E501

        self._gpsi = gpsi

    @property
    def hgmlc_call_back_uri(self):
        """Gets the hgmlc_call_back_uri of this EventNotifyData.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :return: The hgmlc_call_back_uri of this EventNotifyData.
        :rtype: str
        """
        return self._hgmlc_call_back_uri

    @hgmlc_call_back_uri.setter
    def hgmlc_call_back_uri(self, hgmlc_call_back_uri):
        """Sets the hgmlc_call_back_uri of this EventNotifyData.

        String providing an URI formatted according to RFC 3986.  # noqa: E501

        :param hgmlc_call_back_uri: The hgmlc_call_back_uri of this EventNotifyData.
        :type hgmlc_call_back_uri: str
        """

        self._hgmlc_call_back_uri = hgmlc_call_back_uri

    @property
    def ldr_reference(self):
        """Gets the ldr_reference of this EventNotifyData.

        LDR Reference.  # noqa: E501

        :return: The ldr_reference of this EventNotifyData.
        :rtype: str
        """
        return self._ldr_reference

    @ldr_reference.setter
    def ldr_reference(self, ldr_reference):
        """Sets the ldr_reference of this EventNotifyData.

        LDR Reference.  # noqa: E501

        :param ldr_reference: The ldr_reference of this EventNotifyData.
        :type ldr_reference: str
        """
        if ldr_reference is None:
            raise ValueError("Invalid value for `ldr_reference`, must not be `None`")  # noqa: E501
        if ldr_reference is not None and len(ldr_reference) > 510:
            raise ValueError("Invalid value for `ldr_reference`, length must be less than or equal to `510`")  # noqa: E501
        if ldr_reference is not None and len(ldr_reference) < 2:
            raise ValueError("Invalid value for `ldr_reference`, length must be greater than or equal to `2`")  # noqa: E501

        self._ldr_reference = ldr_reference

    @property
    def lir_reference(self):
        """Gets the lir_reference of this EventNotifyData.

        LIR Reference.  # noqa: E501

        :return: The lir_reference of this EventNotifyData.
        :rtype: str
        """
        return self._lir_reference

    @lir_reference.setter
    def lir_reference(self, lir_reference):
        """Sets the lir_reference of this EventNotifyData.

        LIR Reference.  # noqa: E501

        :param lir_reference: The lir_reference of this EventNotifyData.
        :type lir_reference: str
        """
        if lir_reference is not None and len(lir_reference) > 510:
            raise ValueError("Invalid value for `lir_reference`, length must be less than or equal to `510`")  # noqa: E501
        if lir_reference is not None and len(lir_reference) < 2:
            raise ValueError("Invalid value for `lir_reference`, length must be greater than or equal to `2`")  # noqa: E501

        self._lir_reference = lir_reference

    @property
    def location_estimate(self):
        """Gets the location_estimate of this EventNotifyData.


        :return: The location_estimate of this EventNotifyData.
        :rtype: GeographicArea
        """
        return self._location_estimate

    @location_estimate.setter
    def location_estimate(self, location_estimate):
        """Sets the location_estimate of this EventNotifyData.


        :param location_estimate: The location_estimate of this EventNotifyData.
        :type location_estimate: GeographicArea
        """

        self._location_estimate = location_estimate

    @property
    def age_of_location_estimate(self):
        """Gets the age_of_location_estimate of this EventNotifyData.

        Indicates value of the age of the location estimate.  # noqa: E501

        :return: The age_of_location_estimate of this EventNotifyData.
        :rtype: int
        """
        return self._age_of_location_estimate

    @age_of_location_estimate.setter
    def age_of_location_estimate(self, age_of_location_estimate):
        """Sets the age_of_location_estimate of this EventNotifyData.

        Indicates value of the age of the location estimate.  # noqa: E501

        :param age_of_location_estimate: The age_of_location_estimate of this EventNotifyData.
        :type age_of_location_estimate: int
        """
        if age_of_location_estimate is not None and age_of_location_estimate > 32767:  # noqa: E501
            raise ValueError("Invalid value for `age_of_location_estimate`, must be a value less than or equal to `32767`")  # noqa: E501
        if age_of_location_estimate is not None and age_of_location_estimate < 0:  # noqa: E501
            raise ValueError("Invalid value for `age_of_location_estimate`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age_of_location_estimate = age_of_location_estimate

    @property
    def timestamp_of_location_estimate(self):
        """Gets the timestamp_of_location_estimate of this EventNotifyData.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :return: The timestamp_of_location_estimate of this EventNotifyData.
        :rtype: datetime
        """
        return self._timestamp_of_location_estimate

    @timestamp_of_location_estimate.setter
    def timestamp_of_location_estimate(self, timestamp_of_location_estimate):
        """Sets the timestamp_of_location_estimate of this EventNotifyData.

        string with format 'date-time' as defined in OpenAPI.  # noqa: E501

        :param timestamp_of_location_estimate: The timestamp_of_location_estimate of this EventNotifyData.
        :type timestamp_of_location_estimate: datetime
        """

        self._timestamp_of_location_estimate = timestamp_of_location_estimate

    @property
    def civic_address(self):
        """Gets the civic_address of this EventNotifyData.


        :return: The civic_address of this EventNotifyData.
        :rtype: CivicAddress
        """
        return self._civic_address

    @civic_address.setter
    def civic_address(self, civic_address):
        """Sets the civic_address of this EventNotifyData.


        :param civic_address: The civic_address of this EventNotifyData.
        :type civic_address: CivicAddress
        """

        self._civic_address = civic_address

    @property
    def local_location_estimate(self):
        """Gets the local_location_estimate of this EventNotifyData.


        :return: The local_location_estimate of this EventNotifyData.
        :rtype: LocalArea
        """
        return self._local_location_estimate

    @local_location_estimate.setter
    def local_location_estimate(self, local_location_estimate):
        """Sets the local_location_estimate of this EventNotifyData.


        :param local_location_estimate: The local_location_estimate of this EventNotifyData.
        :type local_location_estimate: LocalArea
        """

        self._local_location_estimate = local_location_estimate

    @property
    def positioning_data_list(self):
        """Gets the positioning_data_list of this EventNotifyData.


        :return: The positioning_data_list of this EventNotifyData.
        :rtype: List[PositioningMethodAndUsage]
        """
        return self._positioning_data_list

    @positioning_data_list.setter
    def positioning_data_list(self, positioning_data_list):
        """Sets the positioning_data_list of this EventNotifyData.


        :param positioning_data_list: The positioning_data_list of this EventNotifyData.
        :type positioning_data_list: List[PositioningMethodAndUsage]
        """
        if positioning_data_list is not None and len(positioning_data_list) < 1:
            raise ValueError("Invalid value for `positioning_data_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._positioning_data_list = positioning_data_list

    @property
    def gnss_positioning_data_list(self):
        """Gets the gnss_positioning_data_list of this EventNotifyData.


        :return: The gnss_positioning_data_list of this EventNotifyData.
        :rtype: List[GnssPositioningMethodAndUsage]
        """
        return self._gnss_positioning_data_list

    @gnss_positioning_data_list.setter
    def gnss_positioning_data_list(self, gnss_positioning_data_list):
        """Sets the gnss_positioning_data_list of this EventNotifyData.


        :param gnss_positioning_data_list: The gnss_positioning_data_list of this EventNotifyData.
        :type gnss_positioning_data_list: List[GnssPositioningMethodAndUsage]
        """
        if gnss_positioning_data_list is not None and len(gnss_positioning_data_list) < 1:
            raise ValueError("Invalid value for `gnss_positioning_data_list`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._gnss_positioning_data_list = gnss_positioning_data_list

    @property
    def serving_lm_fidentification(self):
        """Gets the serving_lm_fidentification of this EventNotifyData.

        LMF identification.  # noqa: E501

        :return: The serving_lm_fidentification of this EventNotifyData.
        :rtype: str
        """
        return self._serving_lm_fidentification

    @serving_lm_fidentification.setter
    def serving_lm_fidentification(self, serving_lm_fidentification):
        """Sets the serving_lm_fidentification of this EventNotifyData.

        LMF identification.  # noqa: E501

        :param serving_lm_fidentification: The serving_lm_fidentification of this EventNotifyData.
        :type serving_lm_fidentification: str
        """

        self._serving_lm_fidentification = serving_lm_fidentification

    @property
    def termination_cause(self):
        """Gets the termination_cause of this EventNotifyData.


        :return: The termination_cause of this EventNotifyData.
        :rtype: TerminationCause
        """
        return self._termination_cause

    @termination_cause.setter
    def termination_cause(self, termination_cause):
        """Sets the termination_cause of this EventNotifyData.


        :param termination_cause: The termination_cause of this EventNotifyData.
        :type termination_cause: TerminationCause
        """

        self._termination_cause = termination_cause

    @property
    def velocity_estimate(self):
        """Gets the velocity_estimate of this EventNotifyData.


        :return: The velocity_estimate of this EventNotifyData.
        :rtype: VelocityEstimate
        """
        return self._velocity_estimate

    @velocity_estimate.setter
    def velocity_estimate(self, velocity_estimate):
        """Sets the velocity_estimate of this EventNotifyData.


        :param velocity_estimate: The velocity_estimate of this EventNotifyData.
        :type velocity_estimate: VelocityEstimate
        """

        self._velocity_estimate = velocity_estimate

    @property
    def altitude(self):
        """Gets the altitude of this EventNotifyData.

        Indicates value of altitude.  # noqa: E501

        :return: The altitude of this EventNotifyData.
        :rtype: float
        """
        return self._altitude

    @altitude.setter
    def altitude(self, altitude):
        """Sets the altitude of this EventNotifyData.

        Indicates value of altitude.  # noqa: E501

        :param altitude: The altitude of this EventNotifyData.
        :type altitude: float
        """
        if altitude is not None and altitude > 32767:  # noqa: E501
            raise ValueError("Invalid value for `altitude`, must be a value less than or equal to `32767`")  # noqa: E501
        if altitude is not None and altitude < -32767:  # noqa: E501
            raise ValueError("Invalid value for `altitude`, must be a value greater than or equal to `-32767`")  # noqa: E501

        self._altitude = altitude

    @property
    def achieved_qos(self):
        """Gets the achieved_qos of this EventNotifyData.


        :return: The achieved_qos of this EventNotifyData.
        :rtype: MinorLocationQoS
        """
        return self._achieved_qos

    @achieved_qos.setter
    def achieved_qos(self, achieved_qos):
        """Sets the achieved_qos of this EventNotifyData.


        :param achieved_qos: The achieved_qos of this EventNotifyData.
        :type achieved_qos: MinorLocationQoS
        """

        self._achieved_qos = achieved_qos

    @property
    def supported_features(self):
        """Gets the supported_features of this EventNotifyData.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :return: The supported_features of this EventNotifyData.
        :rtype: str
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this EventNotifyData.

        A string used to indicate the features supported by an API that is used as defined in clause  6.6 in 3GPP TS 29.500. The string shall contain a bitmask indicating supported features in  hexadecimal representation Each character in the string shall take a value of \"0\" to \"9\",  \"a\" to \"f\" or \"A\" to \"F\" and shall represent the support of 4 features as described in  table 5.2.2-3. The most significant character representing the highest-numbered features shall  appear first in the string, and the character representing features 1 to 4 shall appear last  in the string. The list of features and their numbering (starting with 1) are defined  separately for each API. If the string contains a lower number of characters than there are  defined features for an API, all features that would be represented by characters that are not  present in the string are not supported.   # noqa: E501

        :param supported_features: The supported_features of this EventNotifyData.
        :type supported_features: str
        """
        #if supported_features is not None and not re.search(r'^[A-Fa-f0-9]*$', supported_features):  # noqa: E501
        #    raise ValueError("Invalid value for `supported_features`, must be a follow pattern or equal to `/^[A-Fa-f0-9]*$/`")  # noqa: E501

        self._supported_features = supported_features
