from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    # TODO we're generating a dummy data
    def generate_data(self):
        with open(self.input_file) as f:
            data_dict = json.load(f)
            for item in data_dict:
                message = self.dict_to_binary(item)
                self.send(self.topic, message)
                time.sleep(1)

    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode("utf-8")


# if __name__ == "__main__":
#     producer = ProducerServer(
#         './police-department-calls-for-service.json', 'com.udacity.police-call-service')
#     producer.generate_data()
