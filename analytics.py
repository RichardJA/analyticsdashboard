from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build  # this is the updated version of apiclient.discovery

import httplib2
import matplotlib.pyplot as plt
import numpy as np
import sys


def get_keys():
    """
    Checks to see whether the information provided about keys is correct
    If it is, it returns all this information
    """
    try:
        analytics_scope = ['https://www.googleapis.com/auth/analytics.readonly']
        apikey = 'secret_google_key.json'
        analytics_view = open('secret_ga_view.txt').read()
    except Exception as exc:
        print('Error downloading files.\n' + str(exc))
        input('Press ENTER key to exit...')
        sys.exit()

    return [analytics_scope, apikey, analytics_view]


def create_service_object(conn):
    """
    Is passed through the connection information to the API
    Returns a service object
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(conn[1], conn[0])
    http = credentials.authorize(httplib2.Http())
    service_object = build('analytics', 'v4', http=http,
                           discoveryServiceUrl='https://analyticsreporting.googleapis.com/$discovery/rest')

    return service_object


class Analytics(object):
    def __init__(self):
        pass
