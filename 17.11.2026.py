import random

A = "Kullanıcı"
# A değişkeni kullanıcının adı içindir.
B = "Petra"
# B değişkeni yapay zekânın adı içindir.

C = [
    f"Merhaba, ben {B}. Size nasıl yardımcı olabilirim {A}?",
    f"Merhaba {A}. Size nasıl yardımcı olabilirim?",
    f"İyi günler {A}, ben {B}. Size nasıl yardımcı olabilirim?",
]

print(random.choice(C))

while True:
    E = input(f"{A}: ").strip()
    F = E.casefold()

    if F in [
        "dur",
        "dur!",
        "durabilir misin",
        "durabilir misin?",
        "çık",
        "çık!",
        "çıkabilir misin",
        "çıkabilir misin?",
        "kapan",
        "git",
        "kapanır mısın",
        "kapanır mısın?",
        "kapanabilir misin",
        "kapanabilir misin?",
    ]:
        print(f"Anlaşıldı, sonra görüşmek dileği ile {A}.")
        break

    elif F in [
        "merhaba",
        "merhaba!",
        "merhaba?",
        "merhabaa",
        "merhabaa!",
        "mrb",
    ]:
        print(f"Merhaba {A}. Size nasıl yardımcı olabilirim?")

    elif F in [
        "nasılsın",
        "nasılsın?",
        "naasılsın",
        "naasılsın?",
        "naber",
        "naber?",
        "naaber",
        "naaber?",
        "ne haber",
        "ne haber?",
        "ne habeer",
        "ne habeer?",
        "nbr",
        "nbr?",
    ]:
        print(f"İyiyim, sorduğunuz için teşekkür ederim. Peki siz nasılsınız {A}?")

    elif F in [
        "kötüyüm",
        "çok kötüyüm",
        "kötüyüm!",
        "çok kötüyüm!",
        "kötüyüm...",
        "çok kötüyüm...",
        "iyi değilim",
        "iyi değilim...",
    ]:
        print(f"Ah, bu sizin için zorlayıcı olmalı {A}. Biraz bu durumun sebebini anlatmak ister misiniz?")

    elif F in [
        "iyiyim",
        "iyiyim.",
        "iyiyim!", 
        "fena değilim",
        "fena değilim."
        "fena değilim!"
        "idare eder işte"
        "idare eder işte."
    ]:
        print(f"İyi olmanıza sevindim {A}. Size nasıl yardımcı olabilirim?")

    else:
        print("Hmm... peki.")
