import function as fn
DRIVERS_DATA = 'driver.txt'
BUSES_DATA = 'bus.txt'
ROUTES_DATA = 'route.txt'


RUN = True

while RUN:
    fn.console_clear()
    MODE = fn.main_menu()
    if MODE == '1':
        fn.bus_print(BUSES_DATA)
        print()
        input('Нажмите Enter чтобы вернуться в меню..')
    elif MODE == '2':
        fn.bus_add(BUSES_DATA)
        print()
        input('Нажмите Enter чтобы вернуться в меню..')
    elif MODE == '3':
        fn.driver_print(DRIVERS_DATA, BUSES_DATA)
        print()
        input('Нажмите Enter чтобы вернуться в меню..')
    elif MODE == '4':
        fn.driver_add(DRIVERS_DATA)
        print()
        input('Нажмите Enter чтобы вернуться в меню..')
    elif MODE == '5':
        fn.console_clear()
        fn.route_print(ROUTES_DATA, BUSES_DATA)
        print()
        input('Нажмите Enter чтобы вернуться в меню..')
    elif MODE == '6':
        fn.console_clear()
        fn.route_add(ROUTES_DATA)
        print()
        input('Нажмите Enter чтобы вернуться в меню..')
    elif MODE == '7':
        fn.console_clear()
        print()
        print('всего доброго!')
        RUN = False
    else:
        fn.console_clear()
        print('неизвестная комманда')
        print()
        input('Нажмите Enter чтобы вернуться в меню..')