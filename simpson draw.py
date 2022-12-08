import turtle as tu


class rdj:
    def __init__(self):
        self.head = [(634, 277),(622, 265),(613, 257),(624, 249),(624, 238),(615, 226),(599, 222),(589, 223),(577, 206),
                     (564, 187),(538, 151),(516, 127),(489, 106),(471, 100),(451, 100),(438, 99),(418, 102),(404, 108),
                     (385, 118),(367, 135),(353, 153),(349, 163),(348, 190),(355, 211),(368, 238),(366, 257),(370, 269),
                     (378, 264),(376, 292),(389, 307),(408, 310),(410, 320),(426, 319),(424, 335),(428, 338),(432, 339),
                     (442, 340),(444, 360),(460, 390),(487, 391),(503, 387),(503, 402), (516, 420), (528, 401),
                     (541, 380),(569, 362),(591, 349),(611, 332),(620, 320),(630, 307),(640, 296),(642, 287), (-1,-1),
                     (505, 223), (518, 229), (525, 238), (530, 256), (-1,-1), (435, 240), (433, 261), (443, 277),
                     (455, 287), (472, 295), (486, 295), (-1,-1), (426, 319), (435, 308), (446, 299), (454, 289), (-1,-1), (400, 310),
                     (414, 307), (435, 299), (453, 288), (-1,-1), (457, 286), (475, 282), (489, 274), (503, 263), (513, 253), (525, 238),
                     (-1,-1), (597, 245), (598, 232), (607, 241)]

        self.hair = [(562, 242), (550, 194), (586, 204), (-1,-1), (360, 162), (357, 151), (356, 142), (357, 131),
                     (363, 126), (367, 118), (374, 112), (386, 109), (396, 107), (404, 107), (416, 112), (422, 119),
                     (429, 131), (-1,-1), (379, 139), (378, 128), (379, 114), (383, 106), (396, 101), (407, 97), (420, 94), (436, 98), (443, 107), (446, 115)]

        self.background = [(0, 5), (949, 6), (952, 701), (0, 686)]

        self.cloth = [(745, 620), (749, 597), (750, 571), (751, 546), (749, 525), (747, 500), (740, 481), (752, 472),
                      (761, 466), (767, 443), (767, 443), (769, 417), (766, 395), (758, 369), (743, 350), (726, 340),
                      (714, 338), (695, 338), (687, 328), (667, 312), (668, 287), (649, 269), (627, 270), (640, 283),
                      (637, 295), (632, 303), (622, 319), (608, 332), (588, 349), (576, 358), (556, 368), (547, 375),
                      (541, 379), (543, 380), (518, 420), (500, 380), (500, 380), (484, 395),(473, 396), (457, 394),
                      (452, 389), (447, 369), (446, 362), (427, 364), (400, 374), (387, 380),
                      (378, 386), (381, 401), (371, 446), (370, 472), (370, 504), (353, 519), (349, 537), (343, 556),
                      (338, 571), (342, 608), (375, 607), (404, 607), (440, 606), (465, 606), (495, 606), (538, 606), (562, 605), (580, 605), (563, 607), (583, 607),
                      (599, 606), (616, 606), (635, 606), (657, 606), (680, 609), (702, 613), (716, 615), (730, 619),
                      (744, 622), (747, 610), (749, 593), (-1,-1), (632, 276), (642, 276), (640, 288), (-1,-1),
                      (551, 383), (570, 403), (582, 418), (606, 402),
                      (617, 390), (630, 377), (639, 366), (651, 356), (659, 338), (662, 316), (666, 298), (-1,-1),
                      (696, 338), (677, 343), (657, 351), (641, 362), (631, 373), (621, 390), (616, 400), (615, 411), (-1,-1),
                      (380, 383), (397, 381), (415, 390), (-1,-1), (487, 394), (472, 414), (463, 428), (-1,-1),
                      (637, 278), (640, 279), (639, 282)]

        self.hand = [(404, 386), (382, 400), (363, 409), (341, 426), (324, 446), (318, 461), (317, 484), (320, 496),
                     (327, 506), (337, 516), (343, 523), (355, 527), (372, 532), (393, 537), (414, 537), (436, 535),
                     (452, 531), (469, 527), (486, 523), (494, 519), (503, 525), (515, 537), (530, 550), (547, 559),
                     (563, 567), (580, 574), (598, 577), (609, 577), (628, 575), (644, 571), (661, 563), (682, 551),
                     (699, 535), (711, 519), (723, 502), (736, 476), (739, 461), (714, 443), (693, 434), (667, 426),
                     (649, 424), (639, 423), (625, 418), (601, 412), (580, 412), (561, 413), (545, 413), (524, 417),
                     (505, 425), (500, 431), (486, 432), (464, 432), (453, 431), (449, 418), (442, 409), (437, 404),
                     (431, 399), (425, 395), (420, 392), (412, 387), (405, 386), (-1, -1), (633, 421), (644, 428),
                     (651, 437), (657, 442), (660, 451), (657, 458), (651, 460), (645, 449), (635, 439), (642, 445),
                     (648, 456), (651, 467), (652, 473), (648, 481), (639, 480), (636, 470), (629, 462), (622, 454),
                     (613, 450), (626, 458), (633, 468), (638, 475), (639, 490), (626, 490), (615, 483), (604, 475),
                     (595, 466), (579, 457), (570, 452), (558, 448), (547, 445), (529, 439), (507, 433), (484, 430),
                     (460, 430), (438, 433), (421, 436), (413, 439), (423, 450), (434, 461), (446, 472), (455, 481),
                     (465, 493), (474, 500), (487, 513), (497, 521)]

        self.mouth = [(443, 338), (443, 355), (447, 369), (449, 381), (452, 391), (455, 395), (462, 397), (470, 397),
                      (485, 394), (493, 389), (503, 381), (508, 386), (516, 386), (527, 382), (539, 378), (548, 372),
                      (560, 366), (571, 360), (586, 352), (595, 344), (596, 333), (596, 320), (587, 310), (575, 301),
                      (563, 297), (553, 295), (541, 293), (524, 296), (506, 301), (491, 307), (474, 315), (459, 328),
                      (452, 335), (443, 339), (-1,-1), (504, 381), (511, 373), (520, 366), (529, 361), (535, 357),
                      (543, 354), (550, 351)]

        self.pants = [(728, 696), (727, 659), (738, 620), (712, 610), (675, 600), (635, 603), (591, 603), (565, 605),
                      (534, 601), (483, 603), (411, 603), (381, 605), (350, 605), (352, 695), (400, 664), (449, 694),
                      (509, 695), (711, 696)]

        self.pen = tu.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.x_offset = 300
        self.y_offset = 300

    def go(self, x, y):
        self.pen.penup()
        self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.pendown()

    def paint(self, coord, co=(0, 0, 0), brush=None, thickness=1):
        if brush is None:
            self.pen.color(co)
        else:
            self.pen.color(brush)
        t_x, t_y = coord[0]
        self.pen.width(thickness)
        self.go(t_x, t_y)
        self.pen.fillcolor(co)
        self.pen.begin_fill()
        t = 0
        for i in coord[1:]:
            print(i)
            x, y = i
            if t:
                self.go(x, y)
                t = 0
                self.pen.begin_fill()
                continue
            if x == -1 and y == -1:
                t = 1
                self.pen.end_fill()
                continue
            else:
                self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        self.pen.end_fill()

    def draw_fn(self, coord, mode=1, co=(0, 0, 0), thickness=1, brush=None):
        #co = (co[0] / 255, co[1] / 255, co[2] / 255)

        if brush is None:
            self.pen.color(co)
        else:
            self.pen.color(brush)

        if mode:
            self.pen.width(thickness)
            t_x, t_y = coord[0]
            self.go(t_x, t_y)
            t = 0
            for i in coord[1:]:
                print(i)
                x, y = i
                if t:
                    self.go(x, y)
                    t = 0
                    continue
                if x == -1 and y == -1:
                    t = 1
                    continue
                else:
                    self.pen.goto(x - self.x_offset, (y * -1) + self.y_offset)
        else:
            self.paint(coord=coord, co=co, brush=brush, thickness=thickness)

    def draw(self, retain=True):
        tu.colormode(255)
        self.draw_fn(self.background, mode=0, co=(232,174,199))
        self.draw_fn(self.head, mode=0, thickness=3, co=(253,221,96), brush=(155, 93, 79))
        self.draw_fn(self.hair, mode=1, thickness=3, brush=(155,93,79))
        self.draw_fn(self.cloth, mode=0, thickness=3, co=(255,255,255), brush=(155,93,79))
        self.draw_fn(self.mouth, mode=0, thickness=3, co=(218, 183, 125), brush=(155, 93, 79))
        self.draw_fn(self.hand, mode=0, thickness=3, co=(253,221,96), brush=(155, 93, 79))
        self.draw_fn(self.pants, mode=0, thickness=3, co=(105,116,224), brush=(155, 93, 79))
        if retain:
            tu.done()

pen = rdj()
pen.draw()