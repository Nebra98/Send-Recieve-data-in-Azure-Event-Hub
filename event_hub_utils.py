from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def send_log_to_event_hub(log_message, fully_qualified_namespace, eventhub_name, sas_policy_name, sas_key):
    producer_client = EventHubProducerClient.from_connection_string(
        conn_str=f"Endpoint=sb://{fully_qualified_namespace}/;SharedAccessKeyName={sas_policy_name};SharedAccessKey={sas_key}",
        eventhub_name=eventhub_name,
    )

    async with producer_client:
        event_data_batch = await producer_client.create_batch()
        event_data_batch.add(EventData(log_message))
        await producer_client.send_batch(event_data_batch)
