"""Generate millimetre STL rib prototypes, cutting templates, and validation.

Run: python -m pip install -r requirements.txt && python generate.py
No CAD application needed. Outputs are beside this script.
"""
from pathlib import Path
import json
import math
import numpy as np
import trimesh
from shapely.geometry import Polygon, Point
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
FINISHED_RADIUS = 304.8  # 24-inch outside diameter / 2
FOAM = 12.7
RO = FINISHED_RADIUS - FOAM
DEPTH = 20.0
RI = RO - DEPTH
RM = (RI + RO) / 2
THICKNESS = 8.0
PLATE_THICKNESS = 3.0
BOLT_D = 4.5  # nominal clearance for M4; test printed fit

def xy(r, deg):
    a = math.radians(deg)
    return (r * math.cos(a), r * math.sin(a))

def profile(span, holes, inset=0):
    angles = np.linspace(-span/2, span/2, int(span*4)+1)
    p = Polygon([xy(RO-inset, a) for a in angles] +
                [xy(RI+inset, a) for a in angles[::-1]])
    for a, d in holes:
        p = p.difference(Point(xy(RM, a)).buffer(d/2, quad_segs=12))
    assert p.is_valid and p.geom_type == 'Polygon'
    return p

RIB_HOLES = [(a, BOLT_D) for a in (-18.5,-14.5,14.5,18.5)] + [(a,3.5) for a in (-7.5,0,7.5)]
PLATE_HOLES = [(a, BOLT_D) for a in (-8,-4,4,8)]
rib = profile(45, RIB_HOLES)
plate = profile(22, PLATE_HOLES, inset=0.5)

def solid(p, h):
    m = trimesh.creation.extrude_polygon(p, h, engine='earcut')
    m.remove_unreferenced_vertices()
    m.fix_normals()
    return m

def bed_center(m):
    m = m.copy()
    m.apply_translation([-m.bounds[:,0].mean(), -m.bounds[:,1].mean(), -m.bounds[0,2]])
    return m

