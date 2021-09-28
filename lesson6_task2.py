a = input("Введіть слово: ")

def is_palindrome(a):
  if a[::1] == a[::-1]:
    print(True)
  else:
    print(False)

is_palindrome(a)
