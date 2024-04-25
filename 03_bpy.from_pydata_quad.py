
#
# author: Nadeem Elahi
# nadeem.elahi@gmail.com
# nad@3deem.com
# license: gpl v3
#

import numpy as np
import bpy
from math import sin
from math import cos
from math import atan 
from math import radians
from math import sqrt




def fullReset() :
	#https://blenderartists.org/t/deleting-all-from-scene/1296469
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete(use_global=False)

	bpy.ops.outliner.orphans_purge()
	bpy.ops.outliner.orphans_purge()
	bpy.ops.outliner.orphans_purge()


fullReset()

def makeMeshByNameVertsAndFaces( name , verts , faces ) :

	mesh = bpy.data.meshes.new ( name )
	mesh.from_pydata ( verts , [] , faces )
	obj = bpy.data.objects.new ( name , mesh )
	bpy.context.scene.collection.objects.link ( obj )




#
def printArray( start , lim , vertices ) :
	idx = start  

	while idx < lim :

		print ( idx , ":" , vertices[idx][0] , vertices[idx][1] , vertices[idx][2]  )

		idx += 1


		
# 
def setVertZ( start , lim , vertices , zloc ) :

	idx = start

	while idx < lim :

		vertices[idx][2] = zloc 

		idx += 1



#
vertsDim = 3 # x , y , z
vertsLen = 4
verts = np.zeros( ( vertsLen , vertsDim ) , dtype = float )

verts[0] = [ 0.0 ,  0.0 , 0.0 ] 
verts[1] = [ 1.0 ,  0.0 , 0.0 ] 
verts[2] = [ 1.0 ,  1.0 , 0.0 ] 
verts[3] = [ 0.0 ,  1.0 , 0.0 ] 

printArray( 0 , vertsLen , verts )


#
facesDim = 4 # 3 vert triangles - not 4 vert quads
facesLen = 1
faces = np.zeros( ( facesLen , facesDim ) , dtype = int )

faces[0] = [ 0 , 1 , 2 , 3 ]

printArray( 0 , facesLen , faces )


#
makeMeshByNameVertsAndFaces ( "mesh01" , verts , faces )

setVertZ( 0 , vertsLen , verts , 1.0 )
makeMeshByNameVertsAndFaces ( "mesh02" , verts , faces )



