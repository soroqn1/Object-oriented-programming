
from __future__ import annotations
import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import TypeVar, Generic, List, Optional, Callable, Type
from uuid import UUID

from .repository import IRepository

T = TypeVar("T")

def _default(o):
    if isinstance(o, datetime):
        return {"__dt__": True, "v": o.isoformat()}
    if isinstance(o, UUID):
        return {"__uuid__": True, "v": str(o)}
    raise TypeError(f"Not JSON serializable: {type(o)}")

def _object_hook(d):
    if "__dt__" in d:
        return datetime.fromisoformat(d["v"])
    if "__uuid__" in d:
        return UUID(d["v"])
    return d

class JsonRepository(Generic[T], IRepository[T]):
    def __init__(self, data_dir: Path, model: Type[T]):
        self.data_dir = data_dir
        self.model = model
        self.file = data_dir / f"{model.__name__.lower()}.json"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        if not self.file.exists():
            self._write([])

    def _read(self) -> List[dict]:
        if not self.file.exists():
            return []
        return json.loads(self.file.read_text(encoding="utf-8"))

    def _write(self, rows: List[dict]) -> None:
        self.file.write_text(json.dumps(rows, ensure_ascii=False, indent=2, default=_default), encoding="utf-8")

    def add(self, entity: T) -> T:
        rows = self._read()
        rows.append(asdict(entity) if is_dataclass(entity) else entity.__dict__)
        self._write(rows)
        return entity

    def get(self, id: UUID) -> Optional[T]:
        id_str = str(id)
        for row in self._read():
            row_id = row.get("id")
            row_id_str = row_id.get("v") if isinstance(row_id, dict) and "v" in row_id else str(row_id)
            if row_id_str == id_str:
                obj = json.loads(json.dumps(row), object_hook=_object_hook)
                return self.model(**obj)  # type: ignore[arg-type]
        return None

    def get_all(self) -> List[T]:
        res: List[T] = []
        for row in self._read():
            obj = json.loads(json.dumps(row), object_hook=_object_hook)
            res.append(self.model(**obj))  # type: ignore[arg-type]
        return res

    def update(self, entity: T) -> None:
        rows = self._read()
        target_id = str(getattr(entity, "id"))
        for i, row in enumerate(rows):
            row_id = row.get("id")
            row_id_str = row_id.get("v") if isinstance(row_id, dict) and "v" in row_id else str(row_id)
            if row_id_str == target_id:
                rows[i] = asdict(entity)
                self._write(rows)
                return
        raise KeyError("Entity to update not found")

    def delete(self, id: UUID) -> None:
        rows = self._read()
        id_str = str(id)
        def _row_id_str(r):
            v = r.get("id")
            return v.get("v") if isinstance(v, dict) and "v" in v else str(v)
        new_rows = [r for r in rows if _row_id_str(r) != id_str]
        self._write(new_rows)

    def find(self, predicate: Callable[[T], bool]) -> List[T]:
        return [e for e in self.get_all() if predicate(e)]
