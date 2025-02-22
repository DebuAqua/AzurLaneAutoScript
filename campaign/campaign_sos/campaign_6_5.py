from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

from .campaign_base import CampaignBase

MAP = CampaignMap('SOS')
MAP.shape = 'H6'
MAP.camera_data = ['D2', 'D4']
MAP.camera_data_spawn_point = ['D4']
MAP.map_data = """
    ++ ME -- -- -- ME ++ ++
    ME -- ME MB MB -- ME --
    -- ++ ME ME ME ME -- ME
    ME ME __ Me ME __ ME --
    ME Me ME MB ME ME ++ ME
    -- ++ Me SP SP ME ++ --
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50
    50 50 20 10 10 30 50 50
    50 50 20 10 20 30 50 50
    50 50 20 10 20 30 50 50
    50 50 20 10 20 30 50 50
    50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 5},
    {'battle': 1, 'enemy': 2},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'enemy': 1},
    {'battle': 5, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, \
A2, B2, C2, D2, E2, F2, G2, H2, \
A3, B3, C3, D3, E3, F3, G3, H3, \
A4, B4, C4, D4, E4, F4, G4, H4, \
A5, B5, C5, D5, E5, F5, G5, H5, \
A6, B6, C6, D6, E6, F6, G6, H6, \
    = MAP.flatten()


class Config:
    # ===== Start of generated config =====
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = False
    MAP_HAS_AMBUSH = False
    STAR_REQUIRE_1 = 0
    STAR_REQUIRE_2 = 0
    STAR_REQUIRE_3 = 0
    # ===== End of generated config =====

    INTERNAL_LINES_HOUGHLINES_THRESHOLD = 40
    EDGE_LINES_HOUGHLINES_THRESHOLD = 40
    COINCIDENT_POINT_ENCOURAGE_DISTANCE = 1.5


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_enemy(scale=(2, 3), genre=['light', 'carrier', 'enemy', 'main']):
            return True

        return self.battle_default()

    def battle_5(self):
        self.fleet_boss.clear_boss()
