from fastapi import APIRouter
from app.services import stack_service

router = APIRouter()

@router.get("/answered")
def answered():
    return stack_service.get_answered_stats()


@router.get("/max-reputation")
def max_rep():
    return stack_service.get_max_reputation()


@router.get("/min-views")
def min_views():
    return stack_service.get_min_views()


@router.get("/oldest")
def oldest():
    return stack_service.get_oldest()


@router.get("/newest")
def newest():
    return stack_service.get_newest()