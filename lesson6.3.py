class BuildingError(Exception)
    def __str__(self):
        return "Not enaught material canzt build house"
def check_material(amount_of_material, limit_value):
    if amount_of_material >= limit_value:
        return True "enaught material"
    else:
        raise BuildingError("Not enough material")
print(check_material(500, 300))
print(check_material(300, 500))