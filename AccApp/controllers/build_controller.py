from flask import Blueprint, render_template, request
from services.acc_services import AccService


build_controller = Blueprint('build', __name__)


@build_controller.route('/', methods=['GET'])
def get_results():
    # Extract the filter parameters from the request
    metal = request.args.get('metal', type=int)
    ligand = request.args.get('ligand', type=int)
    kind = request.args.get('kind')
    potentiostat = request.args.get('potentiostat', type=int)

    # Use the AccService to filter the experiments based on provided parameters
    experiments = AccService.get_all(metal=metal, ligand=ligand, kind=kind, potentiostat=potentiostat)
    print("Filtered experiments:")
    print(experiments)

    # Render the results page and pass the filtered experiments
    return render_template('experiment.html', experiments=experiments)

