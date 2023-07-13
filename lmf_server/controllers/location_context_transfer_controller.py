import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from lmf_server.models.loc_context_data import LocContextData  # noqa: E501
from lmf_server.models.problem_details import ProblemDetails  # noqa: E501
from lmf_server.models.redirect_response import RedirectResponse  # noqa: E501
from lmf_server import util


def location_context_transfer():  # noqa: E501

    if connexion.request.is_json:
        loc_context_data = LocContextData.from_dict(connexion.request.get_json())  # noqa: E501
        print ("Receive the location_context_transfer request with: \n ", loc_context_data)
    return 'Receive location_context_transfer request and Send the result! location_context_transfer API Test OK'
