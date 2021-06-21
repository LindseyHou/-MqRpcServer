import pika
from pika.adapters.blocking_connection import BlockingChannel
from uvicorn.config import logger


def get_connection() -> pika.BlockingConnection:
    logger.debug("Starting RabbitMQ connection.")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    return connection


mq: pika.BlockingConnection = get_connection()


def get_channel(q: str) -> BlockingChannel:
    mq = get_connection()
    channel = mq.channel()
    channel.queue_declare(queue=q)
    logger.debug(q)
    return channel


def send_mq(groupName: str, methodName: str, body: str) -> None:
    get_channel("SendMessage").basic_publish(
        exchange="", routing_key="SendMessage", body=f"{groupName}&{methodName}&{body}"
    )
