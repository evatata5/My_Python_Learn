def main():
  total_symbol = 1578
  total_page = 0
  symbol = 0
  while symbol < total_symbol:
     total_page += 1
     symbol += len(str(total_page))
  print(f"Всего страниц {total_page}")
  print(f"Всего символов {symbol}")
  print("Test!!!!")
  print("Test from web")
  
if __name__ == "__main__":
  main()
