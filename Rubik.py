#!/usr/bin/env python3

class Rubik():

    def __init__(self, state, debug=False, animation=False):
        self.debug = debug
        self.animation = animation
        self.step_cnt = 0

        if self.animation:
            self.state = [(i // 9, j) for i, j in enumerate(state)]
        else:
            self.state = state

        if self.debug:
            print('\n')
            print('*' * 50)
            print('[+] Debug : {}'.format(self.debug))
            print('[+] Animation : {}'.format(self.animation))
            print('[+] State : {}'.format(self.state))
            print('*' * 50)


    def run(self, seq):
        for s in seq:
            self.step_cnt += 1
            if self.debug:
                print('\n[+] Step {} : {}'.format(self.step_cnt, s))
            eval('self.{}()'.format(s))
            if self.animation:
                self.printf(self.state)

    def U(self):
        self.state[0], self.state[1], self.state[2], self.state[3], self.state[5], self.state[6], self.state[7], self.state[8], self.state[9], self.state[10], self.state[11], self.state[18], self.state[19], self.state[20], self.state[27], self.state[28], self.state[29], self.state[36], self.state[37], self.state[38] = self.state[6], self.state[3], self.state[0], self.state[7], self.state[1], self.state[8], self.state[5], self.state[2], self.state[18], self.state[19], self.state[20], self.state[27], self.state[28], self.state[29], self.state[36], self.state[37], self.state[38], self.state[9], self.state[10], self.state[11]

    def L(self):
        self.state[0], self.state[3], self.state[6], self.state[9], self.state[10], self.state[11], self.state[18], self.state[38], self.state[12], self.state[14], self.state[21], self.state[41], self.state[15], self.state[16], self.state[17], self.state[24], self.state[44], self.state[45], self.state[48], self.state[51] = self.state[44], self.state[41], self.state[38], self.state[15], self.state[12], self.state[9], self.state[0], self.state[51], self.state[16], self.state[10], self.state[3], self.state[48], self.state[17], self.state[14], self.state[11], self.state[6], self.state[45], self.state[18], self.state[21], self.state[24]

    def F(self):
        self.state[6], self.state[7], self.state[8], self.state[11], self.state[18], self.state[19], self.state[20], self.state[27], self.state[14], self.state[21], self.state[23], self.state[30], self.state[17], self.state[24], self.state[25], self.state[26], self.state[33], self.state[45], self.state[46], self.state[47] = self.state[17], self.state[14], self.state[11], self.state[45], self.state[24], self.state[21], self.state[18], self.state[6], self.state[46], self.state[25], self.state[19], self.state[7], self.state[47], self.state[26], self.state[23], self.state[20], self.state[8], self.state[33], self.state[30], self.state[27]

    def R(self):
        self.state[2], self.state[5], self.state[8], self.state[20], self.state[27], self.state[28], self.state[29], self.state[36], self.state[23], self.state[30], self.state[32], self.state[39], self.state[26], self.state[33], self.state[34], self.state[35], self.state[42], self.state[47], self.state[50], self.state[53] = self.state[20], self.state[23], self.state[26], self.state[47], self.state[33], self.state[30], self.state[27], self.state[8], self.state[50], self.state[34], self.state[28], self.state[5], self.state[53], self.state[35], self.state[32], self.state[29], self.state[2], self.state[42], self.state[39], self.state[36]

    def B(self):
        self.state[0], self.state[1], self.state[2], self.state[9], self.state[29], self.state[36], self.state[37], self.state[38], self.state[12], self.state[32], self.state[39], self.state[41], self.state[15], self.state[35], self.state[42], self.state[43], self.state[44], self.state[51], self.state[52], self.state[53] = self.state[29], self.state[32], self.state[35], self.state[2], self.state[53], self.state[42], self.state[39], self.state[36], self.state[1], self.state[52], self.state[43], self.state[37], self.state[0], self.state[51], self.state[44], self.state[41], self.state[38], self.state[9], self.state[12], self.state[15]

    def D(self):
        self.state[15], self.state[16], self.state[17], self.state[24], self.state[25], self.state[26], self.state[33], self.state[34], self.state[35], self.state[42], self.state[43], self.state[44], self.state[45], self.state[46], self.state[47], self.state[48], self.state[50], self.state[51], self.state[52], self.state[53] = self.state[42], self.state[43], self.state[44], self.state[15], self.state[16], self.state[17], self.state[24], self.state[25], self.state[26], self.state[33], self.state[34], self.state[35], self.state[51], self.state[48], self.state[45], self.state[52], self.state[46], self.state[53], self.state[50], self.state[47]

    def M(self):
        self.state[1], self.state[4], self.state[7], self.state[19], self.state[37], self.state[22], self.state[40], self.state[25], self.state[43], self.state[46], self.state[49], self.state[52] = self.state[43], self.state[40], self.state[37], self.state[1], self.state[52], self.state[4], self.state[49], self.state[7], self.state[46], self.state[19], self.state[22], self.state[25]

    def E(self):
        self.state[12], self.state[13], self.state[14], self.state[21], self.state[22], self.state[23], self.state[30], self.state[31], self.state[32], self.state[39], self.state[40], self.state[41] = self.state[39], self.state[40], self.state[41], self.state[12], self.state[13], self.state[14], self.state[21], self.state[22], self.state[23], self.state[30], self.state[31], self.state[32]

    def S(self):
        self.state[3], self.state[4], self.state[5], self.state[10], self.state[28], self.state[13], self.state[31], self.state[16], self.state[34], self.state[48], self.state[49], self.state[50] = self.state[16], self.state[13], self.state[10], self.state[48], self.state[3], self.state[49], self.state[4], self.state[50], self.state[5], self.state[34], self.state[31], self.state[28]

    def Ui(self):
    	self.U(); self.U(); self.U();

    def Li(self):
    	self.L(); self.L(); self.L();

    def Fi(self):
    	self.F(); self.F(); self.F();

    def Ri(self):
    	self.R(); self.R(); self.R();

    def Bi(self):
    	self.B(); self.B(); self.B();

    def Di(self):
    	self.D(); self.D(); self.D();

    def Mi(self):
    	self.M(); self.M(); self.M();

    def Ei(self):
    	self.E(); self.E(); self.E();

    def Si(self):
    	self.S(); self.S(); self.S();

    ############################################
    ################ !important ################
    ############################################

    fmt = {
        'white'   : '\x1b[47m\x1b[30m{}\x1b[0m',
        'magenta' : '\x1b[45m\x1b[30m{}\x1b[0m',
        'green'   : '\x1b[42m\x1b[30m{}\x1b[0m',
        'red'     : '\x1b[41m\x1b[30m{}\x1b[0m',
        'blue'    : '\x1b[44m\x1b[30m{}\x1b[0m',
        'yellow'  : '\x1b[43m\x1b[30m{}\x1b[0m'
    }

    color = ['white', 'magenta', 'green', 'red', 'blue', 'yellow']

    def f(self, s):
        return self.fmt[self.color[int(s[0])]].format(str(s[1]).zfill(2))

    def printf(self, state):
        print('                                      ')
        print('          {} {} {}                    '.format(self.f(state[ 0]), self.f(state[ 1]), self.f(state[ 2])))
        print('          {} {} {}                    '.format(self.f(state[ 3]), self.f(state[ 4]), self.f(state[ 5])))
        print('          {} {} {}                    '.format(self.f(state[ 6]), self.f(state[ 7]), self.f(state[ 8])))
        print('                                      ')
        print('{} {} {}  {} {} {}  {} {} {}  {} {} {}'.format(self.f(state[ 9]), self.f(state[10]), self.f(state[11]), self.f(state[18]), self.f(state[19]), self.f(state[20]), self.f(state[27]), self.f(state[28]), self.f(state[29]), self.f(state[36]), self.f(state[37]), self.f(state[38])))
        print('{} {} {}  {} {} {}  {} {} {}  {} {} {}'.format(self.f(state[12]), self.f(state[13]), self.f(state[14]), self.f(state[21]), self.f(state[22]), self.f(state[23]), self.f(state[30]), self.f(state[31]), self.f(state[32]), self.f(state[39]), self.f(state[40]), self.f(state[41])))
        print('{} {} {}  {} {} {}  {} {} {}  {} {} {}'.format(self.f(state[15]), self.f(state[16]), self.f(state[17]), self.f(state[24]), self.f(state[25]), self.f(state[26]), self.f(state[33]), self.f(state[34]), self.f(state[35]), self.f(state[42]), self.f(state[43]), self.f(state[44])))
        print('                                      ')
        print('          {} {} {}                    '.format(self.f(state[45]), self.f(state[46]), self.f(state[47])))
        print('          {} {} {}                    '.format(self.f(state[48]), self.f(state[49]), self.f(state[50])))
        print('          {} {} {}                    '.format(self.f(state[51]), self.f(state[52]), self.f(state[53])))
        print('                                      ')
