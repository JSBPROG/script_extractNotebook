import json
import argparse


parser = argparse.ArgumentParser(description="Extraer el código de un archivo Jupyter Notebook (.ipynb).")
parser.add_argument('notebook_name', help="Nombre del archivo Jupyter Notebook sin extensión ni './'")


args = parser.parse_args()


notebook_path = f"./{args.notebook_name}.ipynb"


with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)


code_cells = [cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']


all_code = "\n\n".join("".join(cell) for cell in code_cells)


with open(f"{args.notebook_name}_extraido.py", 'w', encoding='utf-8') as f:
    f.write(all_code)

print(f"Código extraído con éxito y guardado en '{args.notebook_name}_extraido.py'.")
