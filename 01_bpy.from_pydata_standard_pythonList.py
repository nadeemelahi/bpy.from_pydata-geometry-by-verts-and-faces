
#
# author: Nadeem Elahi
# nadeem.elahi@gmail.com
# nad@3deem.com
# license: gpl v3
#

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

def makeMeshByNameVertsAndFaces ( name , verts , faces ) :

	mesh = bpy.data.meshes.new ( name )
	mesh.from_pydata ( verts , [] , faces )
	obj = bpy.data.objects.new ( name , mesh )
	bpy.context.scene.collection.objects.link ( obj )




#
def printVerts ( vertices ) :
	idx = 0
	lim = len ( vertices ) 

	while idx < lim :

		print ( idx , ":" , vertices[idx][0] , vertices[idx][1] , vertices[idx][2]  )

		idx += 1


		
# 
def setVertZ ( vertices , zloc ) :

	idx = 0
	lim = len ( vertices ) 

	while idx < lim :

		#vertices[idx][2] = zloc # error TypeError: 'tuple' object does not support assignment
		vertices[idx] = ( vertices[idx][0] , vertices[idx][1] , zloc )

		idx += 1



#
name = "mesh"

verts = [
		(  0.0 ,  0.0 , 0.0 ) ,
		(  1.0 ,  0.0 , 0.0 ) ,
		(  0.0 ,  1.0 , 0.0 ) ,
		
		]



faces = [ 
		( 0 , 1 , 2 )  

		]


makeMeshByNameVertsAndFaces ( "mesh01" , verts , faces )

setVertZ( verts , 1.0 )
makeMeshByNameVertsAndFaces ( "mesh02" , verts , faces )



