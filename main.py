class Arxitektor:
    def __init__(self, ismi, tajriba):
        self.ismi = ismi
        self.tajriba = tajriba

    def __getitem__(self, key):
        if key == 'ismi':
            return self.ismi
        elif key == 'tajriba':
            return self.tajriba
        else:
            raise KeyError(f"Klasterda '{key}' kiritilmagan")

arxitektor = Arxitektor('Google va Meta', 'Arxitektor-dasturchi')

print(arxitektor['ismi'])  # Google va Meta
print(arxitektor['tajriba'])  # Arxitektor-dasturchi
try:
    print(arxitektor['yosh'])
except KeyError as e:
    print(e)  # Klasterda 'yosh' kiritilmagan
