# Fiix Event Logger

This is a script to log an event in Fiix CMMS. 

The recommended way of running this tool is to download the latest executable 
from the releases section and run

```sh
# Run with default config file (event_logger.ini)
C:\FiixFolder> fiix_event_logger.exe

# Run with user defined config file
C:\FiixFolder> fiix_event_logger.exe --config my_config_file.ini
C:\FiixFolder> fiix_event_logger.exe -c my_config_file.ini

# Show help menu
C:\FiixFolder> fiix_event_logger.exe -h
```

## Editing the INI File

Update the `.ini` configuration file with your API keys, and information about 
the event ie. event ID, asset ID to log against, and a description of the event.

## Where to retrieve your Access Keys

Visit [Fiix Developer's Guide](https://fiixlabs.github.io/api-documentation/guide.html#api_keys) 
for information about retrieving your Fiix API keys.

## Warning!

Ensure that you don't commit Fiix API keys to a git repository when updating 
the `.ini` file. 

## Supported Platforms

Unfortunately, the standalone `.exe` for this script is only for Windows x86-64, 
however you can just `git clone` the script and run it providing you have Python
installed on your machine.