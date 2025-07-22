from typing import Union
import uuid

def calculate_player_elo(RA, RB, SA) -> int:
    k_factor = 20
    EA = 1 / (1 + 10**((RB - RA) / 400))
    result = RA + k_factor * (SA - EA)

    return int(result)

        
