# navigation_data.py
NAVIGATION_DATA = {
    'guka': {  # здание ГУК А
        2: {  # этаж 2
            'coordinates': {
                "SGV_GUKA_2_k_209": (200, 370),
                "SGV_GUKA_2_k_210": (100, 320),
                "SGV_GUKA_2_k_211": (200, 270),
            },
        },
        3: {  # этаж 3
            'coordinates': {
                "SGV_GUKA_3_k_309": (120, 180),
                "SGV_GUKA_3_k_310": (170, 230),
            },
        }
    },
    'gukv': {
        3: {
            'coordinates': {
                'S_GV_3_b_1': (4454, 4035),
                'S_GV_3_f_1': (4130, 8800),
                'S_GV_3_l_1': (6934, 4872),
                'S_GV_3_l_2': (4785, 7026),
                'S_GV_3_p_1': (8470, 4872),
                'S_GV_3_p_2': (8470, 4192),
                'S_GV_3_p_3': (4454, 4192),
                'S_GV_3_p_4': (4130, 4192),
                'S_GV_3_p_5': (4130, 8518),
                'S_GV_3_p_6': (4785, 8518),
                'test': (0, 0),
                'test2': (10000, 10000),
                'test3': (5000, 5000)
            }
            }
    },
    'outside': {  # уличная карта
        0: {
            'coordinates': {
                "S_Streshnevo_i_1": (50, 100),
                "S_Streshnevo_i_2": (200, 150),
            }
        }
    }
}

# Собираем все точки в один список для удобства поиска
ALL_POINTS = []

for building, levels in NAVIGATION_DATA.items():
    for level, data in levels.items():
        if 'coordinates' in data:
            for point_name, coords in data['coordinates'].items():
                ALL_POINTS.append({
                    'name': point_name,
                    'building': building,
                    'level': level,
                    'coordinates': coords
                })

# Сортируем точки по имени для удобного отображения
ALL_POINTS.sort(key=lambda x: x['name'])