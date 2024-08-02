import os
import subprocess
from datetime import datetime, timedelta
import random
import git

def create_many_commits(repo_path):
    # Verificar si la ruta del repositorio es válida
    if not os.path.isdir(repo_path):
        print(f"Error: La ruta '{repo_path}' no es válida.")
        return

    # Cambiar al directorio del repositorio
    os.chdir(repo_path)

    # Inicializar el repositorio
    repo = git.Repo(repo_path)

    # Generar un número aleatorio de commits (entre 200 y 300)
    num_commits = random.randint(200, 300)

    for i in range(num_commits):
        # Generar una fecha y hora aleatoria en el pasado reciente
        days_ago = random.randint(0, 365)  # Hasta un año atrás
        random_date = datetime.now() - timedelta(days=days_ago)
        commit_date_str = random_date.strftime('%Y-%m-%dT%H:%M:%S')

        # Crear un archivo temporal con contenido aleatorio para el commit
        file_name = f'temp_commit_{i}.txt'
        random_content = f'Commit {i} on {commit_date_str} with random content {random.randint(1, 1000)}'
        with open(file_name, 'w') as f:
            f.write(random_content)

        # Agregar el archivo al índice
        repo.index.add([file_name])
        repo.index.write()

        # Establecer las fechas de autor y committer
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = commit_date_str
        env['GIT_COMMITTER_DATE'] = commit_date_str

        # Realizar el commit usando subprocess para establecer el entorno
        subprocess.run(['git', 'commit', '-m', f'Commit {i} on {commit_date_str}'], env=env, check=True)

        # Eliminar el archivo temporal
        os.remove(file_name)

    # Hacer push de los commits al repositorio remoto
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)

    print(f'Created {num_commits} random commits in {repo_path}.')

# Parámetros para el ejemplo
repo_path = r'C:\Users\namee\Downloads\test\test'  # Aplica tu ruta de tu ordenador

# Crear muchos commits aleatorios   
create_many_commits(repo_path)
