from models.experiment import Experiment
from models import db
from pathlib import Path
import pandas as pd

class AccService:

    @staticmethod
    def get_all(metal=None, ligand=None, kind=None, potentiostat=None):
        query = Experiment.query

        if metal is not None:
            query = query.filter(Experiment.Metal == metal)
        if ligand is not None:
            query = query.filter(Experiment.Ligand == ligand)
        if kind is not None:
            query = query.filter(Experiment.Kind == kind)
        if potentiostat is not None:
            query = query.filter(Experiment.PotentiostatId == potentiostat)

        return query.all()

    @staticmethod
    def read_binary(path: Path) -> bytes:
        with open(path, "rb") as f:
            return f.read()
    
    @staticmethod
    def csv_decode(binary_csv: bytes):
        return pd.read_csv(
            io.BytesIO(binary_csv)
            , names=EXP_CSV_NAMES
    )