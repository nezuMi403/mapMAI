# navigation_data.py
NAVIGATION_DATA = {
    'guka': {  # здание ГУК А
        2: {  # этаж 2
            'coordinates': {
                1: (200, 370),
                2: (100, 320),
                3: (200, 270),
            },
            'connections': [(1, 2), (2, 3)]
        },
        3: {  # этаж 3
            'coordinates': {
                4: (120, 180),
                5: (170, 230),
            },
            'connections': [(4, 5)]
        }
    },
    'gukv': {  # здание ГУК В
        3: {
            'coordinates': {
                6: (80, 160),
                7: (130, 210),
            },
            'connections': [(6, 7)]
        }
    },
    'outside': {  # уличная карта
        0: {
            'coordinates': {
                8: (50, 100),
                9: (200, 150),
            },
            'connections': [(8, 9)]
        }
    }
}