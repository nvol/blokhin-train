import fortran
import const
from init import initial_dataset
from classes import Arr
from copy import deepcopy
# import matplotlib.pyplot as plt


'''
[__6____] - [__5___] - [__4___] - [__3___] - [__2___] - [__1___],
'''


class Train:
    N = 1   # n - число экипажей или групп (для укороченной системы)
    N0 = 1  # число экипажей всего
    NC1 = 1 # число экипажей в группе (величина постоянная!)

    X = Arr()   # координаты экипажей
    V = Arr()   # скорости экипажей

    LB0 = Arr() # длины экипажей
    LB = Arr()  # длины групп

    M0 = Arr()  # массы экипажей
    M = Arr()   # массы групп

    A1 = Arr() # t, v[1], ..., v[n], q[1], ..., q[n] -- всего 2n+1 элементов
    A2 = Arr() # 1, v'[1], ..., v'[n], q'[1], ..., q'[n] -- всего 2n+1 элементов
    A3 = Arr()
    A4 = Arr()
    A5 = Arr()
    A6 = Arr()
    A7 = Arr()

    Q = Arr()   # деформация i-го межвагонного соединения
                # (или соединения между группами экипажей),
                # в начальный момент 
    S = Arr()

    LP1 = 0

    FB = Arr()
    FP = Arr()
    F = Arr()
    F1 = Arr()
    FT = Arr()
    W = Arr()
    W1 = Arr()
    MPT = Arr()

    H = 0.001
    H1 = None
    NU = 1
    PVH = 0 # интегрирование с постоянным шагом

    MU = 1
    M2 = 1
    M21 = 0
    M1 = Arr()
    S1 = Arr()
    E = 0.0001

    T = 0.0     # шкала времени
    TP = 0.0    # 

    # конечные условия
    TK = 2.0    # конечное время (максимальное)
    VK = 0.001  # конечная скорость (минимальная)
    XK = 1000.0 # конечная координата (максимальная)

    VGR = 0.0013
    HGR = 0.0

    VOT = 0.0 # скорость первого вагона, при которой начинается отпуск

    IA = Arr()
    IA1 = Arr()
    IA11 = Arr()
    AH = Arr()
    AP = Arr()

    K = Arr()
    D = Arr()
    BETA = Arr()
    HETA = Arr()
    KK = Arr()
    SM = Arr()
    DM = Arr()

    IM = 1
    P0 = 0
    PR = 0
    PR1 = 0
    PRT = 0
    PST = 0
    PSR = 0
    PT = 0
    X1 = Arr()
    VS = 0

    C1 = 0.0
    C2 = 0.0
    C3 = 0.0
    C4 = 0.0
    C5 = 0.0
    CK = Arr()
    NTAU = 0
    ITAU = Arr()
    YTAU = Arr()

    TAU = Arr()
    TAU1 = Arr()
    TAU2 = Arr()
    TAU3 = Arr()
    TAU4 = Arr()
    TAU5 = Arr()
    TAU6 = Arr()
    TAUOT = Arr()
    TAU7 = Arr()
    TAU8 = Arr()
    TAU9 = Arr()
    TAU10 = Arr()
    K01 = Arr()
    K02 = Arr()
    K03 = Arr()
    K04 = Arr()
    K05 = Arr()
    K06 = Arr()
    K07 = Arr()
    K08 = Arr()
    K09 = Arr()

    W0 = 0.0
    A0 = 0.0
    W01 = 0.0
    A11 = 0.0
    A22 = 0.0

    M3 = 0

    P = 0
    PM0 = Arr()
    DI = Arr()
    LP = Arr()
    R = Arr()
    A = Arr()

    IND = 0

    V1M = Arr()
    V10 = Arr()
    SMAX = Arr()
    S1MAX = Arr()
    S10 = Arr()
    S0 = Arr()

    HP = 0.0
    TP = 0.0
    HPM = 0.0
    TPM = 0.0
    HPSM = 0.0
    TPSM = 0.0

    NS1 = 0
    NS2 = 0
    NS3 = 0
    NF1 = 0
    NF2 = 0
    NFT1 = 0
    NFT2 = 0
    NFP1 = 0
    NFP2 = 0
    NVOZ = 0

    SMAX1 = 0.0
    SMAX2 = 0.0

    SO1 = 0.0
    SO2 = 0.0
    NL10 = 0
    NL13 = 0
    NL17 = 0
    NL18 = 0

    @classmethod
    def inp(cls, var_name, prompt, val_type=None, limits=None):
        if not hasattr(cls, var_name):
            if not var_name.startswith('tmp_'):
                raise (AttributeError('class %s has no attribute %s' % (
                    cls.__name__, var_name,
                )))
        # try to get value from initials
        if var_name in initial_dataset:
            setattr(cls, var_name, initial_dataset[var_name])
            print(
                'Присвоено значение:',
                var_name, '=', getattr(cls, var_name),
                '@ (%s)' % prompt,
            )
            return

        entered_value = None
        while True:
            entered_value = input('Введите ' + prompt + ': ')
            try:
                if val_type == 'int':
                    entered_value = int(entered_value)
                else:
                    entered_value = float(entered_value)
                if limits is not None and not (limits[0] <= entered_value <= limits[1]):
                    print(
                        'Введено недопустимое значение, введите число в пределах от %s до %s' %
                        (str(limits[0]), str(limits[1])))
                    continue
                break
            except Exception as e:
                print('Простите, непонятно (%s), давайте ещё раз попробуем.' % str(e))
                continue
        setattr(cls, var_name, entered_value)

    @classmethod
    def PARVAG1(cls):
        cls.inp(
            'N0',
            'число масс в полной системе (N0)',
            'int',
            (1, 1000),
        )

        cls.N = cls.N0 ### не укорачиваем систему! => cls.N = cls.N0, cls.NC1 = 1 ###

        ###
        # cls.inp(
        #     'N',
        #     'число масс в укороченной системе (число групп) (N)',
        #     'int',
        #     (1, cls.N0),
        # )
        # if (cls.N0 % cls.N) != 0:
        #     print('Ошибка: N0 не делится без остатка на N')
        #     exit(0)
        ###

        cls.NC1 = cls.N0 // cls.N

        cls.FORMI('M0', 'массы экипажей')
        cls.M = deepcopy(cls.M0)
        print('cls.M0:', cls.M0)
        print('cls.M:', cls.M)
        cls.FORMI('LB0', 'длины экипажей')
        cls.LB = deepcopy(cls.LB0)
        print('cls.LB0:', cls.LB0)
        print('cls.LB:', cls.LB)

    @classmethod
    def VVONU1(cls):
        cls.FORMI('Q', 'деформации межвагонных соединений')
        ### cls.MINPOR(cls.Q) ###

        cls.FORMI('V', 'скорости движения экипажей')

        I = 2 # label 10
        for J in fortran.DO(1, cls.N):
            cls.A1.set_elem(I, cls.V(J))
            cls.A2.set_elem(I, 0.0)
            I += 1 # label 11
        
        I = cls.N + 2
        cls.Q.set_elem(1, cls.Q(1) - (cls.LB0(1) - cls.LB(1)) * 0.5)
        for J in fortran.DO(1, cls.N):
            cls.A1.set_elem(I, cls.Q(J))
            I += 1 # label 12
        
        print('Начальные условия:')
        print('V:', cls.V)
        print('Q:', cls.Q)

    @classmethod
    def SPRAV1(cls):
        # print('==== SPRAV1 ====', cls.T)
        cls.T = cls.A1(1)

        for I in fortran.DO(1, cls.N):
            cls.V.set_elem(I, cls.A1(I+1))

        for I in fortran.DO(1, cls.N):
            L = I + cls.N + 1
            cls.Q.set_elem(I, cls.A1(L))

        for I in fortran.DO(2, cls.N):
            L = I + cls.N + 1
            cls.A2.set_elem(L, cls.V(I-1)- cls.V(I))
        cls.A2.set_elem(cls.N+2, 0.0 - cls.V(1))

        cls.APPARAT1() # SILA
        cls.FVOZM1()

        N1 = cls.N - 1
        for I in fortran.DO(1, N1):
            cls.A2.set_elem(I+1, (cls.S(I) - cls.S(I+1) + cls.FB(I))/cls.M(I))
        cls.A2.set_elem(cls.N+1, (cls.S(cls.N) + cls.FB(cls.N))/cls.M(cls.N))

    @classmethod
    def RKUT2(cls):
        for I in fortran.DO(1, cls.NU):
            cls.A4.set_elem(I, cls.A2(I))
            cls.A5.set_elem(I, cls.A1(I))
            cls.A1.set_elem(I, cls.A1(I) + cls.A2(I) * cls.H1)
        cls.SPRAV1()
        for I in fortran.DO(1, cls.NU):
            cls.A1.set_elem(I, cls.A5(I) + 2 * cls.H1 * cls.A2(I))

    @classmethod
    def INTEGR(cls):
        for I in fortran.DO(1, cls.NU):
            cls.A6.set_elem(I, cls.A3(I))
            cls.A3.set_elem(I, cls.A1(I))
            cls.A1.set_elem(I, cls.A3(I) + (3.0 * cls.A2(I) - cls.A4(I)) * cls.H1)
            cls.A5.set_elem(I, cls.A1(I))
            cls.A7.set_elem(I, cls.A4(I))
            cls.A4.set_elem(I, cls.A2(I))
            cls.SPRAV1()
        for I in fortran.DO(1, cls.NU):
            cls.A1.set_elem(I, cls.A3(I) + (cls.A4(I) + cls.A2(I)) * cls.H1)
        if cls.PVH >= 1:
            ALFA = 0.0
            for I in fortran.DO(cls.NP, cls.NP1):
                Y1 = abs((cls.A5(I) - cls.A1(I)) / 6.0)
                if ALFA < Y1:
                    ALFA = Y1
            if ALFA > cls.HGR:
                if ALFA > cls.VGR:
                    cls.H1 = 0.5 * cls.H
                    for I in fortran.DO(1, cls.NU):
                        cls.A1.set_elem(I, cls.A3(I))
                        cls.A2.set_elem(I, cls.A4(I))
                    cls.RKUT2()
            else: # ALFA <= cls.HGR
                cls.H1 *= 2.0
                cls.SPRAV1()
                for I in fortran.DO(1, cls.NU):
                    cls.A3.set_elem(I, cls.A6(I))
                    cls.A4.set_elem(I, cls.A7(I))
                return
            cls.SPRAV1()

    @classmethod
    def PARINT(cls):
        cls.inp('H', 'шаг интегрирования', 'float', (1e-9, 1.0))
        cls.H *= cls.NC1
        cls.inp(
            'PVH',
            '1 для интегрирования с переменным шагом, 0 - с постоянным',
            'int',
            (0, 1),
        )
        if cls.PVH >= 1:
            cls.NP = cls.N + 2
            cls.NP1 = 2*cls.N + 1

            cls.inp(
                'VGR',
                'верхняя граница допускаемой погрешности',
                'float',
                (1e-9, 1.0),
            )
            cls.inp(
                'HGR',
                'нижняя граница допускаемой погрешности',
                'float',
                (0.0, cls.VGR),
            )
            cls.VGR *= cls.NC1
            cls.HGR *= cls.NC1
            print('Интегрирование с переменным шагом')
            print('Допускаемая погрешность: ' + \
                'верхняя граница = %s, нижняя граница = %s' %
                (str(cls.VGR), str(cls.HGR)))
        else:
            print('Интегрирование с постоянным шагом %s' % str(cls.H))
        
        cls.H1 = 0.5 * cls.H
        cls.NU = 2 * cls.N + 1
        cls.MU = cls.M2 + 1
        for I in fortran.DO(2, cls.N):
            if cls.IA1(I) != 0.0:
                cls.NU += cls.MU
        if cls.M21 != 0:
            for I in fortran.DO(1, cls.N):
                if cls.M1 > cls.E:
                    cls.NU += 2
                    if cls.IA11(I) > cls.E:
                        cls.NU += 2
        cls.A1.set_elem(1, 0.0)
        cls.A2.set_elem(1, 1.0)
        for I in fortran.DO(1, cls.NU):
            cls.A3.set_elem(I, 0.0)
            cls.A4.set_elem(I, 0.0)

    @classmethod
    def FORMI(cls, arr_name, prompt=None):
        if prompt is None:
            prompt = arr_name
        if not hasattr(cls, arr_name):
            if not arr_name.startswith('tmp_'):
                raise(AttributeError('class %s has no attribute %s' % (
                    cls.__name__, arr_name,
                )))
        # try to get list object from initials
        if arr_name in initial_dataset:
            lst = initial_dataset[arr_name]
            if type(lst) is not list:
                raise(ValueError('initial value %s must be the list object' % (
                    arr_name,
                )))
            elif len(lst) < cls.N0:
                print(
                    'Предупреждение: ' + \
                    'во входном массиве %s не хватает данных, ' % (
                    arr_name,
                    ) + 'данные будут дополнены по последнему значению в массиве!')
                while len(lst) < cls.N0:
                    lst.append(lst[-1])
            elif len(lst) > cls.N0:
                print(
                    'Предупреждение: ' + \
                    'во входном массиве %s слишком много данных, ' % (
                    arr_name,
                    ) + 'массив будет укорочен с конца!')
                lst = lst[:cls.N0]

            setattr(cls, arr_name, Arr(lst=lst))
            print(
                'Присвоено значение:',
                arr_name, '=', getattr(cls, arr_name),
                '@ (%s)' % prompt,
            )
            return

        NUP, TABL = Arr(), Arr()
        rest = cls.N0
        I = 0
        while True:
            I += 1
            cls.inp(
                'tmp_NUP',
                'размер %d-й группы экипажей ' % (I, ) + \
                    'для параметра `%s` (0 - весь остаток)' % (prompt, ),
                'int',
                (0, rest),
            )
            if cls.tmp_NUP == 0:
                cls.tmp_NUP = rest
            NUP.set_elem(I, cls.tmp_NUP)
            rest -= NUP(I)
            if rest == 0:
                break
        IK = int(sum([i for i in NUP]))
        NK = len(NUP) # количество групп экипажей
        assert(IK == cls.N0)
        for I in fortran.DO(1, NK):
            cls.inp(
                'tmp_TABL',
                'значение параметра `%s` ' % (prompt, ) + \
                'для %d-й группы из %d экипажей' % (I, NUP(I)),
            )
            TABL.set_elem(I, cls.tmp_TABL)

        ret = list()
        for ix, n in NUP.enumerate():
            ret += [TABL(ix) for _ in range(n)]
        arr = Arr(lst=ret)
        print('%s:' % arr_name, arr)
        setattr(cls, arr_name, arr)

    # @classmethod
    # def MINPOR(cls, TBL_IN):
    #     # использует cls.NC1 (число экипажей в группе)
    #     # и cls.N (число групп) для разбиения на группы
    #     # (суммирования параметров в группе)
    #     TBL_OUT = Arr()
    #     N1 = 1
    #     N2 = cls.NC1
    #     for IK in fortran.DO(1, cls.N):
    #         Y1 = 0
    #         for I in fortran.DO(N1, N2):
    #             Y1 += TBL_IN(I) # label 51
    #         TBL_OUT.set_elem(IK, Y1)
    #         N1 += cls.NC1
    #         N2 += cls.NC1 # label 50
    #     return TBL_OUT
    
    @classmethod
    def APPARAT1(cls):
        for I in fortran.DO(2, cls.N):
            L = I + cls.N + 1
            X = None
            if cls.Q(I) < 0:
                X = cls.Q(I)
            else:
                X = cls.Q(I) - cls.D(I)
            X1 = abs(X)
            if cls.Q(I) * X <= 0:
                cls.S.set_elem(I, 0.0)
                # continue
            else:
                if X1 - cls.DM(I) < 0:
                    if cls.Q(I) * cls.A2(L) >= 0:
                        Y1 = cls.K(I) * X
                        Y2 = X * cls.KK(I) + cls.AH(I) + cls.A2(L) * cls.BETA(I)
                        if abs(Y1) < abs(Y2):
                            cls.S.set_elem(I, Y1)
                            cls.AP.set_elem(I, Y1 - cls.KK(I) * X)
                        else:
                            cls.S.set_elem(I, Y2)
                            cls.AP.set_elem(I, cls.AH(I))
                    else:
                        Y3 = cls.K(I) * X
                        Y1 = Y3 * cls.HETA(I)
                        Y2 = cls.KK(I) * X + cls.AP(I) + cls.A2(L) * cls.BETA(I)
                        if Y1 * Y2 > 0:
                            if abs(Y1) <= abs(Y2):
                                if abs(Y2) <= abs(Y3):
                                    cls.S.set_elem(I, Y2)
                                    cls.AH.set_elem(I, cls.AP(I))
                                else:
                                    cls.S.set_elem(I, Y3)
                                    cls.AP.set_elem(I, Y3 - cls.KK(I) * X)
                            else: # label 13
                                cls.S.set_elem(I, Y1)
                                cls.AH.set_elem(I, Y1 - cls.KK(I) * X)
                        else: # label 13 again
                            cls.S.set_elem(I, Y1)
                            cls.AH.set_elem(I, Y1 - cls.KK(I) * X)
                else:
                    s_new = None
                    if cls.Q(I) >= 0:
                        s_new = (X1 - cls.DM(I)) * cls.KK(I) + cls.SM(I) + \
                                cls.A2(L) * cls.BETA(I)
                    else:
                        s_new = -(X1 - cls.DM(I)) * cls.KK(I) - cls.SM(I) + \
                                cls.A2(L) * cls.BETA(I)
                    cls.S.set_elem(I, s_new)

    @classmethod
    def PARS(cls):
        # TODO: что опять начинается? чьи жёсткости?
        #       что за параметры непонятные?
        cls.FORMI('K', 'жёсткости соединений при нагружении')
        cls.FORMI('D', 'зазоры в межвагонных соединениях')
        cls.FORMI(
            'BETA',
            'коэф. вязкого сопротивления деформированию конструкции кузова (BETA)',
        )
        cls.FORMI(
            'HETA',
            'коэф. поглощения энергии фрикционным поглощающим аппаратом (HETA)',
        )
        cls.FORMI(
            'KK',
            'продольные жёсткости кузова экипажа',
        )
        # cls.FORMI(
        #     'SM',
        #     'параметры SM',
        # ) # TODO: зачем? если можно получить из K и DM

        cls.FORMI(
            'DM',
            'абс. деформации соединений, при которых поглощающие аппараты закрываются',
        )
        
        # TODO: допустима ли данная самодеятельность? уточнить
        for I in fortran.DO(1, cls.N0):
            cls.SM.set_elem(I, cls.K(I) * cls.DM(I))

        if cls.NC1 != 1:
            for I in fortran.DO(1, cls.N0):
                pass ### ... = MINPOR() ###

        for I in fortran.DO(1, 100): # TODO: why hardcode?
            cls.IA.set_elem(I, 0.0)
            cls.AH.set_elem(I, 0.0)
            cls.AP.set_elem(I, 0.0)
            cls.S.set_elem(I, 0.0)

    @classmethod
    def PARG(cls): # AMORTOR4 version
        print('Крепление грузов к вагонам - жёсткое!')
        cls.M21 = 0
        for I in fortran.DO(1, cls.N0):
            cls.S1.set_elem(I, 0.0)
            cls.M1.set_elem(I, 0.0)
        cls.E = 0.0001
        print('Предельное значение V=E=%s' % str(cls.E))

    @classmethod
    def FVOZM1(cls):
        if cls.LP1 > 0:
            # label 5
            # TODO: будем пока использовать PROF3 (профиль без изгибов),
            #       но есть и PROF1
            cls.PROF3()
        # label 8
        cls.VNESH4() # call VNESH
        for I in fortran.DO(1, cls.N0):
            D = -fortran.SIGN(1.0, cls.V(I))
            cls.FT.set_elem(I, cls.FT(I) * D)
            cls.W.set_elem(I, abs(cls.W(I)) * D)
            cls.FB.set_elem(I, cls.FP(I) + cls.F(I) + cls.FT(I) + cls.W(I))
        if cls.NC1 != 1:
            pass ### cls.FB = cls.MINPOR(cls.FB) ###

    @classmethod
    def VNESH4(cls): # VNESH4 version (calls TORM1)
        if cls.PRT + cls.P0 == 0:
            return
        cls.TORM1()
        if cls.M21 != 0:
            for I in fortran.DO(1, cls.N0):
                if cls.M1 < cls.E:
                    continue
                if cls.MPT(I) == 0.0:
                    continue
                cls.F1.set_elem(I, cls.FT(I))
                cls.FT.set_elem(I, 0.0)
        if cls.V(1) > cls.VOT:
            return
        # ASSUMPTION: видимо, здесь начинается отпуск тормозов
        if cls.IM == 2:
            return
        cls.T0 = cls.T
        cls.IM = 2
        cls.P0 = 1
        cls.PRT = 0

    @classmethod
    def PARVF(cls): # for VNESH4 version (calls TORM1)
        cls.PARTOR()
        cls.inp(
            'VOT',
            'скорость первого вагона, ' + \
                'при которой начинается отпуск (VOT)',
            'float',
            (0.001, 250.0),
        )
        cls.PARSP()
        cls.PARPR()
        for I in fortran.DO(1, cls.N0):
            cls.F1.set_elem(I, 0.0)
            cls.F.set_elem(I, 0.0)
            cls.FT.set_elem(I, 0.0)
        cls.IM = 1
        cls.P0 = 0
        cls.PR = 0
        cls.PR1 = 0
        cls.PRT = 0
        cls.PST = 0
        cls.PSR = 0
        cls.PT = 0
        cls.X1.set_elem(1, 0.0)
        cls.VS = 0

    @classmethod
    def TORM1(cls):
        N12 = 1
        N13 = cls.NC1
        for K in fortran.DO(1, cls.N):
            #
            Y = abs(cls.V(K))
            Y1 = (Y + cls.C4) / (Y + cls.C5)
            for I in fortran.DO(N12, N13):
                if cls.P0 > 0:
                    if cls.FT(I) >= 0.0:
                        continue # ~ goto lbl 80
                    jump_to_lbl_32 = False
                    X = cls.T - cls.T0 - cls.TAUOT(I)
                if cls.P0 <= 0 or X < 0.0:
                    # lbl 44: yes! X is local here!
                    X = cls.T - cls.TT - cls.TAU(I)
                    if X <= 0:
                        cls.FT.set_elem(I, 0.0)
                        continue # ~ goto lbl 80

                    # lbl 29
                    X1 = X - cls.TAU1(I)
                    if X1 <= 0:
                        Z = cls.K01(I) / cls.TAU1(I) * X
                        jump_to_lbl_32 = True # goto lbl 32
                    else:
                        X2 = X1 - cls.TAU2(I)
                        if X2 <= 0:
                            Z = (cls.K02(I) - cls.K01(I)) / \
                                cls.TAU2(I) * X1 + \
                                cls.K01(I)
                            jump_to_lbl_32 = True # goto lbl 32
                        else:
                            X3 = X2 - cls.TAU3(I)
                            if X3 <= 0:
                                Z = (cls.K03(I) - cls.K02(I)) / \
                                    cls.TAU3(I) * X2 + \
                                    cls.K02(I)
                                jump_to_lbl_32 = True # goto lbl 32
                            else:
                                X4 = X3 - cls.TAU4(I)
                                if X4 <= 0:
                                    Z = (cls.K04(I) - cls.K03(I)) / \
                                        cls.TAU4(I) * X3 + \
                                        cls.K03(I)
                                    jump_to_lbl_32 = True # goto lbl 32
                                else:
                                    X5 = X4 - cls.TAU5(I)
                                    if X5 <= 0:
                                        Z = (cls.K05(I) - cls.K04(I)) / \
                                            cls.TAU5(I) * X4 + \
                                            cls.K04(I)
                                        jump_to_lbl_32 = True # goto lbl 32
                                    else:
                                        X6 = X5 - cls.TAU6(I)
                                        if X5 <= 0:
                                            Z = (cls.K06(I) - cls.K05(I)) / \
                                                cls.TAU6(I) * X5 + \
                                                cls.K05(I)
                                            jump_to_lbl_32 = True # goto lbl 32
                                        else:
                                            Z = cls.K06(I)
                                            jump_to_lbl_32 = True # goto lbl 32

                    if not jump_to_lbl_32:
                        X1 = X - cls.TAU7(I)
                        if X1 <= 0:
                            Z = cls.K06(I) - ((cls.K06(I) - cls.K07(I)) / \
                                cls.TAU7(I) * X)
                            # goto lbl 32
                        else:
                            X2 = X1 - cls.TAU8(I)
                            if X2 <= 0:
                                Z = cls.K07(I) - ((cls.K07(I) - cls.K08(I)) / \
                                    cls.TAU8(I) * X1)
                                # goto lbl 32
                            else:
                                X3 = X2 - cls.TAU9(I)
                                if X3 <= 0:
                                    Z = cls.K08(I) - ((cls.K08(I) - cls.K09(I)) / \
                                        cls.TAU9(I) * X2)
                                    # goto lbl 32
                                else:
                                    X4 = X3 - cls.TAU10(I)
                                    if X4 <= 0:
                                        Z = cls.K09(I) - \
                                            ((cls.K09(I) / cls.TAU10(I)) * X3)
                                        # goto lbl 32
                                    else:
                                        cls.FT.set_elem(I, 0.0) # lbl 34
                                        continue # goto lbl 80

                    # lbl 32
                    cls.FT.set_elem(
                        I,
                        -cls.C1 * cls.CK * Z * (Z + cls.C2) / (Z + cls.C3) * Y1,
                    )

            # after for I
            N12 += cls.NC1
            N13 += cls.NC1 # lbl 90

        if True not in (cls.FT(I) < 0.0 \
          for I in fortran.DO(1, cls.N0)):
            cls.P0 = 0

        # lbl 692
        if cls.M21 == 0:
            return
        
        for I in fortran.DO(1, cls.N0):
            if cls.M1(I) < cls.E or cls.MPT(I) < cls.E:
                continue
            cls.F1.set_elem(I, cls.FT(I))
            cls.FT.set_elem(I, 0)

    @classmethod
    def PARTOR(cls):
        TAUOB = Arr()
        cls.inp('C1', 'коэффициент C1 в тормозной формуле',
            'float', (1e-9, 1e+9))
        cls.inp('C2', 'коэффициент C2 в тормозной формуле',
            'float', (1e-9, 1e+9))
        cls.inp('C3', 'коэффициент C3 в тормозной формуле',
            'float', (1e-9, 1e+9))
        cls.inp('C4', 'коэффициент C4 в тормозной формуле',
            'float', (1e-9, 1e+9))
        cls.inp('C5', 'коэффициент C5 в тормозной формуле',
            'float', (1e-9, 1e+9))
        cls.FORMI('CK', 'число колодок на каждом экипаже')
        cls.inp(
            'NTAU',
            'число сечений в поезде ' + \
                'для задания параметров тормозных сил NTAU',
            'int',
            (0,1000),
        )
        for I in fortran.DO(1, cls.NTAU):
            cls.inp(
                'tmp_ITAU',
                'номер соответствующего сечения (#%s)' % str(I),
                'int',
            )
            cls.ITAU.set_elem(I, cls.tmp_ITAU)
        for I in fortran.DO(1, cls.NTAU):
            for J in fortran.DO(1, cls.ITAU(I)):
                cls.inp(
                    'tmp_YTAU',
                    'значение параметра в узле #%s,%s YTAU' % (I, J),
                )
                cls.YTAU.set_elem((I, J), cls.tmp_YTAU)
        if cls.NTAU > 0: # TODO: самодеятельность пошла...
            NTAU1 = cls.NTAU - 1
            I = 0
            J = 0
            while True: # lbl 705
                J += 1
                while True: # lbl 701
                    I += 1
                    J1 = cls.ITAU(I)
                    J2 = int(cls.ITAU(I+1)) # TODO: maybe 0.0
                    # print('I:', I, 'J1:', J1, 'J2:', J2)
                    # print('cls.ITAU:', cls.ITAU)
                    for K1 in fortran.DO(J1, J2):
                        tmp = ( cls.YTAU((I+1, J)) - cls.YTAU((I, J)) ) / (J2 - J1) \
                            * (K1 - J1) + cls.YTAU((I, J))
                        TAUOB.set_elem((K1,J), tmp)
                    if I >= NTAU1: # TODO: NTAU1 cases
                        break
                    # if I < NTAU1:
                    #     continue
                    # else:
                    #     break
                if J >= 21:
                    break
                #---
                I = 0
                continue
        
        for I in fortran.DO(1, cls.N0):
            cls.TAU.set_elem(I, TAUOB((I, 1)))
            cls.TAU1.set_elem(I, TAUOB((I, 2)))
            cls.TAU2.set_elem(I, TAUOB((I, 3)))
            cls.TAU3.set_elem(I, TAUOB((I, 4)))
            cls.TAU4.set_elem(I, TAUOB((I, 5)))
            cls.TAU5.set_elem(I, TAUOB((I, 6)))
            cls.TAU6.set_elem(I, TAUOB((I, 7)))
            cls.TAUOT.set_elem(I, TAUOB((I, 8)))
            cls.TAU7.set_elem(I, TAUOB((I, 9)))
            cls.TAU8.set_elem(I, TAUOB((I, 10)))
            cls.TAU9.set_elem(I, TAUOB((I, 11)))
            cls.TAU10.set_elem(I, TAUOB((I, 12)))
            cls.K01.set_elem(I, TAUOB((I, 13)))
            cls.K02.set_elem(I, TAUOB((I, 14)))
            cls.K03.set_elem(I, TAUOB((I, 15)))
            cls.K04.set_elem(I, TAUOB((I, 16)))
            cls.K05.set_elem(I, TAUOB((I, 17)))
            cls.K06.set_elem(I, TAUOB((I, 18)))
            cls.K07.set_elem(I, TAUOB((I, 19)))
            cls.K08.set_elem(I, TAUOB((I, 20)))
            cls.K09.set_elem(I, TAUOB((I, 21)))
        for I in fortran.DO(1, cls.N0):
            cls.FT.set_elem(I, 0.0)
            cls.TT = 0.0
            cls.T0 = 0.0

    @classmethod
    def SOPR1(cls):
        for I in fortran.DO(1, cls.N0):
            Y1 = cls.V(I)
            Y = abs(Y1)
            cls.W.set_elem(I, 
              (
                cls.W0 / (1.0 + cls.A0 * cls.W0 * Y) +
                cls.W01 +
                cls.A11 * Y +
                cls.A22 * (Y**2)
               ) * 0.001
            )
            cls.W.set_elem(I,
                -cls.W(I) * cls.M0(I)
            )
        
        if cls.M21 == 0:
            return
        
        for I in fortran.DO(1, cls.N0):
            if cls.M21 < cls.E or cls.MPT(I) <= cls.E:
                break
            cls.W1.set_elem(I, cls.W(I))
            cls.W.set_elem(I, 0)
        
        return

    @classmethod
    def PARSP(cls):
        cls.inp('W0', 'параметр сил сопротивления W0',
            'float', (1e-9, 1e+9))
        cls.inp('A0', 'параметр сил сопротивления A0',
            'float', (1e-9, 1e+9))
        cls.inp('W01', 'параметр сил сопротивления W01',
            'float', (1e-9, 1e+9))
        cls.inp('A11', 'параметр сил сопротивления A11',
            'float', (1e-9, 1e+9))
        cls.inp('A22', 'параметр сил сопротивления A22',
            'float', (1e-9, 1e+9))
        if abs(cls.W0) < 0.00001:
            cls.M3 = 0

            cls.FORMI('W') # TODO: что это такое?
            for I in fortran.DO(1, cls.N0):
                cls.W.set_elem(I, -cls.W(I))
            print(
                'Силы основного сопротивления движению постоянны W(I)=CONST:',
                cls.W,
            )

            # TODO: в else дублирующийся код!!!
            if cls.M21 == 0:
                return
            
            cls.FORMI('MPT') # TODO: что за чепуха?

            for I in fortran.DO(1, cls.N0):
                cls.W1.set_elem(I, 0.0)

            for I in fortran.DO(1, cls.N):
                if cls.M1(I) < cls.E or cls.MPT(I) <= cls.E:
                    continue
                cls.W1.set_elem(I, cls.W(I))
                cls.W.set_elem(I, 0)
            
        else:
            # label 4
            print('Силы основного сопротивления движению зависят от скорости')
            print('W0:', cls.W0)
            print('A0:', cls.A0)
            print('W01:', cls.W01)
            print('A11:', cls.A11)
            print('A22:', cls.A22)
            cls.M3 = 1

            # TODO: дублирующийся код!!! (такой же в if)
            if cls.M21 == 0:
                return
            
            cls.FORMI('MPT') # TODO: объясните-ка!

            for I in fortran.DO(1, cls.N0):
                cls.W1.set_elem(I, 0.0)

        return

    @classmethod
    def PROF3(cls):
        pass

    @classmethod
    def PROF1(cls):
        cls.X.set_elem(1, -cls.Q(1))
        for I in fortran.DO(2, cls.N):
            cls.X.set_elem(
                I,
                cls.X(I-1) - 0.5*(cls.LB(I-1) + cls.LB(I)),
            )
        N12 = 1
        N13 = cls.NC1 - 1
        K1 = 1
        for J in fortran.DO(1, cls.N):
            cls.XO.set_elem(
                K1,
                cls.X(J) + 0.5 * (cls.LB(J) - cls.LB0(K1)),
            )
            if cls.NC1 <= 1:
                break
            for I in fortran.DO(N12, N13):
                cls.XO.set_elem(
                    I+1,
                    cls.XO(I) - 0.5 * (cls.LB0(I) + cls.LB0(I+1)),
                )
            N12 += cls.NC1
            N13 += cls.NC1
        # label 116
        K1 += cls.NC1
        for I in fortran.DO(1, cls.N0):
            Y = cls.XO(I)
            if Y > 0: # else goto 4
                Y2 = Y
                for L in fortran.DO(cls.IND, cls.P3, 2): # TODO: DO 3 L=IND,P3,2
                    skip_label_4 = False # to make GOTO 11
                    Y1 = Y - cls.A(L)
                    if Y1 >= 0: # else goto 5
                        Y2 = Y - cls.A(L+1)
                        if Y2 > 0:
                            continue
                        J = (L+1)//2 + 1 # TODO: int()? floor? round?
                        cls.FP.set_elem(
                            I,
                            cls.DI(J) * cls.PM0(I),
                        )
                        if I < cls.N0:
                            # goto 11
                            skip_label_4 = True
                            break
                        cls.IND = L
                        pass # TODO: goto 11
                    # label 5:
                    J = (L+1)//2 # TODO: int()?
                    cls.FP.set_elem(
                        I,
                        (cls.DI(J) + Y2/cls.R(J)) * cls.PM0(I),
                    )
                # label 3: CONTINUE

            # label 4:
            if not skip_label_4:
                cls.FP.set_elem(
                    I,
                    cls.DI(1) * cls.PM0(I),
                )
        # label 11: CONTINUE

    @classmethod
    def PARPR(cls):
        cls.inp(
            'LP1',
            'количество изломов профиля (LP1)',
            'int',
            (0, 1000),
        )
        if cls.LP1 <= 0:
            # label 12
            for I in fortran.DO(1, cls.N0):
                cls.FP.set_elem(I, 0)
            print('Движение по площадке')
            return
        
        # label 19
        print('Движение по пути ломаного профиля')
        cls.inp('P', 'P', 'int', (1, 1000))
        for I in fortran.DO(1, 400): # TODO: why hardcode?
            cls.DI.set_elem(I, 0)
            cls.LP.set_elem(I, 0)
            cls.R.set_elem(I, 0)
        P1 = cls.P + 1
        print('Параметры профиля пути:')
        for I in fortran.DO(1, P1):
            cls.inp(
                'tmp_DI',
                'DI(%s)' % str(I),
                'float',
                (1e-9, 1e+9),
            )
            cls.DI.set_elem(I, cls.tmp_DI)
        for I in fortran.DO(1, cls.P):
            cls.inp(
                'tmp_LP',
                'LP(%s)' % str(I),
                'float',
                (1e-9, 1e+9),
            )
            cls.LP.set_elem(I, cls.tmp_LP)
        for I in fortran.DO(1, cls.P):
            cls.inp(
                'tmp_R',
                'R(%s)' % str(I),
                'float',
                (1e-9, 1e+9),
            )
            cls.R.set_elem(I, cls.tmp_R)
        L = 1
        for K in fortran.DO(1, cls.P):
            Y = cls.DI(K+1) - cls.DI(K)
            Y1 = abs(cls.R(K))
            cls.R.set_elem(K, fortran.SIGN(cls.R(K), Y))
            cls.A.set_elem(L, Y1 * abs(Y))
            cls.A.set_elem(L+1, cls.LP(K))
            L += 2
        print('R:', cls.R)
        P2 = cls.P + cls.P
        P3 = P2 - 1
        for L in fortran.DO(2, P2):
            cls.A.set_elem(L, cls.A(L) + cls.A(L-1))
        print('A:', cls.A)
        for I in fortran.DO(1, cls.N0):
            cls.PM0.set_elem(I, cls.M0(I) * const.g)
        cls.IND = 1
        return

    @classmethod
    def PARPRI(cls):
        cls.inp('HP', 'HP', 'float', (1e-9, 1e+9))
        cls.inp('HPM', 'HPM', 'float', (1e-9, 1e+9))
        cls.inp('HPSM', 'HPSM', 'float', (1e-9, 1e+9))
        cls.inp('NS1', 'NS1', 'int', (0, 10000))
        cls.inp('NS2', 'NS2', 'int', (0, 10000))
        cls.inp('NS3', 'NS3', 'int', (0, 10000))
        cls.inp('NF1', 'NF1', 'int', (0, 10000))
        cls.inp('NF2', 'NF2', 'int', (0, 10000))
        cls.inp('NFT1', 'NFT1', 'int', (0, 10000))
        cls.inp('NFT2', 'NFT2', 'int', (0, 10000))
        cls.inp('NFP1', 'NFP1', 'int', (0, 10000))
        cls.inp('NFP2', 'NFP2', 'int', (0, 10000))
        cls.inp('NVOZ', 'NVOZ', 'int', (0, 10000))

        for I in fortran.DO(1, cls.N):
            cls.V1M.set_elem(I, 0.0)
            cls.V10.set_elem(I, 0.0)
            cls.SMAX.set_elem(I, 0.0)
            cls.S1MAX.set_elem(I, 0.0)
            cls.S10.set_elem(I, 0.0)
            cls.S0.set_elem(I, 0.0)
        
        cls.TP = cls.HP
        cls.TPM = cls.HPM
        cls.TPSM = cls.HPSM
        cls.SMAX1 = 0.0
        cls.SO1 = 0.0
        cls.NL10 = 0
        cls.NL13 = 0
        cls.NL17 = 0
        cls.NL18 = 0

    @classmethod
    def MAX(cls):
        Y1 = 0.0
        Y2 = 0.0
        NL15 = 0 # local var
        NL16 = 0 # local var
        for I in fortran.DO(2, cls.N):
            if cls.S(I) >= 0:
                # label 4
                if cls.SMAX(I)<= cls.S(I):
                    # label 8
                    cls.SMAX.set_elem(I, cls.S(I))
                # label 7
                if cls.S(I) > Y1:
                    Y1 = cls.S(I)
                    NL15 = I
            else:
                #label 5
                if cls.S0(I) >= cls.S(I):
                    # label 6
                    cls.S0.set_elem(I, cls.S(I))
                # label 10
                if Y2 > cls.S(I):
                    # label 13
                    Y2 = cls.S(I)
                    NL16 = I
            # label 12: continue
        for I in fortran.DO(1, cls.N):
            if cls.S(I) >= 0:
                # label 44
                if cls.S1MAX(I) <= cls.S1(I):
                    # label 88
                    cls.S1MAX.set_elem(I, cls.S1(I))
            else:
                # label 55
                if cls.S10(I) >= cls.S1(I):
                    # label 66
                    cls.S10.set_elem(I, cls.S1(I))
            # label 112: continue
        for I in fortran.DO(1, cls.N):
            if cls.A2(I+1) >= 0:
                # label 24
                if cls.V1M(I) <= cls.A2(I+1):
                    # label 28
                    cls.V1M.set_elem(I, cls.A2(I+1))
            else:
                # label 25
                if cls.V10(I) >= cls.A2(I+1):
                    # label 26
                    cls.V10.set_elem(I, cls.A2(I+1))
        # label 27: continue
        if cls.SMAX2 < Y1:
            cls.SMAX2 = Y1
            cls.NL17 = NL15
        # label 14
        if cls.SO2 > Y2:
            cls.SO2 = Y2
            cls.NL18 = NL16
        # label 15
        if cls.T <= cls.TPSM:
            return
        
        cls.SMAX1 = cls.SMAX2
        cls.SO1 = cls.SO2
        cls.NL10 = cls.NL17
        cls.NL13 = cls.NL18
        cls.SMAX2 = 0.0
        cls.SO2 = 0.0
        cls.TPSM = cls.T + cls.HPSM

    @classmethod
    def VUMAX(cls):
        print('SMAX:', cls.SMAX)
        print('S0:', cls.S0)
        print('Q:', cls.Q)
        print('S:', cls.S)
        print('V:', cls.V)
        print('V1M:', cls.V1M)
        print('V10:', cls.V10)
        print('S1MAX:', cls.S1MAX)
        print('S10:', cls.S10)

        for I in fortran.DO(1, cls.N):
            cls.V1M.set_elem(I, 0.0)
            cls.V10.set_elem(I, 0.0)
            cls.SMAX.set_elem(I, 0.0)
            cls.S1MAX.set_elem(I, 0.0)
            cls.S10.set_elem(I, 0.0)
            cls.S0.set_elem(I, 0.0)
    
    @classmethod
    def PRINTR1(cls):
        # label 4
        print('T:', cls.T)
        print('X(1):', cls.X(1))
        print('VS:', cls.VS)
        print('V(1):', cls.V(1))
        print('PT:', cls.PT)
        print('PST:', cls.PST)
        print('PR:', cls.PR)
        print('PSR:', cls.PSR)
        print('PRT:', cls.PRT)
        print('P0:', cls.P0)
        print('S:', cls.S(cls.NS1), cls.S(cls.NS2), cls.S(cls.NS3))
        print('F:', cls.F(cls.NF1), cls.S(cls.NF2))
        print('FT:', cls.FT(cls.NFT1), cls.S(cls.NFT2))
        print('FP:', cls.FP(cls.NFP1), cls.S(cls.NFP2))
        print('W:', cls.W(cls.NF1))
        print('FB:', cls.FB(cls.NVOZ))
        print('SMAX1:', cls.SMAX1)
        print('NL10:', cls.NL10)
        print('SO1:', cls.SO1)
        print('NL13:', cls.NL13)

        cls.TP += cls.HP
        if cls.T > cls.TPM:
            # label 6
            cls.VUMAX()
            cls.TPM += cls.HPM
        # label 5

    @classmethod
    def are_limits_reached(cls):
        ret = cls.T >= cls.TK
        ret |= cls.V(1) <= cls.VK
        ret |= abs(cls.X(1)) >= cls.XK
        return ret


if __name__ == '__main__':

    Train.PARVAG1()
    Train.PARS()
    Train.PARG()
    Train.PARVF()
    Train.VVONU1()
    Train.PARINT()

    Train.PARPRI()

    #--------------------

    Train.SPRAV1()
    Train.RKUT2()
    Train.SPRAV1()

    while True:
        Train.INTEGR()
        Train.MAX()
        if Train.T >= Train.TP:
            Train.PRINTR1()
        if Train.are_limits_reached():
            break

    Train.VUMAX()
