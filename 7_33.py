team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2


print('В команде Мастера кода участников: %d!' % team1_num)
print('Итого сегодня в командах участников: %d и %d' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач {}!'.format(score2))
print('Волшебники данных решили задачи за {:.1f} c! '.format(team2_time))
print(f'Команды решили {score1} и {score2} задач.')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода"
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победы команды Волшебники данных'
else:
    challenge_result = 'Ничья!'
challenge_result = challenge_result[:1].lower() + challenge_result[1:]
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {(team1_time + team2_time)/ tasks_total:.1f} секунды на '
      f'задачу!')
