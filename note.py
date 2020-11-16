try:
    b = "text"
    while True:
	from system_hotkey import SystemHotkey
	hk = SystemHotkeys()
	hk.register(('control', 'shift', 'h'), callback=lambda:print("Easy!"))
	a = input()
	b = b + "\n" + a
	f= open("note.txt","w+")
	f.write(b)
	f.close()
except KeyboardInterrupt:
    pass
