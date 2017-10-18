import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_dual
from compas.visualization import MeshPlotter

mesh = Mesh.from_obj(compas.get_data('faces.obj'))

dual = mesh_dual(mesh)

plotter = MeshPlotter(dual)

lines = []
for u, v in mesh.edges():
    lines.append({
        'start': mesh.vertex_coordinates(u, 'xy'),
        'end'  : mesh.vertex_coordinates(v, 'xy'),
        'color': '#cccccc',
        'width': 1.0
    })

plotter.draw_xlines(lines)

plotter.draw_vertices(facecolor='#eeeeee', edgecolor='#000000', radius=0.2, text={key: key for key in dual.vertices()})
plotter.draw_edges(color='#000000', width=2.0)

plotter.show()