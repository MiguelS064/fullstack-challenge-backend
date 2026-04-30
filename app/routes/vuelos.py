from fastapi import APIRouter
from app.services import vuelos_service

router = APIRouter()

@router.get("/top-aeropuerto")
def top_aeropuerto():
    return vuelos_service.top_aeropuerto()


@router.get("/top-aerolinea")
def top_aerolinea():
    return vuelos_service.top_aerolinea()


@router.get("/top-dia")
def top_dia():
    return vuelos_service.top_dia()


@router.get("/aerolineas-mas-2")
def aerolineas_mas_2():
    return vuelos_service.aerolineas_mas_2()