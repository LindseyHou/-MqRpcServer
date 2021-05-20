from asyncio import run
from crud import METHODNAME_2_METHOD, getData
from pika.adapters.blocking_connection import BlockingChannel
import pika
import logging
from typing import Any

logging.basicConfig(
    handlers=[logging.FileHandler("mq.log"), logging.StreamHandler()],
    format="%(asctime)s %(levelname)-8s: %(filename)s %(funcName)s %(lineno)s %(message)s",
    datefmt="%m-%d %H:%M:%S",
    level=logging.INFO,
)


connection: pika.BlockingConnection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel: BlockingChannel = connection.channel()

channel.queue_declare(queue="rpc_queue")


def on_request(ch: BlockingChannel, method: Any, props: Any, body: bytes) -> None:
    message = body.decode()
    methodName, groupName, *_ = message.split("&")
    logging.info(f" [.] getData({methodName}, {groupName})")
    try:
        response = run(getData(groupName, methodName))
    except ValueError:
        response = "ValueError"
    logging.info(" [>] response = %s" % response)
    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

    logging.info(" [x] Awaiting RPC requests")
    channel.start_consuming()
