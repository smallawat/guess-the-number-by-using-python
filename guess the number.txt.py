import random

play_game = 'y'
while(play_game == 'y'):
     ans = random.randint(1,100)
     try_number = input('Guess a number betwen 1& 100:')
     try_number = int(try_number)
     counter = 1
     
     while try_number  != ans:
         if try_number > ans:
             print('your number is too large.')
         if try_number < ans:
             print('your number is too small.')
         try_number = int(input('Guess a number betwen 1& 100:'))
         counter = counter + 1
     print('you got it! you tried ' + str(counter) + 'times.')
     play_game = input('continue?')