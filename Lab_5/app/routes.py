from flask import Blueprint, request, jsonify
from .forms import CodeExecutionForm
from subprocess import Popen, PIPE, TimeoutExpired

bp = Blueprint('routes', __name__)

@bp.route('/execute', methods=['POST'])
def execute_code():
    form = CodeExecutionForm()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        command = ['prlimit', '--nproc=1:1', 'python3', '-c', code]
        try:
            process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
            stdout, stderr = process.communicate(timeout=timeout)
            return jsonify({'stdout': stdout, 'stderr': stderr})
        except TimeoutExpired:
            process.kill()
            return jsonify({'error': 'Execution timed out'}), 408
    return jsonify({'errors': form.errors}), 400
