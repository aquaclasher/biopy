'''b. Fetch a protein structure from the Protein Data Bank (PDB) using Bio.PDB and visualize the 3D
structure of the protein. Perform basic manipulations like selecting a region or displaying specific
chains.'''

#pip install py3Dmol

from Bio import PDB
from Bio.PDB import PDBList

parser = PDB.PDBParser(QUIET=True)

pdb_id = "1TUP"

pdb_list = PDBList()
pdb_file_path = pdb_list.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')

structure = parser.get_structure("protein", pdb_file_path)

model = structure[0]
chain = model['A']

print(f"Chain {chain.id}:")
for residue in chain:
  print(residue)

io = PDB.PDBIO()
io.set_structure(structure)
io.save("output.pdb")

import os, webbrowser, py3Dmol

view = py3Dmol.view(width=800, height=600)
view.addModel(open('output.pdb', 'r').read(), 'pdb')

view.setStyle({'cartoon': {'color': 'spectrum'}})
view.zoomTo()

html_path = os.path.abspath('output.html')
view.write_html(html_path, fullpage=True)
print(f'3D structure saved to {html_path}')
webbrowser.open(f'file://{html_path}', new=2)