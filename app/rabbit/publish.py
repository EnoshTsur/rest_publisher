import json

from app.rabbit.channel import create_channel
from app.settings.rabbit_config import TOPIC_EXCHANGE, REST_NEW_MEAL_QUEUE, REST_STOCK_AMOUNT_QUEUE, \
    REST_ALL_ROUTING_KEY, REST_ALL_QUEUE, REST_NEW_MEAL_ROUTING_KEY, REST_STOCK_AMOUNT_ROUTING_KEY


def publish_topic(message: dict, routing_key: str):
    with create_channel() as channel:
        # Declare a topic exchange
        channel.exchange_declare(
            exchange=TOPIC_EXCHANGE,  # Exchange name
            exchange_type='topic',  # Type of exchange
            durable=True  # Make the exchange persistent
        )

        channel.queue_declare(queue=REST_NEW_MEAL_QUEUE, durable=True)
        channel.queue_declare(queue=REST_STOCK_AMOUNT_QUEUE, durable=True)
        channel.queue_declare(queue=REST_ALL_QUEUE, durable=True)

        for key, queue in [
            (REST_ALL_ROUTING_KEY, REST_ALL_QUEUE),
            (REST_NEW_MEAL_ROUTING_KEY, REST_NEW_MEAL_QUEUE),
            (REST_STOCK_AMOUNT_ROUTING_KEY, REST_STOCK_AMOUNT_QUEUE)
        ]:
            channel.queue_bind(
                queue=queue,
                exchange=TOPIC_EXCHANGE,
                routing_key=key
            )

        # Publish the message to the topic exchange
        channel.basic_publish(
            exchange=TOPIC_EXCHANGE,  # Publish to the topic exchange
            routing_key=routing_key,  # Routing key determines the target queue(s)
            body=json.dumps({
                **message,
                '_id': str(message['_id'])}
            ).encode()  # Encode the message
        )

        # Log confirmation
        print(f" [x] Sent: '{message}' with routing key '{routing_key}'")