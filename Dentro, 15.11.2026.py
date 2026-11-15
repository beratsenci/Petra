A = "X Kişisi"
# A Değişkeni kullanıcının adı içindir.
C = "Petra"
# C değişkeni yapay zekânın adı içindir.

while True:
    B = input(f"{A}:")

    if B.casefold().strip() in ["dur", "dur!", "kapan", "kendini kapat", "kapan!", "kendini kapat!", "kendini kapatabilir misin?"]:
     print(f"Anladım, sonra görüşmek üzere {A}." or f"Anladım, sonra tekrar görüşme dileği ile {A}" or f"Anladım, iyi günler dilerim {A}")
     break

    elif B.casefold().strip() in ["merhaba", "merhaba!", "merhaba?", "merhabaa", "merhabaa!"]:
     print(f"Merhaba, size bugün nasıl yardımcı olabilirim {A}?")

    elif B.casefold().strip() in ["adın ne", "adın ne?", "adınız nedir", "adınız nedir?"]:
     print(f"Benim adım {C}, {A}.")

    elif B.casefold().strip() in ["nasılsın", "nasılsın?", "nasılsınız", "nasılsınız?", "nasılsın iyi misin", "nasılsın? iyi misin?"]:
      print(f"Benim duygularım olmadığı için bu soruya dürüst bir cevap vermem mümkün değil, fakat yine de sorduğun için çok teşekkür ederim {A}." or f"Benim duygularım yok {A}, fakat yine de sorduğun için çok teşekkür ederim.")

    else:
      print(f"Girdinizi tam olarak anlayamadım {A}.")
        
