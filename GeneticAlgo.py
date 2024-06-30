import numpy as np
import random

# Define the genetic algorithm parameters
POP_SIZE = 100
GENS = 200  # Increase generations for better accuracy
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.1  # Increase mutation rate for more exploration

# Example data: (paddle y-axis, ball y-axis speed, distance, actual y position)
sample_data = [
   (55, -7.5, 550, 137.5),
(55, -7.5, 500, 55.0),
(55, -7.5, 400, 242.5),
(55, -7.5, 300, 430.0),
(55, -7.5, 200, 377.5),
(55, -7.5, 100, 190.0),
(55, -7.5, 40, 77.5),
(55, -6, 550, 157),
(55, -6, 500, 235),
(55, -6, 400, 385),
(55, -6, 300, 463),
(55, -6, 200, 313),
(55, -6, 100, 163),
(55, -6, 40, 73),
(55, -4, 550, 419),
(55, -4, 500, 471),
(55, -4, 400, 419),
(55, -4, 300, 319),
(55, -4, 200, 219),
(55, -4, 100, 119),
(55, -4, 40, 59),
(55, -2, 550, 309),
(55, -2, 500, 283),
(55, -2, 400, 233),
(55, -2, 300, 183),
(55, -2, 200, 133),
(55, -2, 100, 83),
(55, -2, 40, 53),
(55, -0.5, 550, 111.5),
(55, -0.5, 500, 105.0),
(55, -0.5, 400, 92.5),
(55, -0.5, 300, 80.0),
(55, -0.5, 200, 67.5),
(55, -0.5, 100, 55.0),
(55, -0.5, 40, 52.5),
(55, 0.5, 550, 121.5),
(55, 0.5, 500, 115.0),
(55, 0.5, 400, 102.5),
(55, 0.5, 300, 90.0),
(55, 0.5, 200, 77.5),
(55, 0.5, 100, 65.0),
(55, 0.5, 40, 57.5),
(55, 2, 550, 321),
(55, 2, 500, 295),
(55, 2, 400, 245),
(55, 2, 300, 195),
(55, 2, 200, 145),
(55, 2, 100, 95),
(55, 2, 40, 65),
(55, 4, 550, 403),
(55, 4, 500, 455),
(55, 4, 400, 435),
(55, 4, 300, 335),
(55, 4, 200, 235),
(55, 4, 100, 135),
(55, 4, 40, 75),
(55, 6, 550, 145),
(55, 6, 500, 223),
(55, 6, 400, 373),
(55, 6, 300, 475),
(55, 6, 200, 325),
(55, 6, 100, 175),
(55, 6, 40, 85),
(55, 7.5, 550, 152.5),
(55, 7.5, 500, 55.0),
(55, 7.5, 400, 227.5),
(55, 7.5, 300, 415.0),
(55, 7.5, 200, 392.5),
(55, 7.5, 100, 205.0),
(55, 7.5, 40, 92.5),
(100, -7.5, 550, 92.5),
(100, -7.5, 500, 100.0),
(100, -7.5, 400, 287.5),
(100, -7.5, 300, 475.0),
(100, -7.5, 200, 332.5),
(100, -7.5, 100, 145.0),
(100, -7.5, 40, 62.5),
(100, -6, 550, 202),
(100, -6, 500, 280),
(100, -6, 400, 430),
(100, -6, 300, 412),
(100, -6, 200, 262),
(100, -6, 100, 112),
(100, -6, 40, 70),
(100, -4, 550, 464),
(100, -4, 500, 476),
(100, -4, 400, 376),
(100, -4, 300, 276),
(100, -4, 200, 176),
(100, -4, 100, 76),
(100, -4, 40, 80),
(100, -2, 550, 266),
(100, -2, 500, 240),
(100, -2, 400, 190),
(100, -2, 300, 140),
(100, -2, 200, 90),
(100, -2, 100, 60),
(100, -2, 40, 90),
(100, -0.5, 550, 66.5),
(100, -0.5, 500, 60.0),
(100, -0.5, 400, 52.5),
(100, -0.5, 300, 65.0),
(100, -0.5, 200, 77.5),
(100, -0.5, 100, 90.0),
(100, -0.5, 40, 97.5),
(100, 0.5, 550, 166.5),
(100, 0.5, 500, 160.0),
(100, 0.5, 400, 147.5),
(100, 0.5, 300, 135.0),
(100, 0.5, 200, 122.5),
(100, 0.5, 100, 110.0),
(100, 0.5, 40, 102.5),
(100, 2, 550, 366),
(100, 2, 500, 340),
(100, 2, 400, 290),
(100, 2, 300, 240),
(100, 2, 200, 190),
(100, 2, 100, 140),
(100, 2, 40, 110),
(100, 4, 550, 360),
(100, 4, 500, 412),
(100, 4, 400, 480),
(100, 4, 300, 380),
(100, 4, 200, 280),
(100, 4, 100, 180),
(100, 4, 40, 120),
(100, 6, 550, 94),
(100, 6, 500, 172),
(100, 6, 400, 322),
(100, 6, 300, 472),
(100, 6, 200, 370),
(100, 6, 100, 220),
(100, 6, 40, 130),
(100, 7.5, 550, 197.5),
(100, 7.5, 500, 100.0),
(100, 7.5, 400, 182.5),
(100, 7.5, 300, 370.0),
(100, 7.5, 200, 437.5),
(100, 7.5, 100, 250.0),
(100, 7.5, 40, 137.5),
(150, -7.5, 550, 52.5),
(150, -7.5, 500, 150.0),
(150, -7.5, 400, 337.5),
(150, -7.5, 300, 465.0),
(150, -7.5, 200, 277.5),
(150, -7.5, 100, 90.0),
(150, -7.5, 40, 112.5),
(150, -6, 550, 252),
(150, -6, 500, 330),
(150, -6, 400, 480),
(150, -6, 300, 366),
(150, -6, 200, 216),
(150, -6, 100, 66),
(150, -6, 40, 120),
(150, -4, 550, 482),
(150, -4, 500, 430),
(150, -4, 400, 330),
(150, -4, 300, 230),
(150, -4, 200, 130),
(150, -4, 100, 70),
(150, -4, 40, 130),
(150, -2, 550, 216),
(150, -2, 500, 190),
(150, -2, 400, 140),
(150, -2, 300, 90),
(150, -2, 200, 60),
(150, -2, 100, 110),
(150, -2, 40, 140),
(150, -0.5, 550, 83.5),
(150, -0.5, 500, 90.0),
(150, -0.5, 400, 102.5),
(150, -0.5, 300, 115.0),
(150, -0.5, 200, 127.5),
(150, -0.5, 100, 140.0),
(150, -0.5, 40, 147.5),
(150, 0.5, 550, 216.5),
(150, 0.5, 500, 210.0),
(150, 0.5, 400, 197.5),
(150, 0.5, 300, 185.0),
(150, 0.5, 200, 172.5),
(150, 0.5, 100, 160.0),
(150, 0.5, 40, 152.5),
(150, 2, 550, 416),
(150, 2, 500, 390),
(150, 2, 400, 340),
(150, 2, 300, 290),
(150, 2, 200, 240),
(150, 2, 100, 190),
(150, 2, 40, 160),
(150, 4, 550, 306),
(150, 4, 500, 358),
(150, 4, 400, 458),
(150, 4, 300, 430),
(150, 4, 200, 330),
(150, 4, 100, 230),
(150, 4, 40, 170),
(150, 6, 550, 48),
(150, 6, 500, 126),
(150, 6, 400, 276),
(150, 6, 300, 426),
(150, 6, 200, 420),
(150, 6, 100, 270),
(150, 6, 40, 180),
(150, 7.5, 550, 247.5),
(150, 7.5, 500, 150.0),
(150, 7.5, 400, 127.5),
(150, 7.5, 300, 315.0),
(150, 7.5, 200, 487.5),
(150, 7.5, 100, 300.0),
(150, 7.5, 40, 187.5),
(200, -7.5, 550, 102.5),
(200, -7.5, 500, 200.0),
(200, -7.5, 400, 387.5),
(200, -7.5, 300, 425.0),
(200, -7.5, 200, 237.5),
(200, -7.5, 100, 50.0),
(200, -7.5, 40, 162.5),
(200, -6, 550, 290),
(200, -6, 500, 368),
(200, -6, 400, 470),
(200, -6, 300, 320),
(200, -6, 200, 170),
(200, -6, 100, 80),
(200, -6, 40, 170),
(200, -4, 550, 428),
(200, -4, 500, 376),
(200, -4, 400, 276),
(200, -4, 300, 176),
(200, -4, 200, 76),
(200, -4, 100, 120),
(200, -4, 40, 180),
(200, -2, 550, 166),
(200, -2, 500, 140),
(200, -2, 400, 90),
(200, -2, 300, 60),
(200, -2, 200, 110),
(200, -2, 100, 160),
(200, -2, 40, 190),
(200, -0.5, 550, 133.5),
(200, -0.5, 500, 140.0),
(200, -0.5, 400, 152.5),
(200, -0.5, 300, 165.0),
(200, -0.5, 200, 177.5),
(200, -0.5, 100, 190.0),
(200, -0.5, 40, 197.5),
(200, 0.5, 550, 266.5),
(200, 0.5, 500, 260.0),
(200, 0.5, 400, 247.5),
(200, 0.5, 300, 235.0),
(200, 0.5, 200, 222.5),
(200, 0.5, 100, 210.0),
(200, 0.5, 40, 202.5),
(200, 2, 550, 466),
(200, 2, 500, 440),
(200, 2, 400, 390),
(200, 2, 300, 340),
(200, 2, 200, 290),
(200, 2, 100, 240),
(200, 2, 40, 210),
(200, 4, 550, 260),
(200, 4, 500, 312),
(200, 4, 400, 412),
(200, 4, 300, 480),
(200, 4, 200, 380),
(200, 4, 100, 280),
(200, 4, 40, 220),
(200, 6, 550, 110),
(200, 6, 500, 68),
(200, 6, 400, 218),
(200, 6, 300, 368),
(200, 6, 200, 470),
(200, 6, 100, 320),
(200, 6, 40, 230),
(200, 7.5, 550, 297.5),
(200, 7.5, 500, 200.0),
(200, 7.5, 400, 87.5),
(200, 7.5, 300, 275.0),
(200, 7.5, 200, 462.5),
(200, 7.5, 100, 350.0),
(200, 7.5, 40, 237.5),
(250, -7.5, 550, 152.5),
(250, -7.5, 500, 250.0),
(250, -7.5, 400, 437.5),
(250, -7.5, 300, 370.0),
(250, -7.5, 200, 182.5),
(250, -7.5, 100, 100.0),
(250, -7.5, 40, 212.5),
(250, -6, 550, 352),
(250, -6, 500, 430),
(250, -6, 400, 412),
(250, -6, 300, 262),
(250, -6, 200, 112),
(250, -6, 100, 130),
(250, -6, 40, 220),
(250, -4, 550, 382),
(250, -4, 500, 330),
(250, -4, 400, 230),
(250, -4, 300, 130),
(250, -4, 200, 70),
(250, -4, 100, 170),
(250, -4, 40, 230),
(250, -2, 550, 116),
(250, -2, 500, 90),
(250, -2, 400, 60),
(250, -2, 300, 110),
(250, -2, 200, 160),
(250, -2, 100, 210),
(250, -2, 40, 240),
(250, -0.5, 550, 183.5),
(250, -0.5, 500, 190.0),
(250, -0.5, 400, 202.5),
(250, -0.5, 300, 215.0),
(250, -0.5, 200, 227.5),
(250, -0.5, 100, 240.0),
(250, -0.5, 40, 247.5),
(250, 0.5, 550, 316.5),
(250, 0.5, 500, 310.0),
(250, 0.5, 400, 297.5),
(250, 0.5, 300, 285.0),
(250, 0.5, 200, 272.5),
(250, 0.5, 100, 260.0),
(250, 0.5, 40, 252.5),
(250, 2, 550, 472),
(250, 2, 500, 490),
(250, 2, 400, 440),
(250, 2, 300, 390),
(250, 2, 200, 340),
(250, 2, 100, 290),
(250, 2, 40, 260),
(250, 4, 550, 206),
(250, 4, 500, 258),
(250, 4, 400, 358),
(250, 4, 300, 458),
(250, 4, 200, 430),
(250, 4, 100, 330),
(250, 4, 40, 270),
(250, 6, 550, 148),
(250, 6, 500, 70),
(250, 6, 400, 172),
(250, 6, 300, 322),
(250, 6, 200, 472),
(250, 6, 100, 370),
(250, 6, 40, 280),
(250, 7.5, 550, 347.5),
(250, 7.5, 500, 250.0),
(250, 7.5, 400, 62.5),
(250, 7.5, 300, 220.0),
(250, 7.5, 200, 407.5),
(250, 7.5, 100, 400.0),
(250, 7.5, 40, 287.5),
(300, -7.5, 550, 202.5),
(300, -7.5, 500, 300.0),
(300, -7.5, 400, 487.5),
(300, -7.5, 300, 315.0),
(300, -7.5, 200, 127.5),
(300, -7.5, 100, 150.0),
(300, -7.5, 40, 262.5),
(300, -6, 550, 402),
(300, -6, 500, 480),
(300, -6, 400, 366),
(300, -6, 300, 216),
(300, -6, 200, 66),
(300, -6, 100, 180),
(300, -6, 40, 270),
(300, -4, 550, 328),
(300, -4, 500, 276),
(300, -4, 400, 176),
(300, -4, 300, 76),
(300, -4, 200, 120),
(300, -4, 100, 220),
(300, -4, 40, 280),
(300, -2, 550, 66),
(300, -2, 500, 60),
(300, -2, 400, 110),
(300, -2, 300, 160),
(300, -2, 200, 210),
(300, -2, 100, 260),
(300, -2, 40, 290),
(300, -0.5, 550, 233.5),
(300, -0.5, 500, 240.0),
(300, -0.5, 400, 252.5),
(300, -0.5, 300, 265.0),
(300, -0.5, 200, 277.5),
(300, -0.5, 100, 290.0),
(300, -0.5, 40, 297.5),
(300, 0.5, 550, 366.5),
(300, 0.5, 500, 360.0),
(300, 0.5, 400, 347.5),
(300, 0.5, 300, 335.0),
(300, 0.5, 200, 322.5),
(300, 0.5, 100, 310.0),
(300, 0.5, 40, 302.5),
(300, 2, 550, 422),
(300, 2, 500, 448),
(300, 2, 400, 490),
(300, 2, 300, 440),
(300, 2, 200, 390),
(300, 2, 100, 340),
(300, 2, 40, 310),
(300, 4, 550, 160),
(300, 4, 500, 212),
(300, 4, 400, 312),
(300, 4, 300, 412),
(300, 4, 200, 480),
(300, 4, 100, 380),
(300, 4, 40, 320),
(300, 6, 550, 198),
(300, 6, 500, 120),
(300, 6, 400, 126),
(300, 6, 300, 276),
(300, 6, 200, 426),
(300, 6, 100, 420),
(300, 6, 40, 330),
(300, 7.5, 550, 397.5),
(300, 7.5, 500, 300.0),
(300, 7.5, 400, 112.5),
(300, 7.5, 300, 165.0),
(300, 7.5, 200, 352.5),
(300, 7.5, 100, 450.0),
(300, 7.5, 40, 337.5),
(350, -7.5, 550, 252.5),
(350, -7.5, 500, 350.0),
(350, -7.5, 400, 462.5),
(350, -7.5, 300, 275.0),
(350, -7.5, 200, 87.5),
(350, -7.5, 100, 200.0),
(350, -7.5, 40, 312.5),
(350, -6, 550, 440),
(350, -6, 500, 470),
(350, -6, 400, 320),
(350, -6, 300, 170),
(350, -6, 200, 80),
(350, -6, 100, 230),
(350, -6, 40, 320),
(350, -4, 550, 282),
(350, -4, 500, 230),
(350, -4, 400, 130),
(350, -4, 300, 70),
(350, -4, 200, 170),
(350, -4, 100, 270),
(350, -4, 40, 330),
(350, -2, 550, 84),
(350, -2, 500, 110),
(350, -2, 400, 160),
(350, -2, 300, 210),
(350, -2, 200, 260),
(350, -2, 100, 310),
(350, -2, 40, 340),
(350, -0.5, 550, 283.5),
(350, -0.5, 500, 290.0),
(350, -0.5, 400, 302.5),
(350, -0.5, 300, 315.0),
(350, -0.5, 200, 327.5),
(350, -0.5, 100, 340.0),
(350, -0.5, 40, 347.5),
(350, 0.5, 550, 416.5),
(350, 0.5, 500, 410.0),
(350, 0.5, 400, 397.5),
(350, 0.5, 300, 385.0),
(350, 0.5, 200, 372.5),
(350, 0.5, 100, 360.0),
(350, 0.5, 40, 352.5),
(350, 2, 550, 372),
(350, 2, 500, 398),
(350, 2, 400, 448),
(350, 2, 300, 490),
(350, 2, 200, 440),
(350, 2, 100, 390),
(350, 2, 40, 360),
(350, 4, 550, 106),
(350, 4, 500, 158),
(350, 4, 400, 258),
(350, 4, 300, 358),
(350, 4, 200, 458),
(350, 4, 100, 430),
(350, 4, 40, 370),
(350, 6, 550, 260),
(350, 6, 500, 182),
(350, 6, 400, 68),
(350, 6, 300, 218),
(350, 6, 200, 368),
(350, 6, 100, 470),
(350, 6, 40, 380),
(350, 7.5, 550, 447.5),
(350, 7.5, 500, 350.0),
(350, 7.5, 400, 162.5),
(350, 7.5, 300, 125.0),
(350, 7.5, 200, 312.5),
(350, 7.5, 100, 500.0),
(350, 7.5, 40, 387.5),
(400, -7.5, 550, 302.5),
(400, -7.5, 500, 400.0),
(400, -7.5, 400, 407.5),
(400, -7.5, 300, 220.0),
(400, -7.5, 200, 62.5),
(400, -7.5, 100, 250.0),
(400, -7.5, 40, 362.5),
(400, -6, 550, 490),
(400, -6, 500, 412),
(400, -6, 400, 262),
(400, -6, 300, 112),
(400, -6, 200, 130),
(400, -6, 100, 280),
(400, -6, 40, 370),
(400, -4, 550, 228),
(400, -4, 500, 176),
(400, -4, 400, 76),
(400, -4, 300, 120),
(400, -4, 200, 220),
(400, -4, 100, 320),
(400, -4, 40, 380),
(400, -2, 550, 134),
(400, -2, 500, 160),
(400, -2, 400, 210),
(400, -2, 300, 260),
(400, -2, 200, 310),
(400, -2, 100, 360),
(400, -2, 40, 390),
(400, -0.5, 550, 333.5),
(400, -0.5, 500, 340.0),
(400, -0.5, 400, 352.5),
(400, -0.5, 300, 365.0),
(400, -0.5, 200, 377.5),
(400, -0.5, 100, 390.0),
(400, -0.5, 40, 397.5),
(400, 0.5, 550, 466.5),
(400, 0.5, 500, 460.0),
(400, 0.5, 400, 447.5),
(400, 0.5, 300, 435.0),
(400, 0.5, 200, 422.5),
(400, 0.5, 100, 410.0),
(400, 0.5, 40, 402.5),
(400, 2, 550, 322),
(400, 2, 500, 348),
(400, 2, 400, 398),
(400, 2, 300, 448),
(400, 2, 200, 490),
(400, 2, 100, 440),
(400, 2, 40, 410),
(400, 4, 550, 60),
(400, 4, 500, 112),
(400, 4, 400, 212),
(400, 4, 300, 312),
(400, 4, 200, 412),
(400, 4, 100, 480),
(400, 4, 40, 420),
(400, 6, 550, 298),
(400, 6, 500, 220),
(400, 6, 400, 70),
(400, 6, 300, 172),
(400, 6, 200, 322),
(400, 6, 100, 472),
(400, 6, 40, 430),
(400, 7.5, 550, 497.5),
(400, 7.5, 500, 400.0),
(400, 7.5, 400, 212.5),
(400, 7.5, 300, 70.0),
(400, 7.5, 200, 257.5),
(400, 7.5, 100, 445.0),
(400, 7.5, 40, 437.5),
(450, -7.5, 550, 352.5),
(450, -7.5, 500, 450.0),
(450, -7.5, 400, 352.5),
(450, -7.5, 300, 165.0),
(450, -7.5, 200, 112.5),
(450, -7.5, 100, 300.0),
(450, -7.5, 40, 412.5),
(450, -6, 550, 444),
(450, -6, 500, 366),
(450, -6, 400, 216),
(450, -6, 300, 66),
(450, -6, 200, 180),
(450, -6, 100, 330),
(450, -6, 40, 420),
(450, -4, 550, 182),
(450, -4, 500, 130),
(450, -4, 400, 70),
(450, -4, 300, 170),
(450, -4, 200, 270),
(450, -4, 100, 370),
(450, -4, 40, 430),
(450, -2, 550, 184),
(450, -2, 500, 210),
(450, -2, 400, 260),
(450, -2, 300, 310),
(450, -2, 200, 360),
(450, -2, 100, 410),
(450, -2, 40, 440),
(450, -0.5, 550, 383.5),
(450, -0.5, 500, 390.0),
(450, -0.5, 400, 402.5),
(450, -0.5, 300, 415.0),
(450, -0.5, 200, 427.5),
(450, -0.5, 100, 440.0),
(450, -0.5, 40, 447.5),
(450, 0.5, 550, 470.5),
(450, 0.5, 500, 477.0),
(450, 0.5, 400, 489.5),
(450, 0.5, 300, 485.0),
(450, 0.5, 200, 472.5),
(450, 0.5, 100, 460.0),
(450, 0.5, 40, 452.5),
(450, 2, 550, 272),
(450, 2, 500, 298),
(450, 2, 400, 348),
(450, 2, 300, 398),
(450, 2, 200, 448),
(450, 2, 100, 490),
(450, 2, 40, 460),
(450, 4, 550, 94),
(450, 4, 500, 58),
(450, 4, 400, 158),
(450, 4, 300, 258),
(450, 4, 200, 358),
(450, 4, 100, 458),
(450, 4, 40, 470),
(450, 6, 550, 348),
(450, 6, 500, 270),
(450, 6, 400, 120),
(450, 6, 300, 126),
(450, 6, 200, 276),
(450, 6, 100, 426),
(450, 6, 40, 480),
(450, 7.5, 550, 442.5),
(450, 7.5, 500, 450.0),
(450, 7.5, 400, 262.5),
(450, 7.5, 300, 75.0),
(450, 7.5, 200, 202.5),
(450, 7.5, 100, 390.0),
(450, 7.5, 40, 487.5)
]

