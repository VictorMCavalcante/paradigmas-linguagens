class Configuracao:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls, *args, **kwargs)
        return cls._instancia

config1 = Configuracao()
config2 = Configuracao()
print(config1 is config2)  
