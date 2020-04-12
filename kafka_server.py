import producer_server


def run_kafka_server():
    # TODO get the json file path
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="com.udacity.sfpolice.service",
        bootstrap_servers="localhost:9095",
        client_id="com.udacity.sfpolice.broker"
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