# Fitness function: Mean squared error
def fitness(individual, data):
    y, speed, pos, actual_y = np.array(data).T
    predicted_y = individual[0] * y + individual[1] * speed + individual[2] * pos + individual[3]
    error = np.sum((predicted_y - actual_y) ** 2)
    return -error  # Negative error for maximization

# Generate initial population
def generate_population(size):
    return [np.random.uniform(-1, 1, 4) for _ in range(size)]

# Selection: Tournament selection
def select(population, scores):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, scores)), 3)
        selected.append(max(tournament, key=lambda x: x[1])[0])
    return selected

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, len(parent1) - 1)
        child1 = np.concatenate((parent1[:point], parent2[point:]))
        child2 = np.concatenate((parent2[:point], parent1[point:]))
        return child1, child2
    else:
        return parent1, parent2

# Mutation: Random mutation
def mutate(individual):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(individual) - 1)
        individual[index] = np.random.uniform(-1, 1)
    return individual

# Genetic Algorithm
def genetic_algorithm(data, pop_size, gens):
    population = generate_population(pop_size)
    for gen in range(gens):
        scores = [fitness(ind, data) for ind in population]
        selected = select(population, scores)
        children = []
        for i in range(0, len(selected), 2):
            if i + 1 < len(selected):
                child1, child2 = crossover(selected[i], selected[i + 1])
                children.append(mutate(child1))
                children.append(mutate(child2))
            else:
                children.append(mutate(selected[i]))
        population = children

    # Best solution
    scores = [fitness(ind, data) for ind in population]
    best_index = np.argmax(scores)
    best_solution = population[best_index]
    return best_solution

