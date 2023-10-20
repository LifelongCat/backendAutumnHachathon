from fastapi import APIRouter


router = APIRouter(
    prefix='',
    tags=['Test']
)


@router.get("/")
async def root():
    return {'data': {'phrase': 'Hello World'}}


@router.post('/test')
def test(age: int, name: str, testing: bool):
    return {'data': {'age': age, 'name': name, 'testing': testing}}
