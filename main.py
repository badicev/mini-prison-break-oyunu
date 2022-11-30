print('''
************************************************************
     \                  ###PRISON###                 /
      \                  ##BREAK##                  /
       \                                           /
        \                                         /
         \                                       /
          \                                     /
           \                                   /
            \_________________________________/
            |                                 |
            |                                 |
            |                                 |
            |            _________            |
            |           |         |           |
            |           |   ___   |           |
            |           I  |___|  |           |
            |           |         |           |
            |           |         |           |
            |           |        _|           |
            |           |       |#|           |  ;,
    -- ___  |           |         |           |   ;'
    T*/   ` |           |         |      _____|    .,`
    */     )|           I         |     \_____\     ;'
    /___.,';|           |         |     \\     \     ."`
    |     ; |___________|_________|______\\     \      ;:
**********************************************************

''')
print("Hapishaneye hoş geldin!")
print("Kaçıp kaçamamak senin elinde.")

choice1 = input(
    'Gardiyanlardan biri hata yaptı, kapı açık. "Sağ"a mı gideceksin yoksa "Sol"a mı?'
)
choice1.lower()

if choice1 == "sağ":
    print("Yan hücredeki suçlu seni ispiyonlandı. Yakalandın. Oyun bitti!")
elif choice1 == "sol":
    choice2 = input(
    'Gardiyan kapıyı açık bıraktığını hatırladı ve geri dönüyor. "Kaçmak" mı istersin, "Saklanmak" mı?'
).lower()
    if choice2 == "kaçmak":
      print("Gardiyan seni gördü, yakalandın. Oyun bitti!")
    elif choice2 == "saklanmak":
      print("Gardiyan kapıyı kapalı gördü ve geri döndü.")
      choice3 = input(
                  'Çıkışa yaklaştın ancak çıkış kapısının önünde bir sürü buton var. "Kırmızı", "Yeşil", "Mavi", "Pembe" Hangisine basacaksın?').lower()
      if choice3 == "pembe":
        print("Tebrikler, hapishaneden kaçmayı başardın!")
      else:
        print("Sonsuza dek burada çürüyeceksin! HAHAHAHA")
    else:
      print("Lütfen geçerli bir yanıt girniz.")
else:
    print("Lütfen geçerli bir yanıt giriniz.")






