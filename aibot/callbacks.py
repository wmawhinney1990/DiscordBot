from enum import Enum

class CallbackManager:
    def __init__(self):
        self.callbacks = {}

    def __contains__(self, callback_name):
        return callback_name in self.callbacks

    def register_callback(self, event_name, callback):
        if event_name not in self.callbacks:
            self.callbacks[event_name] = []
        self.callbacks[event_name].append(callback)

    def unregister_callback(self, event_name, callback):
        if event_name in self.callbacks:
            if callback in self.callbacks[event_name]:
                self.callbacks[event_name].remove(callback)

    def invoke_callbacks(self, event_name, *args, **kwargs):
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                callback(*args, **kwargs)

    async def async_invoke_callbacks(self, event_name, *args, **kwargs):
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                await callback(*args, **kwargs)