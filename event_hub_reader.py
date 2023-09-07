from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential
from config import EVENT_HUB_FULLY_QUALIFIED_NAMESPACE, EVENT_HUB_NAME, SAS_POLICY_NAME, SAS_KEY

import asyncio

async def on_event(partition_context, event):
    # Action you want to perform when you receive the log.
    print("Received event from partition: {}".format(partition_context.partition_id))
    print("Event data: {}".format(event.body_as_str()))

async def receive_logs():
    credential = DefaultAzureCredential()

    consumer_client = EventHubConsumerClient.from_connection_string(
        conn_str=f"Endpoint=sb://{EVENT_HUB_FULLY_QUALIFIED_NAMESPACE}/;SharedAccessKeyName={SAS_POLICY_NAME};SharedAccessKey={SAS_KEY}",
        consumer_group="$Default",
        eventhub_name=EVENT_HUB_NAME,
        credential=credential,
    )

    async with consumer_client:
        # We connect to Event Hub and receive logs.
        await consumer_client.receive(
            on_event=on_event,
            starting_position="-1", # "-1" means the start from the end of the partition.
        )

if __name__ == "__main__":
    asyncio.run(receive_logs())
