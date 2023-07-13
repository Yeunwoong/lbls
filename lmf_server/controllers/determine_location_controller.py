import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from lmf_server.models.input_data import InputData  # noqa: E501
from lmf_server.models.location_data import LocationData  # noqa: E501
from lmf_server.models.problem_details import ProblemDetails  # noqa: E501
from lmf_server.models.redirect_response import RedirectResponse  # noqa: E501
from lmf_server import util


def determine_location():  # noqa: E501

    if connexion.request.is_json:
        input_data = InputData.from_dict(connexion.request.get_json())
        print ("Receive the determine_location request with: \n", input_data)
    return 'Receive determine-location request and Send the result! determine-location API Test OK'
