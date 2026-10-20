"""
Investigation of IEEE 754 floating-point precision and error accumulation
in computational physics simulations.
"""
import math

# 1. Bellekteki Gerçek Değerler (20 basamak duyarlık)
a: float = 0.1
b: float = 0.2
c: float = a + b

print("--- Deney 1: Ondalık Temsil ve IEEE 754 ---")
print(f"a (0.1)                     : {a:.20f}")
print(f"b (0.2)                     : {b:.20f}")
print(f"c (0.1 + 0.2)               : {c:.20f}")
print(f"Doğrudan beklenen (0.3)     : {0.3:.20f}")
print(f"Doğrudan eşitlik (c == 0.3) : {c == 0.3}")
print(f"math.isclose(c, 0.3)        : {math.isclose(c, 0.3)}")

# 2. Fiziksel Simülasyonda Hata Birikimi (Time-stepping Drift)
# dt = 0.1 saniye adımla 1000 adım ilerleyelim (Teorik beklenen: 100.0 s)
dt: float = 0.1
total_steps: int = 1000

# Yöntem A: Her adımda dt ekleme (Hata adım adım birikir)
t_accumulated: float = 0.0
for _ in range(total_steps):
    t_accumulated += dt

# Yöntem B: Adım sayısı ile doğrudan çarpma (Hata birikmez)
t_exact: float = total_steps * dt

print("\n--- Deney 2: Simülasyon Zamanı Sapması (1000 Adım) ---")
print(f"Birikimli zaman (t += dt)   : {t_accumulated:.17f}")
print(f"Çarpımsal zaman (n * dt)    : {t_exact:.17f}")
print(f"Oluşan zaman sapması (drift): {t_accumulated - t_exact}")