# Cache the best solution
best_solution = genetic_algorithm(sample_data, POP_SIZE, GENS)

# Predict function using cached solution
def predict_y_position(y, speed, pos):
    return best_solution[0] * y + best_solution[1] * speed + best_solution[2] * pos + best_solution[3]

# Validate predictions against actual data
def validate_solution(solution, data):
    predictions = []
    for y, speed, pos, _ in data:
        predicted_y = solution[0] * y + solution[1] * speed + solution[2] * pos + solution[3]
        predictions.append(predicted_y)
    return predictions

# Validate predictions
# predictions = validate_solution(best_solution, sample_data)

# Print results
# print("Best solution:", best_solution)
# print("Predicted Y Positions:", predictions)

# actual_data = [predicted_y for _, _, _, predicted_y in sample_data]
# for pred, actual in zip(predictions, actual_data):
#     print(f"Predicted: {pred:.2f}, Actual: {actual}")

# # Accuracy test (mean squared error)
# mse = np.mean([(pred - actual) ** 2 for pred, actual in zip(predictions, actual_data)])
# print(f"Mean Squared Error: {mse:.2f}")

# # Example prediction
# example_y = 250
# example_speed = -4
# example_pos = 300
# predicted_y = predict_y_position(example_y, example_speed, example_pos)
# print(f"Predicted Y Position for y={example_y}, speed={example_speed}, pos={example_pos}: {predicted_y:.2f}")