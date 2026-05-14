'''b. Fetch a protein structure from the Protein Data Bank (PDB) using Bio.PDB and visualize the 3D
structure of the protein. Perform basic manipulations like selecting a region or displaying specific
chains.'''

# Please run pip install py3Dmol

from Bio import PDB
from Bio.PDB import PDBList

# Step 1: Create a PDB parser
parser = PDB.PDBParser(QUIET=True)

# Step 2: Fetch a protein structure from the PDB (using a known PDB ID)
pdb_id = "1TUP" # Example PDB ID for a protein structure

pdb_list = PDBList()
# Download the PDB file. By default, it downloads to './pdb<PDB_ID>.ent'
# The function returns the path to the downloaded file.
pdb_file_path = pdb_list.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')

structure = parser.get_structure("protein", pdb_file_path)

# Step 3: Visualize and manipulate the structure

model = structure[0] # Get the first model (if there are multiple)
chain = model['A'] # Select chain 'A'
# Step 4: Print out information about the selected chain
print(f"Chain {chain.id}:")
for residue in chain:
  print(residue)
# Step 5: Display the structure (this requires an external visualization tool like PyMOL or Chimera)
# You can save the structure for visualization in an external tool:
io = PDB.PDBIO()
io.set_structure(structure)
io.save("output.pdb")

import os
import webbrowser
import py3Dmol

# Create a 3D viewer object
view = py3Dmol.view(width=800, height=600)

# Add the PDB structure from the 'output.pdb' file
view.addModel(open('output.pdb', 'r').read(), 'pdb')

# Apply a style to the protein structure (e.g., cartoon representation)
view.setStyle({'cartoon': {'color': 'spectrum'}})

# Zoom to fit the entire structure
view.zoomTo()

# Save the viewer to an HTML file so it can be opened in a browser
html_path = os.path.abspath('output.html')
view.write_html(html_path, fullpage=True)
print(f'3D structure saved to {html_path}')
webbrowser.open(f'file://{html_path}', new=2)