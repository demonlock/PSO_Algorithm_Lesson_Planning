from __future__ import division
import random
import copy
from datetime import datetime


global_periyod = 8
global_gun = 5
global_derslik = 5
max_bound1 = 7
max_bound2 = 24

ogretmenler = [[1, 11, "Edebiyat Öğretmeni 1"],             # 0
               [2, 12, "Edebiyat Öğretmeni 2"],             # 1
               [3, 113, "Müzik Öğretmeni"],                 # 2
               [4, 124, "Resim Öğretmeni"],                 # 3
               [5, 135, "Beden Öğretmeni"],                 # 4
               [6, 146, "Yabancı Dil Öğretmeni 1"],         # 5
               [7, 147, "Yabancı Dil Öğretmeni 2"],         # 6
               [8, 88, "Matematik Öğretmeni 1"],            # 7
               [9, 89, "Matematik Öğretmeni 2"],            # 8
               [10, 910, "Biyoloji Öğretmeni 1"],           # 9
               [11, 911, "Biyoloji Öğretmeni 2"],           # 10
               [12, 712, "Kimya Öğretmeni 1"],              # 11
               [13, 713, "Kimya Öğretmeni 2"],              # 12
               [14, 614, "Fizik Öğretmeni 1"],              # 13
               [15, 615, "Fizik Öğretmeni 2"],              # 14
               [16, 516, "Coğrafya Öğretmeni 1"],           # 15
               [17, 517, "Coğrafya Öğretmeni 2"],           # 16
               [18, 418, "Tarih Öğretmeni 1"],              # 17
               [19, 419, "Tarih Öğretmeni 2"],              # 18
               [20, 220, "Sosyoloji Öğretmeni"],            # 19
               [21, 321, "Din Kültürü Öğretmeni"],          # 20
               [22, 1022, "İstatistik Öğretmeni 1"],        # 21
               [23, 1023, "İstatistik Öğretmeni 2"]         # 22
               ]

dersler = [[1, "Edebiyat", [11, 12], [4, 4, 4, 4, 4]],           # 0
           [2, "Sosyoloji", [220], [2, 2, 2, 2, 2]],             # 1
           [3, "Din Kültürü", [321], [2, 2, 2, 2, 2]],           # 2
           [4, "Tarih", [418, 419], [4, 4, 4, 4, 4]],            # 3
           [5, "Coğrafya", [516, 517], [2, 2, 2, 2, 2]],         # 4
           [6, "Fizik", [614, 615], [4, 4, 4, 4, 4]],            # 5
           [7, "Kimya", [712, 713], [4, 4, 4, 4, 4]],            # 6
           [8, "Matematik", [88, 89], [4, 4, 4, 4, 4]],          # 7
           [9, "Biyoloji", [9, 10], [2, 2, 2, 2, 2]],            # 8
           [10, "İstatistik", [1022, 1023], [4, 4, 4, 4, 4]],    # 9
           [11, "Müzik", [113], [1, 1, 1, 1, 1]],                # 10
           [12, "Resim", [124], [2, 2, 2, 2, 2]],                # 11
           [13, "Beden", [135], [1, 1, 1, 1, 1]],                # 12
           [14, "Yabancı Dil", [146, 147], [4, 4, 4, 4, 4]]]     # 13

ders_index = {11: 0, 12: 0, 220: 1, 321: 2, 418: 3, 419: 3, 516: 4, 517: 4, 614: 5, 615: 5, 712: 6, 713: 6, 88: 7, 89: 7, 9: 8, 10: 8, 1022: 9, 1023: 9, 113: 10, 124: 11, 135: 12, 146: 13, 147: 13}


def ogretmen_sec(dr_program, dr):
    secilen = 0
    for ogretmen in dr[2]:
        secilen = ogretmen
        for gun in range(global_gun):
            for periyod in range(global_periyod):
                if ogretmen == dr_program[gun][periyod]:
                    secilen = 0

    index = random.randint(0, 1)
    if len(dr[2])>1:
        secilen = dr[2][index]
    else:
        secilen = dr[2][0]
#    if secilen == 0:
#        for ogretmen in dr[2]:
#            secilen = ogretmen
#            if random.randint(0, 1) == 1:
#                break
    return secilen


def get_ders_saat(dr_program, dr):
    saat = 0
    for ogretmen in dr[2]:
        for gun in range(global_gun):
            for periyod in range(global_periyod):
                if ogretmen == dr_program[gun][periyod]:
                    saat = saat + 1
    return saat


def rastgele_bos_gun_periyod_bul(dr_program):
    gg = -1
    pp = -1

    while gg == -1:
        gun = random.randint(0, 4)
        periyod = random.randint(0, 7)
        if dr_program[gun][periyod] == 0:
            gg = gun
            pp = periyod

    return gg, pp


