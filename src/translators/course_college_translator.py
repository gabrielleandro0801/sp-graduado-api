MODALITIES = {
    1: "Presencial",
    2: "EAD"
}

PERIODS = {
    1: "Matutino",
    2: "Vespertino",
    3: "Noturno"
}


def translate_modality(modality: int) -> str:
    return MODALITIES[modality]


def translate_period(period: int) -> str:
    return PERIODS[period]
