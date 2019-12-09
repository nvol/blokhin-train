# initial dataset

initial_dataset = {
    'N0': 6,        # количество экипажей (вагонов)
    'M0': [         # массы экипажей, кг
        59300.,
    ],
    'LB0': [        # длины экипажей, м
        14.52,
    ],

    'K': [          # жёсткости соединений при нагружении, н/м
        12000000.,
    ],
    'KK': [         # продольные жёсткости кузова экипажа, н/м
        9000000.,
    ],
    'Q': [          # деформации, м
        0.012,
    ],
    'BETA': [       # коэф. вязкого сопротивления деформированию
        0.01,       # конструкции кузова, н*с/м
    ],
    'HETA': [       # 1 минус коэф. поглощения энергии
        1. - 0.95,  # фрикционным поглощающим аппаратом
    ],
    'D': [          # наибольший зазор в соединении
        0.10,
    ],
    'DM': [         # абс. деформации соединений,
        0.05,       # при которых поглощающие аппараты закрываются
    ],              # (исчерпывают свой ход)

    'VOT': 5.,      # скорость, при которой начинается отпуск тормозов
    'C1': 0.33,
    'C2': 0.0,
    'C3': 0.0,
    'C4': 0.0,
    'C5': 0.0,

    'CK': [4, ],    # количество колодок на каждом экипаже

    'LP1': 0,       # профиль пути без изломов
}
