#!/usr/bin/env python3

import connexion

from lmf_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('Broadcast.yaml',
                arguments={'title': 'LMF Broadcast'},
                pythonic_params=True)
    app.add_api('Location.yaml',
                arguments={'title': 'LMF Location'},
                pythonic_params=True)
    app.add_api('NewService.yaml',
                arguments={'title': 'LMF NewService'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
