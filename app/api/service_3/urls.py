from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def index():
    return {'hello': 'service_3'}


@router.get('/test')
async def index():
    return {'test': 'service_3'}