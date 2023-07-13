import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from lmf_server.models.cancel_loc_data import CancelLocData  # noqa: E501
from lmf_server.models.problem_details import ProblemDetails  # noqa: E501
from lmf_server.models.redirect_response import RedirectResponse  # noqa: E501
from lmf_server import util


def cancel_location():  # noqa: E501

    if connexion.request.is_json:
        cancel_loc_data = CancelLocData.from_dict(connexion.request.get_json())
        print ("Receive the cancel_location request with: \n", cancel_loc_data)
    return 'Receive cancel-location request and Send the result! cancel-location API Test OK'
