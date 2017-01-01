class WebApplicationException(Exception):
    def __init__(self, error_message, description, status_code):
        self._error_message = error_message
        self._description = description
        self._status_code = status_code

    @property
    def code(self):
        return self._status_code

    @property
    def message(self):
        return self._error_message

    @property
    def description(self):
        return self._description

    @property
    def serialize(self):
        return {
            'message': self._error_message,
            'description:': self._description,
            'code': self._status_code
        }
