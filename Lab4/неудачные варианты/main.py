import pickle

class Message:
    def __init__(self, content):
        self.content = content

    def serialize(self):
        return pickle.dumps(self)

    def deserialize(serialized_message):
        return pickle.loads(serialized_message)
    
mes = Message('hello')
g = mes.serialize()
print(g)

deserialized_message = Message.deserialize(g)
print(deserialized_message.content)