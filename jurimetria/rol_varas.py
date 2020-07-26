LISTA_NOMES = [
    "1ª Vara Criminal de Belo Horizonte",
    "3ª Vara Criminal de Belo Horizonte",
    "4ª Vara Criminal de Belo Horizonte",
    "5ª Vara Criminal de Belo Horizonte",
    "6ª Vara Criminal de Belo Horizonte",
    "7ª Vara Criminal de Belo Horizonte",
    "8ª Vara Criminal de Belo Horizonte",
    "9ª Vara Criminal de Belo Horizonte",
    "10ª Vara Criminal de Belo Horizonte",
    "11ª Vara Criminal de Belo Horizonte",
    "12ª Vara Criminal de Belo Horizonte",
    "1ª Vara Criminal de Betim",
    "2ª Vara Criminal de Betim",
    "3ª Vara Criminal de Betim",
    "2ª Vara Criminal de Contagem",
    "3ª Vara Criminal de Contagem",
    "4ª Vara Criminal de Contagem",
    "4ª Vara Criminal de Juiz de Fora",
    "1ª Vara Criminal de Montes Claros",
    "1ª Vara Criminal de Ribeirão das Neves",
    "1ª Vara de Tóxicos de Belo Horizonte",
    "2ª Vara de Tóxicos de Belo Horizonte",
    "3ª Vara de Tóxicos de Belo Horizonte",
    "4ª Vara de Tóxicos de Belo Horizonte",
    "1ª Vara Criminal de Uberlândia",
    "2ª Vara Criminal de Uberlândia",
    "4ª Vara Criminal de Uberlândia",
]

LISTA_VARAS = [
    "1", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
    "b1", "b2", "b3", "c2", "c3", "c4", "j4", "m1", "r1", "t1",
    "t2", "t3", "t4", "u1", "u2", "u4"
]

VARAS_NOMES = {
    vara: nome
    for vara, nome in zip(LISTA_VARAS, LISTA_NOMES)
}
