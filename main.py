from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Actividad Semana 7 - FastAPI")

# Modelo de datos
class Sesion(BaseModel):
    id: int
    nombre: str
    empresa: str
    tipo: str
    codigo: str
    categoria: str

# Base de datos simulada (lista en memoria)
sesiones = [
    {
        "id": 26,
        "nombre": "TRAVIEZO MIJARES",
        "empresa": "Centro de Masajes Relax",
        "tipo": "Sesión",
        "codigo": "massage_",
        "categoria": "Tipo B"
    }
]

# Obtener todas las sesiones
@app.get("/sesiones")
def obtener_sesiones():
    return sesiones

# Obtener sesión por ID
@app.get("/sesiones/{sesion_id}")
def obtener_sesion(sesion_id: int):
    for sesion in sesiones:
        if sesion["id"] == sesion_id:
            return sesion
    raise HTTPException(status_code=404, detail="Sesión no encontrada")

# Crear nueva sesión
@app.post("/sesiones")
def crear_sesion(sesion: Sesion):
    sesiones.append(sesion.dict())
    return {"mensaje": "Sesión creada con éxito", "data": sesion}

# Actualizar sesión
@app.put("/sesiones/{sesion_id}")
def actualizar_sesion(sesion_id: int, sesion: Sesion):
    for i, s in enumerate(sesiones):
        if s["id"] == sesion_id:
            sesiones[i] = sesion.dict()
            return {"mensaje": "Sesión actualizada con éxito", "data": sesion}
    raise HTTPException(status_code=404, detail="Sesión no encontrada")

# Eliminar sesión
@app.delete("/sesiones/{sesion_id}")
def eliminar_sesion(sesion_id: int):
    for i, s in enumerate(sesiones):
        if s["id"] == sesion_id:
            sesiones.pop(i)
            return {"mensaje": "Sesión eliminada con éxito"}
    raise HTTPException(status_code=404, detail="Sesión no encontrada")
