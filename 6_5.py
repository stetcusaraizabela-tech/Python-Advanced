import warnings
warnings.warn("Das könnte ein Problem machen", UserWarning)

warnings.simplefilter("always", UserWarning)
warnings.warn("Diese warnung wird immer angezeigt", UserWarning)

warnings.simplefilter("error", UserWarning)

try:
    warnings.warn("Das ist jetzt wie ein Fehler", UserWarning)
except UserWarning:
    print("warnung wurde aöls fehler behandelt")

warnings.warn("Das ist ein Fehler", UserWarning) 