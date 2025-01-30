# OR
from .fivem import FiveM
from .minecraft import Minecraft
from .protocol import Protocol
from .samp import Samp
from .source import Source
from .teamspeak3 import Teamspeak3

protocols = {str(protocol.name): protocol for protocol in Protocol.__subclasses__()}
