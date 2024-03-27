from fastapi import APIRouter, HTTPException, Depends, status, Path, Query

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/availability", status_code=status.HTTP_200_OK)
async def get_products(data=Query(None)):
    print(data)
    return {
    "products":[
    {
        "id": "ABC123",
        "available": True,
        "count": 1,
        "delivery": 0,
        "name": "Diesel Zero Plus Masculine",
        "price": 100.00,
        "related": [
        {
            "title": "Zdarma dárková taška"
        }
        ],
        "priceTotal": 100.00
        },
        {
            "id": "ABC124",
            "available": True,
            "count": 2,
            "delivery": "na dotaz",
            "name": "Mikrovlnná trouba Ariete-Scarlett 933 nerez",
            "price": 200.00,
            "related": [
            {
                "title": "Vynáška do 5. patra zdarma"
            },
            {
                "title": "Propiska zdarma."
            }
            ],
            "priceTotal": 400.00
        }
    ],
    "priceSum": 500.00
}
