import pyb, epaper, courier25

a = epaper.Display(side = 'L')

a.clear_screen()

with a.font(courier25):
  a.puts('It works!')

a.show()