import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from lmf_server.models.problem_details import ProblemDetails  # noqa: E501
from lmf_server.models.redirect_response import RedirectResponse  # noqa: E501
from lmf_server.models.relative_data import RelativeData  # noqa: E501
from lmf_server import util


def relative_location():  # noqa: E501
    """UEs within a particular radius around a specific UE

     # noqa: E501

    :param relative_data: 
    :type relative_data: dict | bytes

    :rtype: Union[RelativeData, Tuple[RelativeData, int], Tuple[RelativeData, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        relative_data = RelativeData.from_dict(connexion.request.get_json())  # noqa: E501
        print ("Receive the relative_location request with: \n", relative_data)
    return 'Receive relative_location request and Send the result! relative_location API Test OK'
