import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from lmf_server.models.cipher_request_data import CipherRequestData  # noqa: E501
from lmf_server.models.cipher_response_data import CipherResponseData  # noqa: E501
from lmf_server.models.problem_details import ProblemDetails  # noqa: E501
from lmf_server.models.redirect_response import RedirectResponse  # noqa: E501
from lmf_server import util


def ciphering_key_data():  # noqa: E501
    """Request ciphering key data

     # noqa: E501

    :param cipher_request_data: 
    :type cipher_request_data: dict | bytes

    :rtype: Union[CipherResponseData, Tuple[CipherResponseData, int], Tuple[CipherResponseData, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        cipher_request_data = CipherRequestData.from_dict(connexion.request.get_json())  # noqa: E501
        print("Receive the ciphering_key_data request with: \n", cipher_request_data)
    return 'Receive ciphering_key_data request and Send the result! ciphering_key_data API Test OK'
