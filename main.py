from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4, UUID
from pathlib import Path
import json

app = FastAPI(title="Events API")


class Event(BaseModel):
    title: str
    description: str
    location: str
    starts_at: datetime
    ends_at: datetime


class EventResponse(Event):
    id: UUID


# In-memory store seeded from events.json
def _load_events() -> dict[UUID, EventResponse]:
    path = Path(__file__).parent / "events.json"
    data = json.loads(path.read_text())
    return {UUID(e["id"]): EventResponse(**e) for e in data}


events: dict[UUID, EventResponse] = _load_events()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/events", response_model=list[EventResponse])
def list_events():
    return list(events.values())


@app.post("/events", response_model=EventResponse, status_code=201)
def create_event(event: Event):
    new_event = EventResponse(id=uuid4(), **event.model_dump())
    events[new_event.id] = new_event
    return new_event


@app.get("/events/{event_id}", response_model=EventResponse)
def get_event(event_id: UUID):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    return events[event_id]


@app.put("/events/{event_id}", response_model=EventResponse)
def update_event(event_id: UUID, event: Event):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    updated = EventResponse(id=event_id, **event.model_dump())
    events[event_id] = updated
    return updated


@app.delete("/events/{event_id}", status_code=204)
def delete_event(event_id: UUID):
    if event_id not in events:
        raise HTTPException(status_code=404, detail="Event not found")
    del events[event_id]


handler = Mangum(app)
