def calculation(price, tax):
  total = price + (price* (tax/ 100))
  return total

total_amount = calculation(100, 10)
print(f"合計金額は{total_amount}円です。")