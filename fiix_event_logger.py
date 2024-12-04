"""
File Name: fiix_event_logger.py
Description: A simple python script to log an event in Fiix CMMS.
Authors: Mike Cooper, David Bak
Date: 2024-12-02
Version: 0.0
"""
import hmac
import requests
import hashlib
import configparser
import argparse
from datetime import datetime, timezone


def get_config_data(config_file):
    # Get the config data from the configuration file
    config = configparser.ConfigParser()
    config.read(config_file)

    tenant_url = config.get('General', 'fiix_tenant')

    app_key = config.get('Auth', 'app_key')
    access_key = config.get('Auth', 'access_key')
    api_secret = config.get('Auth', 'api_secret')

    event_id = config.get('Data', 'event_id')
    asset_id = config.get('Data', 'asset_id')
    description = config.get('Data', 'description')

    return tenant_url, app_key, access_key, api_secret, event_id, asset_id, description


def prepare_msg_header(secret, msg):
    # Create the auth token and header
    signature = hmac.new(
        key=secret.encode(encoding="utf-8"),
        msg=msg.encode(encoding="utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    # Set the reqest header
    headers = {
        "Content-type": "text/plain;charset=utf-8",
        "Authorization": signature
    }
    return headers


def prepare_msg_body(event_id, asset_id, description):
    # Set up the message body
    body = {
        "_maCn": "AddRequest",
        "clientVersion": {
            "major": 2,
            "minor": 8,
            "patch": 1
        },
        "className": "AssetEvent",
        "object": {
            "className": "AssetEvent"
        },
        "fields": "*"
    }

    body["object"]["intAssetEventTypeID"] = str(event_id)
    body["object"]["intAssetID"] = str(asset_id)
    body["object"]["strAdditionalDescription"] = description
    body["object"]["dtmDateSubmitted"] = str(
        int(datetime.now(timezone.utc).timestamp() * 1000)
    )

    return body

if __name__ == '__main__':
    # Parse command line args (default to event_logger.ini)
    parser = argparse.ArgumentParser(
                    prog='fiix_event_logger',
                    description='Log an event against an asset in Fiix CMMS')
    
    parser.add_argument('-c', '--config', 
                        help="the name of the config file",
                        default="event_logger.ini")
    
    # Grab the config filename
    config_file = vars(parser.parse_args())["config"]

    # Get config data
    tenant_url, app_key, access_key,\
          api_secret, event_id, asset_id, description = get_config_data(config_file)

    # Set-up the request url
    request_url = (f"https://{tenant_url}.macmms.com/api/?service=cmms"
                   f"&appKey={app_key}"
                   f"&accessKey={access_key}"
                   "&signatureMethod=HmacSHA256"
                   "&signatureVersion=1")

    # Prepare the request 
    headers = prepare_msg_header(api_secret, request_url.replace("https://", ""))
    body = prepare_msg_body(event_id, asset_id, description)

    # Send the request
    try:
        response = requests.post(request_url, json=body, headers=headers)
        print(f"\nResponse status: {response.status_code}\n")
        print(f"\nData: {response.text}\n")
    except:
        print("An error occured in sending the request.")