def svg_template(p, name, description):
    # Full-size SVG; 5mm margin. No fit-to-page scaling.
    x0,y0,x1,y1 = p.bounds
    w,h=x1-x0+10,y1-y0+30
    def path(ring):
        pts=[(x-x0+5,y1-y+5) for x,y in ring.coords]
        return 'M '+' L '.join(f'{x:.4f},{y:.4f}' for x,y in pts)+' Z'
    d=' '.join(path(r) for r in [p.exterior,*p.interiors])
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w:.4f}mm" height="{h:.4f}mm" viewBox="0 0 {w:.4f} {h:.4f}">
<title>{description}</title><path d="{d}" fill="none" stroke="black" stroke-width="0.2"/>
<path d="M 5,{h-12} h 25.4 m -25.4,-2 v 4 m 25.4,-4 v 4" stroke="black" fill="none" stroke-width="0.3"/>
<text x="5" y="{h-4}" font-size="3">1 inch / 25.4 mm — print at 100%</text></svg>'''
    (OUT/name).write_text(s)

report={}
def export(name, mesh, components=1):
    # Re-import the actual serialized file, not just the source mesh.
    mesh.export(OUT/name)
    check=trimesh.load_mesh(OUT/name)
    assert check.is_watertight and check.is_winding_consistent and check.volume > 0
    assert len(check.split()) == components
    # Every undirected edge must have exactly two incident faces.
    assert np.all(np.bincount(check.edges_unique_inverse)==2)
    assert np.min(check.area_faces)>1e-9
    assert check.extents[0] < 240 and check.extents[1] < 240
    assert abs(check.bounds[0,2])<1e-5
    report[name]={'bounds_mm':check.extents.round(3).tolist(),
                  'volume_cm3':round(check.volume/1000,3),
                  'watertight':bool(check.is_watertight),'components':components,
                  'triangles':len(check.faces)}

mr=solid(rib,THICKNESS)
mp=solid(plate,PLATE_THICKNESS)
export('rib-45deg.stl',bed_center(mr))
export('splice-plate.stl',bed_center(mp))

# Arrange 2 ribs and 2 splice plates as separate objects in one STL.
parts=[]
for mesh,x,y in [(mr,-65,0),(mr,-12,0),(mp,45,-60),(mp,45,60)]:
    m=bed_center(mesh); m.apply_translation([x,y,0]); parts.append(m)
kit=bed_center(trimesh.util.concatenate(parts))
export('one-rib-kit.stl',kit,4)

# Check intended assembly: rib centers are +/-22.5deg about the splice.
def rotation(a):
    return trimesh.transformations.rotation_matrix(math.radians(a),[0,0,1])
for center, hole_angles, targets in [(-22.5,[14.5,18.5],[-8,-4]),(22.5,[-18.5,-14.5],[4,8])]:
    for angle,target in zip(hole_angles,targets):
        assert np.linalg.norm(np.array(xy(RM,center+angle))-xy(RM,target))<1e-8
expected_area=0.5*(RO**2-RI**2)*math.pi/4-sum(math.pi*(d/2)**2 for a,d in RIB_HOLES)
assert abs(mr.volume-expected_area*THICKNESS)/(expected_area*THICKNESS)<0.001
report['assembly']={'outer_radius_mm':RO,'foam_mm':FOAM,'finished_diameter_mm':2*(RO+FOAM),
                    'rib_arc_degrees':90,'joint_bolts':4,'hole_diameter_mm':BOLT_D,
                    'joint_stack_mm':THICKNESS+2*PLATE_THICKNESS,
                    'holes_align':True,'physical_fit_tested':False,'sliced':False}
(OUT/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
svg_template(rib,'rib-45deg-template.svg','45 degree rib, full scale, millimetres')
svg_template(plate,'splice-template.svg','22 degree splice plate, full scale, millimetres')

# Human-readable preview: bed arrangement and assembled quarter rib.
fig,axs=plt.subplots(1,2,figsize=(12,6),facecolor='#f4f4f0')
ax=axs[0]
for m in parts:
    p=rib if m.extents[2]>4 else plate
    verts=np.array(p.exterior.coords)
    verts += m.bounds[:,:2].mean(axis=0)-np.array(p.bounds).reshape(2,2).mean(axis=0)
    ax.fill(verts[:,0],verts[:,1],alpha=.25,color='#157f83')
    # Mesh top-edge outlines, including holes.
    for loop in m.section(plane_origin=[0,0,1],plane_normal=[0,0,1]).discrete:
        ax.plot(loop[:,0],loop[:,1],color='#14575a',lw=.5)
ax.set_title('Print flat: 2 rib segments + 2 splice plates')
ax.set_xlim(-128,128);ax.set_ylim(-128,128);ax.set_aspect('equal');ax.grid(alpha=.2)
ax.set_xlabel('mm');ax.set_ylabel('mm')
ax=axs[1]
for center,c in [(-22.5,'#16878a'),(22.5,'#efaa4b')]:
    a=math.radians(center); R=np.array([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]])
    pts=np.array(rib.exterior.coords)@R.T
    ax.fill(pts[:,0],pts[:,1],color=c,alpha=.9)
    for ang,d in RIB_HOLES:
        pos=xy(RM,ang+center);ax.add_patch(plt.Circle(pos,d/2,color='white'))
pts=np.array(plate.exterior.coords)
ax.fill(pts[:,0],pts[:,1],color='#333333',alpha=.55)
for a,d in PLATE_HOLES:
    x,y=xy(RM,a);ax.plot(x,y,'o',color='white',ms=3)
ax.annotate('Two plates sandwich the joint\n4 x M4 bolts',xy=(RM,0),xytext=(40,30),arrowprops={'arrowstyle':'->'})
ax.plot([0,RO/math.sqrt(2)],[0,RO/math.sqrt(2)],'--',color='#999',lw=.8)
ax.plot([0,RO/math.sqrt(2)],[0,-RO/math.sqrt(2)],'--',color='#999',lw=.8)
ax.set_title('Assembled: one 90° meridian rib')
ax.set_aspect('equal');ax.set_xlim(0,330);ax.set_ylim(-230,230);ax.axis('off')
fig.suptitle('Xanathar — rib prototype v1 | R = 292.1 mm + 12.7 mm foam',fontsize=14)
fig.tight_layout();fig.savefig(OUT/'preview.png',dpi=140);plt.close(fig)
print(json.dumps(report,indent=2))
