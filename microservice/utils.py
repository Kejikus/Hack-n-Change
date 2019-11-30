from enum import Enum


class Status(Enum):
    Idea = 'IDEA'
    InDev = 'INDEV'
    Testing = 'TEST'
    Deployed = 'DEPLOYED'
    Deprecated = 'DEPRECATED'
    Removed = 'ENDLIFE'