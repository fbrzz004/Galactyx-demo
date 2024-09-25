from src.states.home import Home
from src.states.origin_cinematic import OriginCinematic
from src.states.map_levels import MapLevels
from src.states.trip import Trip
from src.states.jump_cinematic import JumpCinematic
from src.states.arrival_cinematic import ArrivalCinematic
from src.states.end import End

navigation = {
    'home': Home,
    'origin_cinematic': OriginCinematic,
    'map_levels': MapLevels,
    'trip': Trip,
    'jump_cinematic': JumpCinematic,
    'arrival_cinematic': ArrivalCinematic,
    'end': End
}
