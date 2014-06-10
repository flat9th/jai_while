
yomeFlg = False # True:採用 / False:不採用
jai_kekkon = False

while jai_kekkon:
  yomeFlg = yome_condition(saiyou_jyoshi) # 嫁として対象になればTrue。yome_conditionは嫁条件の関数
  if yomeflg:
    jai_kekkon = yome_attack(saiyou_jyoshi) # yome_attack 嫁候補にJAIがアタック
    if jai_kekkon:
      break
    else:
      kubi(saiyou_jyoshi)


