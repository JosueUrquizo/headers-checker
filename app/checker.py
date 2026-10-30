"""Analiza cabeceras HTTP de seguridad y calcula un puntaje."""

# nombre de la cabecera (en minúsculas) -> (puntos, por qué importa)
SECURITY_HEADERS = {
    "strict-transport-security": (25, "Fuerza el uso de HTTPS (HSTS)."),
    "content-security-policy": (25, "Limita de dónde se cargan scripts y recursos (CSP)."),
    "x-frame-options": (15, "Protege contra clickjacking."),
    "x-content-type-options": (15, "Evita que el navegador adivine el tipo de contenido."),
    "referrer-policy": (10, "Controla qué información se envía en el Referer."),
    "permissions-policy": (10, "Limita el acceso a funciones del navegador."),
}


def _grade(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    if score >= 40:
        return "D"
    return "F"


def analyze_headers(headers: dict[str, str]) -> dict:
    """Devuelve puntaje, nota, cabeceras presentes y cabeceras faltantes."""
    # Los nombres de cabeceras HTTP no distinguen mayúsculas de minúsculas.
    lowered = {name.lower(): value for name, value in headers.items()}

    present = []
    missing = []
    score = 0

    for name, (points, why) in SECURITY_HEADERS.items():
        if name in lowered:
            present.append({"header": name, "value": lowered[name]})
            score += points
        else:
            missing.append({"header": name, "why_it_matters": why})

    return {
        "score": score,
        "grade": _grade(score),
        "present": present,
        "missing": missing,
    }
