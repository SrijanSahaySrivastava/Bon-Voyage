from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Task(_message.Message):
    __slots__ = ("Place", "Food", "Interests", "Health", "Days", "email", "in_date", "out_date")
    PLACE_FIELD_NUMBER: _ClassVar[int]
    FOOD_FIELD_NUMBER: _ClassVar[int]
    INTERESTS_FIELD_NUMBER: _ClassVar[int]
    HEALTH_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IN_DATE_FIELD_NUMBER: _ClassVar[int]
    OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    Place: str
    Food: str
    Interests: str
    Health: str
    Days: int
    email: str
    in_date: str
    out_date: str
    def __init__(self, Place: _Optional[str] = ..., Food: _Optional[str] = ..., Interests: _Optional[str] = ..., Health: _Optional[str] = ..., Days: _Optional[int] = ..., email: _Optional[str] = ..., in_date: _Optional[str] = ..., out_date: _Optional[str] = ...) -> None: ...

class GetTask(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class ChatHistoriesResponse(_message.Message):
    __slots__ = ("chat_histories",)
    CHAT_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    chat_histories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chat_histories: _Optional[_Iterable[str]] = ...) -> None: ...
