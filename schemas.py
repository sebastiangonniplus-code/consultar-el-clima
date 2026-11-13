from pydantic import BaseModel

class ClimaRespuesta(BaseModel):
    ciudad: str
    temperatura: float
    sensacion_termica: float
    humedad: int
    descripcion: str