def fill_ders_programi():
    pp = global_periyod
    gg = global_gun
    dr = global_derslik
    ders_programi = [[[0] * pp for i in range(gg)] for i in range(dr)]

    for ders in dersler:
        for derslik in range(global_derslik):
            ogretmen = ogretmen_sec(ders_programi[derslik], ders)
            dr = ders[3]
            while get_ders_saat(ders_programi[derslik], ders) < dr[derslik]:
                gun, periyod = rastgele_bos_gun_periyod_bul(ders_programi[derslik])
                ders_programi[derslik][gun][periyod] = ogretmen

    return copy.deepcopy(ders_programi)


def get_ders_tanimli_saat(derslik, ogretmen):
    return dersler[ders_index[ogretmen]][3][derslik]


def get_ders_saat_ogretmen(dr_program, ogretmen):
    saat = 0
    for gun in range(global_gun):
        for periyod in range(global_periyod):
            if ders_index[ogretmen] == ders_index[dr_program[gun][periyod]]:
                saat = saat + 1
    return saat


def cevir_koordinat_dizi_boyut(x, y):
    #delta_x = (global_periyod*x) / max_bound1
    #delta_y = ((global_derslik * global_gun)*y) / max_bound2

    dizi_x = int(x)
    dizi_y = int(y)

    #if dizi_y >= global_derslik * global_gun:
    #    dizi_y = (global_derslik * global_gun) - 1

    if dizi_y > 4:
        derslik = int(dizi_y / global_derslik)
        gun = dizi_y - (int(dizi_y / global_derslik) * global_derslik)
    else:
        derslik = 0
        gun = dizi_y

    if dizi_x >= global_periyod:
        dizi_x = global_periyod-1

#    derslik = 0
    #    gun = 0
    #for i in range(global_derslik*global_gun):
        #    if i == dizi_y:
        #    break
        #gun += 1
        #if gun == 5:
        #    gun = 0
    #    derslik = derslik + 1


    periyod = dizi_x
    if derslik < 0 or derslik > 4:
        print("derslik: %i" % derslik)
        print("x: %d y: %d" % (x, y))
    if gun < 0 or gun > 4:
        print("gun: %i" % gun)
        print("x: %d y: %d" % (x, y))
    if periyod < 0 or periyod > 7:
        print("periyod: %i" % periyod)
        print("x: %d y: %d" % (x, y))
    return derslik, gun, periyod


def puanla(dr_program, derslik, gun, periyod):
    katsayi = 1
    dd = derslik
    gg = gun
    pp = periyod
    # Farklı dersliklerde aynı gün aynı dersin aynı öğretmen ile olması
    for i in range(global_derslik):
        if i != derslik:
            if dr_program[derslik][gun][periyod] == dr_program[i][gun][periyod]:
                katsayi = katsayi + (3 * 0.9)
    # Ders saati derslik için tanımlanandan farklı olması
    if get_ders_tanimli_saat(dd, dr_program[dd][gg][pp]) != get_ders_saat_ogretmen(dr_program[dd], dr_program[dd][gg][pp]):
        katsayi = katsayi + (3 * 0.9)
    # Aynı dersin farklı öğretmenlerle aynı dersliğe girmesi
    for i in range(global_gun):
        for j in range(global_periyod):
            if (ders_index[dr_program[dd][gg][pp]] == ders_index[dr_program[dd][i][j]]) & (dr_program[dd][gun][periyod] != dr_program[dd][i][j]):
                katsayi = katsayi + (3 * 0.7)
    # Aynı ders 4 saat ise 2+2 olarak günlere bölünmeli
    if get_ders_tanimli_saat(dd, dr_program[dd][gg][pp]) == 4:
        saat = 0
        for i in range(global_periyod):
            if dr_program[dd][gg][pp] == dr_program[dd][gg][i]:
                saat = saat + 1
        if saat != 2:
            katsayi = katsayi + (1 * 0.7)
    # Aynı dersin aynı günde farklı saatlerde olması
    for i in range(global_periyod):
        if i != pp:
            if (dr_program[dd][gg][i] == dr_program[dd][gg][pp]) & (i+1 != pp) & (i-1 != pp):
                katsayi = katsayi + (1 * 0.7)
    return katsayi


def toplam_program_puanla(dr_program):
    puan = 0
    for derslik in range(global_derslik):
        for gun in range(global_gun):
            for periyod in range(global_periyod):
                puan = puan + puanla(dr_program, derslik, gun, periyod)
    return puan


def str_ders_ogretmen(ders):
    dersstr = ""
    for dd in range(14):
        for dr in dersler[dd][2]:
            if dr == ders:
                dersstr = dersler[dd][1]
                break
    for dd in range(23):
        if ogretmenler[dd][1] == ders:
            dersstr = dersstr + "/" + ogretmenler[dd][2]
            break
    return dersstr


