# navigation_data.py
NAVIGATION_DATA = {
    'guka': {  # здание ГУК А
        2: {  # этаж 2
            'coordinates': {
                "SGV_GUKA_2_k_209": (200, 370),
                "SGV_GUKA_2_k_210": (100, 320),
                "SGV_GUKA_2_k_211": (200, 270),
            },
            'connections': [("SGV_GUKA_2_k_209", "SGV_GUKA_2_k_210"),
                          ("SGV_GUKA_2_k_210", "SGV_GUKA_2_k_211")]
        },
        3: {  # этаж 3
            'coordinates': {
                "SGV_GUKA_3_k_309": (120, 180),
                "SGV_GUKA_3_k_310": (170, 230),
            },
            'connections': [("SGV_GUKA_3_k_309", "SGV_GUKA_3_k_310")]
        }
    },
    'gukv': {  # здание ГУК В
        3: {
            'coordinates': {
                "SGV_GUKV_3_k_301": (80, 160),
                "SGV_GUKV_3_k_302": (130, 210),
            },
            'connections': [("SGV_GUKV_3_k_301", "SGV_GUKV_3_k_302")]
        }
    },
    'outside': {  # уличная карта
        0: {
            'coordinates': {
                "S_Streshnevo_i_1": (50, 100),
                "S_Streshnevo_i_2": (200, 150),
            },
            'connections': [("S_Streshnevo_i_1", "S_Streshnevo_i_2")]
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