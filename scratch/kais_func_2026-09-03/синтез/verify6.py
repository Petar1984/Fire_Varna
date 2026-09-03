# -*- coding: utf-8 -*-
"""V11: cause of the centroid deviation in the 'регистри' cache."""
import json, sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
gj=json.load(open('C:/git/varna_3d/web/varna_buildings_3d.geojson',encoding='utf-8'))
F={f['properties']['i']:f for f in gj['features']}
closed=0; open_=0
for f in gj['features']:
    r=f['geometry']['coordinates'][0]
    if r[0]==r[-1]: closed+=1
    else: open_+=1
print('пръстени затворени:',closed,'| НЕзатворени:',open_)
r=F[26049]['geometry']['coordinates'][0]
print('i=26049 върхове:',len(r),'| затворен:',r[0]==r[-1])
from shapely.geometry import shape
g=shape(F[26049]['geometry'])
print('shapely centroid (lon,lat):',round(g.centroid.x,6),round(g.centroid.y,6))
# their formula
a=cx=cy=0.0; n=len(r)
for k in range(n-1):
    x1,y1=r[k][0],r[k][1]; x2,y2=r[k+1][0],r[k+1][1]
    cr=x1*y2-x2*y1; a+=cr; cx+=(x1+x2)*cr; cy+=(y1+y2)*cr
print('shoelace-без-затваряне (lon,lat):',round(cx/(3*a),6),round(cy/(3*a),6))
# closed variant
r2 = r if r[0]==r[-1] else r+[r[0]]
a=cx=cy=0.0; n=len(r2)
for k in range(n-1):
    x1,y1=r2[k][0],r2[k][1]; x2,y2=r2[k+1][0],r2[k+1][1]
    cr=x1*y2-x2*y1; a+=cr; cx+=(x1+x2)*cr; cy+=(y1+y2)*cr
print('shoelace-СЪС-затваряне (lon,lat):',round(cx/(3*a),6),round(cy/(3*a),6))
