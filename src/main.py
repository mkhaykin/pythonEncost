from datetime import datetime, timedelta

import uvicorn
from asgiref.sync import sync_to_async
from django.db.models import F
from fastapi import FastAPI, Depends

from django_models import EndpointStates
from src.schemas import Schema

app = FastAPI()


@app.get("/")
async def hello() -> dict:
    return {"msg": "hi, use /task"}


def _get_endpoint_states(input_start: datetime):
    u_time = (input_start - timedelta(hours=3)).timestamp()
    return (
        EndpointStates.objects
        .filter(endpoint_id=139, state_start__gte=u_time)
        .order_by('-state_start')
        .filter(id=F('id') - F('id') % 3))


@app.get(
    path="/task",
    summary="Get filtered EndpointStates",
)
async def task(
        start_date: Schema = Depends()
) -> dict:
    items = await sync_to_async(
        _get_endpoint_states,
        thread_sensitive=True,
    )(start_date.input_start)
    result = {
        'filtered_count': len(items),
        'client_info': items[2].client.client_info.info,
        'state_id': items[2].state_id,
    }
    return result


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        workers=1,
    )
