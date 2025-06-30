from  models import db

# An ORM tool like SQLAlchemy translates Python classes to database tables 
# and automatically converts function calls to SQL statements.

class Experiment(db.Model):
    __tablename__ = 'experiments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Metal = db.Column(db.Integer, nullable=False)
    Ligand = db.Column(db.Integer, nullable=False)
    Kind = db.Column(db.String(20), nullable=False)  # Stores string like "CV", "CDPV"
    PotentiostatId = db.Column(db.Integer, nullable=False)
    ExpCSV = db.Column(db.LargeBinary, nullable=False)  # CSV bytes
    Image = db.Column(db.LargeBinary, nullable=True)    # PNG image or similar (optional)

    def __init__(self, Metal, Ligand, Kind, PotentiostatId, ExpCSV, Image=None):
        self.Metal = Metal
        self.Ligand = Ligand
        self.Kind = Kind  # string (e.g., "CV")
        self.PotentiostatId = PotentiostatId
        self.ExpCSV = ExpCSV
        self.Image = Image

   
