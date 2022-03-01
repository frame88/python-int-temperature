scala = input('In che scala? Inserisci F per Fahrenheit, o C per Celsius \t')
a = int(input('inserisci i gradi: '))

if scala == 'F':
    a = (a - 32)/1.8  #conversione in Celsius

if a < 0:
    print('A questa temperatura,', a, 'gradi Celsius, l\'acqua è allo stato solido')
if 0 < a < 100:
    print('A questa temperatura,', a, 'gradi Celsius, l\'acqua è allo stato liquido')
if a > 100:
    print('A questa temperatura,', a, 'gradi Celsius, l\'acqua è allo stato gassoso')


    

