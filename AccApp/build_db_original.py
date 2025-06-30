import io
import sqlite3
from enum import StrEnum, auto
from pathlib import Path
from typing import NamedTuple, Tuple

import pandas as pd


EXP_CSV_NAMES = ["Time", "Voltage", "Intensity", "Cycle", "Exp"]


class EchemKind(StrEnum):
    CV = auto()
    CDPV = auto()


class DBEntry(NamedTuple):
    metal: int
    ligand: int
    kind: EchemKind
    potentiostat_id: int
    exp_csv: bytes
    image: bytes | None
    

def read_binary(path: Path) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def insert_experiment(entry: DBEntry) -> None:
    conn = sqlite3.connect("chemistry.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO experiments (Metal, Ligand, Kind, PotentiostatId, ExpCSV, Image)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
        ( entry.metal
        , entry.ligand
        , entry.kind
        , entry.potentiostat_id
        , entry.exp_csv
        , entry.image
        )
    )

    conn.commit()
    conn.close()


def entry_from_name(path: Path) -> Tuple:
    splt = path.stem.split("_")

    return (
        int(splt[1])
        , int(splt[3])
        , EchemKind(splt[-3].lower())
        , int(splt[-1][-1])
        , read_binary(path)
    )


def csv_decode(binary_csv: bytes):
    return pd.read_csv(
        io.BytesIO(binary_csv)
        , names=EXP_CSV_NAMES
    )


if __name__ == "__main__":
    conn = sqlite3.connect("chemistry.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS experiments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Metal INTEGER,
        Ligand INTEGER,
        Kind TEXT,
        PotentiostatId INTEGER,
        ExpCSV BLOB,
        Image BLOB
    )
    """)

    conn.commit()
    conn.close()
