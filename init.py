# initial dataset

N = 6
TAU_T1 = 0.2 # время бега тормозной волны до первого экипажа
TAU_TN = TAU_T1 + 0.4 * N # время бега тормозной волны до N-ного экипажа
Fbrk1, FbrkN = 13.8, 13.8 # максимальные силы нажатия на колодки в первом и последнем срезе

initial_dataset = {
    'N0': N,        # количество экипажей (вагонов)
    'M0': [         # массы экипажей, т? (TODO)
        18.8,
        8.6,
        8.6,
        8.6,
        8.6,
        18.8,
    ],
    'LB0': [        # длины экипажей, м
        28,
        14,
        14,
        14,
        14,
        28,
    ],

    'K': [          # жёсткости соединений при нагружении, кн/м? (TODO)
        2600.,
    ],
    'KK': [         # продольные жёсткости кузова экипажа, н/км? (TODO)
        8500.,
    ],
    'Q': [          # деформации, м
        0.065,
    ],
    'BETA': [       # коэф. вязкого сопротивления деформированию
        30.0,       # конструкции кузова, н*с/м
    ],
    'HETA': [       # 1 минус коэф. поглощения энергии
        1. - 0.95,  # фрикционным поглощающим аппаратом
    ],
    'D': [          # наибольший зазор в соединении
        0.065,
    ],
    'DM': [         # абс. деформации соединений,
        0.077,      # при которых поглощающие аппараты закрываются
    ],              # (исчерпывают свой ход)

    'VOT': 1.5,      # скорость, при которой начинается отпуск тормозов
    'C1': 0.055,
    'C2': 20.0,
    'C3': 5.0,
    'C4': 41.7,
    'C5': 20.85,

    'CK': [4, ],    # количество колодок на каждом экипаже

    'LP1': 0,       # 0 - профиль пути без изломов

    'NTAU': 2,      # число сечений в поезде для задания
                    # параметров тормозных сил
    'ITAU': [1, N], # номера экипажей, где находятся вышеупомянутые сечения
    'YTAU': [
        [
            TAU_T1, # время распространения тормозной волны до первого сечения
            1.0, 9.0, 990., 991., 992., 993., # длительности нарастания сил нажатия на колодку
            TAU_T1, # время распространения отпускной волны до первого сечения
            15.0, 994., 995., 996., # длительности убывания сил нажатия на колодку
            Fbrk1*0.7, Fbrk1, Fbrk1, Fbrk1, Fbrk1, # силы нажатия до отпуска
            Fbrk1, 0.0, 0.0, 0.0, # силы нажатия после отпуска
        ],
        [
            TAU_TN, # время распространения тормозной волны до второго сечения
            1.0, 9.0, 990., 991., 992., 993., # длительности нарастания сил нажатия на колодку
            TAU_TN, # время распространения отпускной волны до второго сечения
            15.0, 994., 995., 996., # длительности убывания сил нажатия на колодку
            FbrkN*0.7, FbrkN, FbrkN, FbrkN, FbrkN, # силы нажатия до отпуска
            FbrkN, 0.0, 0.0, 0.0, # силы нажатия после отпуска
        ],
    ],

    'V': [11.5, ],    # скорости движения экипажей

    'W0': 0.6,
    'A0': 0.5,
    'W01': 0.8,
    'A11': 0.07,
    'A22': 0.013,
    'W01': 0.8,

    'H': 0.005, # шаг интегрирования
    'PVH': 0, # постоянный шаг интегрирования

    'HP': 1.6,
    'HPM': 80.0,
    'HPSM': 1.6,

    'NS1': 2,
    'NS2': 4,
    'NS3': 5,
    'NF1': 1,
    'NF2': 6,
    'NFT1': 1,
    'NFT2': 6,
    'NFP1': 1,
    'NFP2': 6,
    'NVOZ': 1,
}
