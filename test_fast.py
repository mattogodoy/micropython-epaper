import epaper, time, pyb

a = epaper.Display('L', mode = epaper.FAST)

with a:
  a.clear_screen()

  while True:
    t = str(pyb.millis())
    with a.font('/sd/LiberationSerif-Regular44'):
      a.locate(0,0)
      a.puts(t)
      a.refresh()
    time.sleep(2)