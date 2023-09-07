# Send/Recive data in Azure Event Hub using Python

This document provides steps and guidance to successfully implement sending and receiving data to Azure Event Hub.

## Introduction

Azure Event Hubs is a service within the Microsoft Azure platform that enables the creation and management of large streams of events and data in real-time. Azure Event Hubs is commonly used in scenarios involving IoT device monitoring, application metrics tracking, event logging, real-time data analytics, and other applications that require handling large streams of real-time events and data.

###  Prerequisites

Clone the repository to your computer:
```bash
git clone https://github.com/Nebra98/Send-Recieve-data-in-Azure-Event-Hub.git
```

Navigate to the repository you cloned with the command:
```bash
cd repository_name
```
Before you run the command to install the package, create and activate the virtual environment:
```bash
python3 -m venv <name_of_virtualenv>
```
```bash
source <name_of_virtualenv>/bin/activate
```

### Installation and configuration


Installing Python Packages From a Requirements File:
```bash
pip install -r requirements.txt
```

Edit `config.py` with your credentials to connect to Azure Event Hub:

```bash
EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "your_namespace.servicebus.windows.net"
EVENT_HUB_NAME = "your_eventhub_name"
SAS_POLICY_NAME = "RootManageSharedAccessKey"
SAS_KEY = "your_primary_key"
```

Run `main.py` to send logs to Event Hub:
```bash
python main.py
```

Run `event_hub_reader.py` to receive logs from Event Hub:
```bash
python event_hub_reader.py 
```




