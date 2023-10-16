# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

# ou colocar como pt_BR/en_US na string para deixar no padrão desejado
# podendo mudar a codificação tmb como pt_BR.utf8
locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2023))
print(locale.getlocale())
