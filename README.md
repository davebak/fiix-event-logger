# Fiix Event Logger

This is a script to log an event in Fiix CMMS. Simply update the `.ini` file 
with your data and run:

```sh
python fiix_event_logger.py
```

## Where to retrieve your Access Keys

Visit [Fiix Developer's Guide](https://fiixlabs.github.io/api-documentation/guide.html#api_keys) 
for information about retrieving your Fiix API keys.

## Editing the INI File

Update the `.ini` configuration file with your API keys, and information about 
the event ie. event ID, asset ID to log against, and a description of the event.

## Warning!

Ensure that you don't commit Fiix API keys to a git repository when updating 
the `.ini` file. 