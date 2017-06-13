import pyb

MapperDict = {
    'X1': pyb.Pin.cpu.A0,
    'X2': pyb.Pin.cpu.A1,
    'X3': pyb.Pin.cpu.A2,
    'X4': pyb.Pin.cpu.A3,
    'X5': pyb.Pin.cpu.A4,
    'X6': pyb.Pin.cpu.A5,
    'X7': pyb.Pin.cpu.A6,
    'X8': pyb.Pin.cpu.A7,
    'X9': pyb.Pin.cpu.B6,
    'X10': pyb.Pin.cpu.B7,
    'X11': pyb.Pin.cpu.C4,
    'X12': pyb.Pin.cpu.C5,
    'X17': pyb.Pin.cpu.B3,
    'X18': pyb.Pin.cpu.C13,
    'X19': pyb.Pin.cpu.C0,
    'X20': pyb.Pin.cpu.C1,
    'X21': pyb.Pin.cpu.C2,
    'X22': pyb.Pin.cpu.C3,

    'Y1': pyb.Pin.cpu.C6,
    'Y2': pyb.Pin.cpu.C7,
    'Y3': pyb.Pin.cpu.B8,
    'Y4': pyb.Pin.cpu.B9,
    'Y5': pyb.Pin.cpu.B12,
    'Y6': pyb.Pin.cpu.B13,
    'Y7': pyb.Pin.cpu.B14,
    'Y8': pyb.Pin.cpu.B15,
    'Y9': pyb.Pin.cpu.B10,
    'Y10': pyb.Pin.cpu.B11,
    'Y11': pyb.Pin.cpu.B0,
    'Y12': pyb.Pin.cpu.B1,

    'P2': pyb.Pin.cpu.B4,
    'P3': pyb.Pin.cpu.A15,
    'P4': pyb.Pin.cpu.A14,
    'P5': pyb.Pin.cpu.A13
}

pyb.Pin.dict(MapperDict)
