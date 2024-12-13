# vazifa 1
# class SimpleIterator:
#     def __init__(self):
#         self.start = 1
#         self.end = 10
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.end:
#             value = self.start
#             self.start += 1
#             return value
#         else:
#             raise StopIteration
#
# iterator = SimpleIterator()
# for number in iterator:
#     print(number)

# ===================================================================================

# vazifa 2
# users = ["Toxir", "Sobir","Jalil","Bakir"]
#
# iter_user = users.__iter__()
#
# print(iter_user.__next__())
# print(iter_user.__next__())
# print(iter_user.__next__())
# print(iter_user.__next__())

# ===================================================================================

# vazifa 3
# class ReverseIterable:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self.index = len(iterable)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.iterable[self.index]
#
# my_list = [1, 2, 3, 4, 5]
# reverse_iter = ReverseIterable(my_list)
#
# for item in reverse_iter:
#     print(item)

# ===================================================================================

# vazifa 4
# string = "Python"
# iter_string = string.__iter__()
#
# for i in iter_string:
#     print(i)

# ===================================================================================

# vazifa 5
# class JuftSonlar:
#     def __init__(self, num1):
#         self.num1 = num1
#         self.boshlangich_qiymat = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.boshlangich_qiymat <= self.num1:
#             if self.boshlangich_qiymat % 2 == 0:
#                 natija = self.boshlangich_qiymat
#                 self.boshlangich_qiymat += 1
#                 return natija
#             self.boshlangich_qiymat += 1
#         raise StopIteration
#
# num1 = input("Son kiritin: ")
# if num1.isdigit():
#     num1 = int(num1)
#     for i in JuftSonlar(num1):
#         print(i)
#
# else:
#     print("Son kiritin harf emas!!!")

# ===================================================================================

# vazifa 6
# from typing import Iterable
#
# num = [1,2,3,4,5,6,7,8,9,10]
#
# class Calculate:
#     def __init__(self, royxat: Iterable):
#         self.royxat = royxat
#         self.index = 0
#         self.yigindi = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.royxat):
#             raise StopIteration
#         self.yigindi += self.royxat[self.index]
#         self.index += 1
#         return self.yigindi
#
# for i in Calculate(num):
#     print(i)

# ===================================================================================

# vazifa 7
# royxat = ["olma", "banan", "nok", "mandarin", "gilos", "shaftoli"]
#
# royxat_iter = royxat.__iter__()
# search = input("Qaysi mevani qidirmoqchisiz: ")
# if search in royxat_iter:
#     print(f"Siz qidirigan meva: {search}")
# else:
#     print("siz qidirgan meva topilmadi!!!")

# =========Generatorlarga oid vazufalar=========

# vazifa 1
# def my_range(start, stop, step=1):
#     current = start
#     while current < stop:
#         yield current
#         current += step
#
# for num in my_range(0, 10, 2):
#     print(num)

# ===================================================================================

# vazifa 2
# def soz_uzunligi(matn):
#     for soz in matn.split():
#         yield len(soz)
#
# text = input("matn kiritin: ")
# for uzunlik in soz_uzunligi(text):
#     print(uzunlik)

# ===================================================================================

# vazifa 3
# def toq_sonlar(start, stop):
#     for num in range(start, stop):
#         if num % 2 == 1:
#             yield num
#
# num = input("Son kiritin: ")
# if num.isdigit():
#     num = int(num)
#     for toq in toq_sonlar(1, num):
#         print(toq)
# else:
#     print("son kiritin harf emas!!!")

# ===================================================================================

# vazifa 4
# def toq_sonlar(start, stop):
#     for num in range(start, stop):
#         if num % 2 == 0:
#             yield num
#
# num = input("Son kiritin: ")
# if num.isdigit():
#     num = int(num)
#     for juft in toq_sonlar(1, num):
#         print(juft)
# else:
#     print("son kiritin harf emas!!!")

# ===================================================================================

# vazifa 5
# import time
# def generator():
#     a = 0
#     while True:
#         a += 1
#         time.sleep(0.1)
#         yield a
#
# for i in generator():
#     print(i)

# ===================================================================================

# vazifa 6
# def kvadrat_sonlar(start, stop):
#     for num in range(start, stop):
#         yield num ** 2
#
# num = input("Son kiritin: ")
# if  num.isdigit():
#     num =int(num)
#     for kvadrat in kvadrat_sonlar(1, num + 1):
#         print(kvadrat)
# else:
#     print("Son kiritin harf emas!!!")

# ===================================================================================

# vazifa 7
# def yigindi_generator(ketma_ketlik):
#     yigindi = 0
#     for son in ketma_ketlik:
#         yigindi += son
#         yield yigindi
#
# num = [1,2,3,4,5,6,7,8,9,10]
# for yigindi in yigindi_generator(num):
#     print(yigindi)

# ===================================================================================

# vazifa 8
# def ijobiy_sonlar(*raqamlar):
#     for raqam in raqamlar:
#         if raqam > 0:
#             yield raqam
#
# raqamlar = [-5, 3, 0, 7, -2, 4]
# for son in ijobiy_sonlar(*raqamlar):
#     print(son)

# ===================================================================================

# vazifa 9
# import random
#
# def tasodifiy_sonlar(min_val, max_val, n):
#     for _ in range(n):
#         yield random.randint(min_val, max_val)
#
# for son in tasodifiy_sonlar(1, 100, 5):
#     print(son)

# ===================================================================================

# vazifa 10
# def tub_sonlar(N):
#     def is_tub(son):
#         if son < 2:
#             return False
#         for i in range(2, int(son ** 0.5) + 1):
#             if son % i == 0:
#                 return False
#         return True
#
#     son = 2
#     count = 0
#     while count < N:
#         if is_tub(son):
#             yield son
#             count += 1
#         son += 1
#
# for son in tub_sonlar(10):
#     print(son)

# ===================================================================================

# vazifa 11
# def teskari_matn(matn):
#     for harf in reversed(matn):
#         yield harf
#
# matn = input("Matn kiritin: ")
# for harf in teskari_matn(matn):
#     print(harf, end="")

# ===================================================================================

# vazifa 12
# def kopaytma(N):
#     result = 1
#     for son in range(1, N + 1):
#         result *= son
#         yield result
#
# for natija in kopaytma(5):
#     print(natija)

