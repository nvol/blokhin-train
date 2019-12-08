# Расчёт динамики тяжеловесных поездов

### *По одноимённому роману под редакцией д-ра техн. наук проф. Е. П. Блохина "Расчёты и испытания тяжеловесных поездов"*

## Описание функций (фортрановские имена сохранены)

| имя функции | назначение |
| --- | --- |
| PARVAG1 | формирование параметров экипажей |
| VVONU1 | подготовка начальных условий (вагоны с жёстко закреплёнными грузами) |
| SPRAV1 | формирование правых частей дифференциальных уравнений (вагоны с жёстко закреплёнными грузами) |
| RKUT2 | интегрирование системы дифференциальных уравнений на начальных отрезках (реализация метода Рунге-Кутта второго порядка, одношаговый метод) |
| INTEGR, PARINT | интегрирование системы дифференциальных уравнений (реализация двухшагового метода интегрирования на базе формул Адамса-Башфорта и Адамса-Мултона) |
| FORMI | формирование массивов исходных данных |
| MINPOR | формирование параметров "укороченной" системы дифференциальных уравнений (TODO: пока не используется, не рассматриваем укороченную систему) |
| PRINTR, PARPRI | печать промежуточных результатов (TODO: написать) |
| MAX | выбор и печать наибольших сил и ускорений (TODO: написать) |
| SILA->APPARAT1, PARS | формирование параметров междувагонных соединений и вычисление сил в автосцепках |
| SILA1->AMORTOR4, PARG  | силы в соединениях "вагон-груз" не вычисляются, параметры соединений и грузов не вводятся |
| FVOZM1 | организация вычисления и суммирования внешних сил (сопротивления поступательному движению постоянны; движение без остановок) |
| VNESH4, PARVF | формирование параметров внешних сил и некоторых параметров управления движением поезда; организация вычисления внешних сил, вызванных управлением движением (торможение и отпуск тормозов) |
| SOPR1, PARSP | формирование параметров сил сопротивления поступательному движению экипажей; вычисление сил сопротивления (силы сопротивления постоянны либо зависят от скорости) |
| PROF3, PARPR | формирование параметров профиля пути; вычисление возмущений от профиля пути (движение поезда по горизонтальному участку пути) |
| PROF1, PARPR | формирование параметров профиля пути; вычисление возмущений от профиля пути (вагоны с жёстко закреплёнными грузами) |
| TORM1, PARTOR | формирование параметров тормозных сил от пневматического торможения; вычисление тормозных сил (моделируется этап торможения и отпуска тормозов; закон изменения силы нажатия на тормозную колодку во времени аппроксимируется кусочно-линейной функцией) |

## Ссылки (страница в [PDF](doc/blokhin.pdf) (страница в книге))

- PARVAG1 11л(18)
- VVONU1 11п(19)
- SPRAV1 14л(24)
- RKUT2 17л(30)
- INTEGR, PARINT 18(32,33)
- FORMI 19п(35)
- MINPOR 20л(36)
- PRINTR, PARPRI 21л(38)
- MAX, VUMAX 24п(45), 25п(47)
- SILA->APPARAT1, PARS 26п(49), 27л(50)
- SILA1->AMORTOR4, PARG 51л(98)
- FVOZM1 51п(99)
- VNESH4, PARVF 57п(111)
- SOPR1, PARSP 59л(114)
- PROF3, PARPR 63л(122)
- TORM1, PARTOR 68п(133)

## Зависимости

**MAIN**  
&#9567;&#9472;**PARVAG1**  
&#9553;&#9617;&#9617;&#9561;&#9472; FORMI  
&#9567;&#9472;**PARS**  
&#9553;&#9617;&#9617;&#9561;&#9472; FORMI  
&#9567;&#9472;**PARG**  
&#9567;&#9472;**PARVF**  
&#9553;&#9617;&#9617;&#9567;&#9472;PARTOR  
&#9553;&#9617;&#9617;&#9553;&#9617;&#9617;&#9561;&#9472;FORMI  
&#9553;&#9617;&#9617;&#9567;&#9472;PARSP  
&#9553;&#9617;&#9617;&#9553;&#9617;&#9617;&#9561;&#9472;FORMI  
&#9553;&#9617;&#9617;&#9561;&#9472;PARPR  
&#9567;&#9472;**VVONU1**  
&#9553;&#9617;&#9617;&#9561;&#9472;FORMI  
&#9567;&#9472;**PARINT**  
&#9567;&#9472;**PARPRI**  
&#9567;&#9472;**SPRAV1**  
&#9553;&#9617;&#9617;&#9567;&#9472;APPARAT1  
&#9553;&#9617;&#9617;&#9561;&#9472;FVOZM1  
&#9553;&#9617;&#9617;&#9617;&#9617;&#9617;&#9567;&#9472;PROF3  
&#9553;&#9617;&#9617;&#9617;&#9617;&#9617;&#9561;&#9472;VNESH4  
&#9553;&#9617;&#9617;&#9617;&#9617;&#9617;&#9617;&#9617;&#9617;&#9561;&#9472;TORM1    
&#9567;&#9472;**RKUT2**  
&#9553;&#9617;&#9617;&#9561;&#9472;SPRAV1  
&#9553;&#9617;&#9617;&#9617;&#9617;&#9617;&#9561;&#9472;APPARAT1,FVOZM1,PROF3,VNESH4,TORM1  
&#9567;&#9472;**SPRAV1**  
&#9553;&#9617;&#9617;&#9561;&#9472;APPARAT1,FVOZM1,PROF3,VNESH4,TORM1  
&#9567;&#9472;**INTEGR**  
&#9553;&#9617;&#9617;&#9567;&#9472;SPRAV1  
&#9553;&#9617;&#9617;&#9553;&#9617;&#9617;&#9561;&#9472;APPARAT1,FVOZM1,PROF3,VNESH4,TORM1  
&#9553;&#9617;&#9617;&#9561;&#9472;RKUT2  
&#9553;&#9617;&#9617;&#9617;&#9617;&#9617;&#9561;&#9472;SPRAV1,APPARAT1,FVOZM1,...  
&#9567;&#9472;**MAX**  
&#9567;&#9472;**PRINTR**  
&#9553;&#9617;&#9617;&#9561;&#9472;VUMAX  
&#9561;&#9472;**VUMAX**  
