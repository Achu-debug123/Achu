from flask import Flask, jsonify, request, Response
import subprocess

app = Flask(__name__)

@app.route('/api/images', methods=['GET'])
def get_images():
    try:
        # Get the list of Docker images
        result = subprocess.run(['docker', 'images', '--format', '{{json .}}'], capture_output=True, text=True, check=True)
        images = result.stdout.splitlines()
        images_json = [json.loads(image) for image in images]
        return jsonify(images_json), 200
    except subprocess.CalledProcessError as e:
        return Response(f'Error fetching images: {str(e)}', status=500)

@app.route('/api/containers', methods=['GET'])
def get_containers():
    try:
        # Get the list of Docker containers
        result = subprocess.run(['docker', 'ps', '--format', '{{json .}}'], capture_output=True, text=True, check=True)
        containers = result.stdout.splitlines()
        containers_json = [json.loads(container) for container in containers]
        return jsonify(containers_json), 200
    except subprocess.CalledProcessError as e:
        return Response(f'Error fetching containers: {str(e)}', status=500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)