def programi_ciz(ders_programi):
    gunler = ["P.tesi", "Salı", "Çarş.", "Perş.", "Cuma"]
    for dr in range(global_derslik):
        ll = dr + 1
        derslikBaslik = "Derslik " + str(ll)
        print(derslikBaslik.ljust(299, "-"))
        print("%s|%s|%s|%s|%s|%s|%s|%s|%s|" % ("".ljust(10, ' '),
                                               "1.Saat".ljust(35, ' '),
                                               "2.Saat".ljust(35, ' '),
                                               "3.Saat".ljust(35, ' '),
                                               "4.Saat".ljust(35, ' '),
                                               "5.Saat".ljust(35, ' '),
                                               "6.Saat".ljust(35, ' '),
                                               "7.Saat".ljust(35, ' '),
                                               "8.Saat".ljust(35, ' ')
                                               ))
        for gg in range(global_gun):
            print("%s|%s|%s|%s|%s|%s|%s|%s|%s|" % (gunler[gg].ljust(10, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][0]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][1]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][2]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][3]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][4]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][5]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][6]).ljust(35, ' '),
                                                                    str_ders_ogretmen(ders_programi[dr][gg][7]).ljust(35, ' ')
                                                                    ))


# --- COST FUNCTION ------------------------------------------------------------+

# function we are attempting to optimize (minimize)
def func1(x, drprg):
    dd = copy.deepcopy(drprg)
    derslik, gun, periyod = cevir_koordinat_dizi_boyut(x[0], x[1])
    #derslik, gun, periyod = int(x[2]), int(x[0]), int(x[1])
    #print(derslik, gun, periyod)
    kaynak_derslik, kaynak_gun, kaynak_periyod = random.randint(0, global_derslik - 1), random.randint(0, global_gun - 1), random.randint(0, global_periyod - 1)
    dd[derslik][gun][periyod], dd[kaynak_derslik][kaynak_gun][kaynak_periyod] = dd[kaynak_derslik][kaynak_gun][kaynak_periyod], dd[derslik][gun][periyod]
    return toplam_program_puanla(dd), dd


# --- MAIN ---------------------------------------------------------------------+

class Particle:
    def __init__(self, x0, dr_prg):
        self.position_i = []  # particle position
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual
        self.drprg = copy.deepcopy(dr_prg)

        for i in range(0, num_dimensions):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self, costFunc):
        self.err_i, drprg2 = costFunc(self.position_i, self.drprg)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i
            self.err_best_i = self.err_i
            self.drprg = copy.deepcopy(drprg2)

    # update new particle velocity
    def update_velocity(self, pos_best_g):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1  # cognative constant
        c2 = 2  # social constant

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i] > bounds[i][1]:
                self.position_i[i] = bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i] = bounds[i][0]


def PSO(costFunc, x0, bounds, drprg, fitness, num_particles, maxiter ):
    global num_dimensions

    num_dimensions = len(x0)
    err_best_g = fitness  # best error for group
    # pos_best_g = []  # best position for group
    best_prg_g = copy.deepcopy(drprg)
    pos_best_g = list(x0)

    # establish the swarm
    swarm = []
    for i in range(0, num_particles):
        x0 = [random.randint(0, 7), random.randint(0, 24)]
        swarm.append(Particle(x0, drprg))

    # begin optimization loop
    i = 0
    while i < maxiter:
        # print i,err_best_g
        # cycle through particles in swarm and evaluate fitness
        for j in range(0, num_particles):
            swarm[j].evaluate(costFunc)

            # determine if current particle is the best (globally)
            if swarm[j].err_i < err_best_g or err_best_g == -1:
                pos_best_g = list(swarm[j].position_i)
                best_prg_g = copy.deepcopy(swarm[j].drprg)
                err_best_g = float(swarm[j].err_i)

        # cycle through swarm and update velocities and position
        for j in range(0, num_particles):
            swarm[j].update_velocity(pos_best_g)
            swarm[j].update_position(bounds)
        i += 1
    return copy.deepcopy(best_prg_g), err_best_g


def main():
    start_datetime = datetime.now()

    initial = [2, 4]  # initial starting location [x1,x2...]
    bounds = [(0, max_bound1), (0, max_bound2)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
    gl_ders_programi = fill_ders_programi()
    fitness = toplam_program_puanla(gl_ders_programi)
    eski_puan = 1000
    limit = 200
    cycle = 0
    ayni_deger = 0
    while (ayni_deger < 10 or fitness > 220) and fitness > 200 and cycle < limit:
        cycle += 1
        cycle_time =  datetime.now()
        gl_ders_programi, fitness = PSO(func1, initial, bounds, gl_ders_programi, fitness, num_particles=15, maxiter=20)
        if fitness < eski_puan:
            cycle_elapsed_time = datetime.now() - cycle_time
            print("CYCLE: %i FITNESS : %i ELAPSED TIME : %s" % (cycle, fitness, cycle_elapsed_time))
            print(gl_ders_programi)
        if fitness == eski_puan:
            ayni_deger += 1
        else:
            ayni_deger = 0
        eski_puan = fitness

    programi_ciz(gl_ders_programi)

    stop_datetime = datetime.now()
    elapsed_datetime = stop_datetime - start_datetime

    print("Start Time    : %s" % start_datetime)
    print("Stop Time     : %s" % stop_datetime)
    print("Elapsed Time  : %s\n" % elapsed_datetime)

if __name__ == "__main__":
    main()

# --- RUN ----------------------------------------------------------------------+



# --- END ----------------------------------------------------------------------+
