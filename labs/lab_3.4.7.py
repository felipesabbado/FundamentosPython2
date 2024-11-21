# The Timer class

class Timer:
    def __init__(self, hour = 0, min = 0, sec = 0):
        self.__hour = hour
        self.__min = min
        self.__sec = sec

    def __str__(self):
        h = str(self.__hour).zfill(2)
        m = str(self.__min).zfill(2)
        s = str(self.__sec).zfill(2)
        return f'{h}:{m}:{s}'

    def next_second(self):
        self.__sec += 1
        if self.__sec == 60:
            self.__sec = 0
            self.__min += 1
        if self.__min == 60:
            self.__min = 0
            self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0


    def prev_second(self):
        self.__sec -= 1
        if self.__sec == -1:
            self.__sec = 59
            self.__min -= 1
        if self.__min == -1:
            self.__min = 59
            self.__hour -= 1
        if self.__hour == -1:
            self.__hour = 23


timer = Timer(23, 59, 59)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

print('-------- Testes --------')
timer1 = Timer(23, 59, 59)
timer2 = Timer(0, 0, 0)
print('Timer 1:', timer1)
print('Timer 2:', timer2)

add = 23
print(f'Adicionando {add} segundos ao Timer 1:')
for i in range(add):
    timer1.next_second()
print('Timer 1:', timer1)

sub = 125
print(f'Subtraindo {sub} segundos ao Timer 2:')
for i in range(sub):
    timer2.prev_second()
print('Timer 2:', timer2)
