money = int(input('введите сумму вклада'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
ТКБ = int((per_cent['ТКБ'])*(money/100))
СКБ = int((per_cent['СКБ'])*(money/100))
ВТБ = int((per_cent['ВТБ'])*(money/100))
СБЕР = int((per_cent['СБЕР'])*(money/100))
deposit = ТКБ,СКБ,ВТБ,СБЕР
print(deposit,'ТКБ,СКБ,ВТБ,СБЕР')
id = max(deposit)
print('Максимальная сумма, которую вы можете заработать',id)
