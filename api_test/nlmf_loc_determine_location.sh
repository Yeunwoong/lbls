
# Determine Location Reqeust Data

curl -X 'POST' \
  'http://localhost:8080/nlmf-loc/v1/determine-location' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "amfId": "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "areaEventInfo": {
    "areaDefinition": [
      {
        "areaType": null,
        "ecgi": {
          "eutraCellId": "eutraCellId",
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "ncgi": {
          "nid": "nid",
          "nrCellId": "nrCellId",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "tai": {
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          },
          "tac": "tac"
        }
      },
      {
        "areaType": null,
        "ecgi": {
          "eutraCellId": "eutraCellId",
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "ncgi": {
          "nid": "nid",
          "nrCellId": "nrCellId",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "tai": {
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          },
          "tac": "tac"
        }
      },
      {
        "areaType": null,
        "ecgi": {
          "eutraCellId": "eutraCellId",
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "ncgi": {
          "nid": "nid",
          "nrCellId": "nrCellId",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "tai": {
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          },
          "tac": "tac"
        }
      },
      {
        "areaType": null,
        "ecgi": {
          "eutraCellId": "eutraCellId",
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "ncgi": {
          "nid": "nid",
          "nrCellId": "nrCellId",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "tai": {
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          },
          "tac": "tac"
        }
      },
      {
        "areaType": null,
        "ecgi": {
          "eutraCellId": "eutraCellId",
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "ncgi": {
          "nid": "nid",
          "nrCellId": "nrCellId",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          }
        },
        "tai": {
          "nid": "nid",
          "plmnId": {
            "mcc": "mcc",
            "mnc": "mnc"
          },
          "tac": "tac"
        }
      }
    ],
    "maximumInterval": 61010,
    "minimumInterval": 7544,
    "occurrenceInfo": null,
    "reportingDuration": 3124290,
    "reportingLocationReq": true,
    "samplingInterval": 3348
  },
  "correlationID": "correlationID",
  "ecgi": {
    "eutraCellId": "eutraCellId",
    "nid": "nid",
    "plmnId": {
      "mcc": "mcc",
      "mnc": "mnc"
    }
  },
  "ecgiOnSecondNode": {
    "eutraCellId": "eutraCellId",
    "nid": "nid",
    "plmnId": {
      "mcc": "mcc",
      "mnc": "mnc"
    }
  },
  "evtRptAllowedAreas": [
    {
      "areaType": null,
      "ecgi": {
        "eutraCellId": "eutraCellId",
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "ncgi": {
        "nid": "nid",
        "nrCellId": "nrCellId",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "tai": {
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        },
        "tac": "tac"
      }
    },
    {
      "areaType": null,
      "ecgi": {
        "eutraCellId": "eutraCellId",
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "ncgi": {
        "nid": "nid",
        "nrCellId": "nrCellId",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "tai": {
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        },
        "tac": "tac"
      }
    },
    {
      "areaType": null,
      "ecgi": {
        "eutraCellId": "eutraCellId",
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "ncgi": {
        "nid": "nid",
        "nrCellId": "nrCellId",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "tai": {
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        },
        "tac": "tac"
      }
    },
    {
      "areaType": null,
      "ecgi": {
        "eutraCellId": "eutraCellId",
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "ncgi": {
        "nid": "nid",
        "nrCellId": "nrCellId",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "tai": {
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        },
        "tac": "tac"
      }
    },
    {
      "areaType": null,
      "ecgi": {
        "eutraCellId": "eutraCellId",
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "ncgi": {
        "nid": "nid",
        "nrCellId": "nrCellId",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        }
      },
      "tai": {
        "nid": "nid",
        "plmnId": {
          "mcc": "mcc",
          "mnc": "mnc"
        },
        "tac": "tac"
      }
    }
  ],
  "externalClientType": null,
  "gpsi": "gpsi",
  "hgmlcCallBackURI": "hgmlcCallBackURI",
  "intermediateLocationInd": false,
  "lcsServiceType": 18,
  "ldrReference": "ldrReference",
  "ldrType": null,
  "lirGmlcCallBackUri": "lirGmlcCallBackUri",
  "lirReference": "lirReference",
  "locationQoS": {
    "hAccuracy": 0.08008282,
    "lcsQosClass": null,
    "minorLocQoses": [
      {
        "hAccuracy": 0.5637377,
        "vAccuracy": 0.23021358
      },
      {
        "hAccuracy": 0.5637377,
        "vAccuracy": 0.23021358
      }
    ],
    "responseTime": null,
    "vAccuracy": 0.6027456,
    "verticalRequested": true
  },
  "lpHapType": null,
  "lppMessage": {
    "contentId": "contentId"
  },
  "lppMessageExt": [
    {
      "contentId": "contentId"
    },
    {
      "contentId": "contentId"
    }
  ],
  "maxRespTime": 1,
  "moAssistanceDataTypes": {
    "locationAssistanceType": ""
  },
  "motionEventInfo": {
    "linearDistance": 2027,
    "maximumInterval": 63817,
    "minimumInterval": 13584,
    "occurrenceInfo": null,
    "reportingDuration": 885294,
    "reportingLocationReq": true,
    "samplingInterval": 444
  },
  "ncgi": {
    "nid": "nid",
    "nrCellId": "nrCellId",
    "plmnId": {
      "mcc": "mcc",
      "mnc": "mnc"
    }
  },
  "ncgiOnSecondNode": {
    "nid": "nid",
    "nrCellId": "nrCellId",
    "plmnId": {
      "mcc": "mcc",
      "mnc": "mnc"
    }
  },
  "pei": "pei",
  "periodicEventInfo": {
    "reportingAmount": 5151283,
    "reportingInterval": 4870693
  },
  "priority": null,
  "reliableLocReq": false,
  "reportingAccessTypes": [
    null,
    null
  ],
  "scheduledLocTime": "2000-01-23T04:56:07+00:00",
  "supi": "supi",
  "supportedFeatures": "supportedFeatures",
  "supportedGADShapes": [
    null,
    null
  ],
  "tnapId": {
    "bssId": "bssId",
    "civicAddress": "civicAddress",
    "ssId": "ssId"
  },
  "twapId": {
    "bssId": "bssId",
    "civicAddress": "civicAddress",
    "ssId": "ssId"
  },
  "ueConnectivityStates": {
    "accessType": null,
    "connectivitystate": null
  },
  "ueCountryDetInd": true,
  "ueLcsCap": {
    "ciotOptimisation": false,
    "lppSupport": true
  },
  "ueLocationServiceInd": null,
  "uePositioningCap": "uePositioningCap",
  "ueUnawareInd": true,
  "velocityRequested": null,
  "vgmlcAddress": "vgmlcAddress"
}'
