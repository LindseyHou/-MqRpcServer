from typing import Any

import pika
from pika.adapters.blocking_connection import BlockingChannel

from crud import get_data

connection: pika.BlockingConnection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel: BlockingChannel = connection.channel()

channel.queue_declare(queue="rpc_queue")


def on_request(ch: BlockingChannel, method: Any, props: Any, methodName: str) -> None:
    print(" [.] get_data(%s)" % methodName)
    response = get_data(methodName)

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
