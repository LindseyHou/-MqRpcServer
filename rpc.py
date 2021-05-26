import asyncio
import logging
from asyncio import run
from typing import Any, Coroutine

import pika
from pika.adapters.blocking_connection import BlockingChannel

from crud import METHODNAME_2_METHOD, getData

# def run(coroutine: Any) -> Any:
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value


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


def is_upper_char(s: str) -> bool:
    for c in s:
        if c < "A" or c > "Z":
            return False
    return True


def is_numbers(s: str) -> bool:
    for c in s:
        if c < "0" or c > "9":
            return False
    return True


def is_valid_id(companyID: str) -> bool:
    if companyID == "":
        return True
    if len(companyID) <= 7:
        return False
    prefix = companyID[0:7]
    leftover = companyID[7:]
    return is_upper_char(prefix) and is_numbers(leftover)


async def on_request(ch: BlockingChannel, method: Any, props: Any, body: bytes) -> None:
    message = body.decode()
    methodName, groupName, *_ = message.split("&")
    logging.info(f" [.] getData({methodName}, {groupName})")
    response: str = ""

    if not is_valid_id(groupName):
        logging.warning("companyID not valid: " + groupName)
        response = "InValidID"
    else:
        try:
            response = await getData(groupName, methodName)
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


async def main() -> Any:
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

    logging.info(" [x] Awaiting RPC requests")
    channel.start_consuming()


if __name__ == "__main__":
    run(main())
