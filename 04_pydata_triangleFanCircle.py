
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


def radial2rectangularX( radius , angle ) :
	return round( radius * cos( radians ( angle ) ) , 2)

def radial2rectangularY( rad , angle ) :
	return round( radius * sin( radians ( angle ) ) , 2)

def setPointXY0( idx , verts , radius , angle ) :
	verts[idx][0] = radial2rectangularX( radius , angle )
	verts[idx][1] = radial2rectangularY( radius , angle )
	verts[idx][2] = 0

def setVerts4triangleFanCircle( verts , vertsLen , radius , angle ) :

	verts[0] = [ 0.0 , 0.0 , 0.0 ]

	nextAngle = angle
	idx = 1
	lim = vertsLen

	while idx < lim :
		#print( "angle: " , nextAngle)
		setPointXY0( idx , verts , radius , nextAngle )
		nextAngle += angle
		idx += 1

def setFaces4triangleFanCircle( faces , facesLen ) :
	idx = 0
	lim = facesLen - 1

	while idx < lim :

		faces[idx][0] = 0
		faces[idx][1] = idx + 1
		faces[idx][2] = idx + 2

		idx += 1
	
	faces[idx][0] = 0
	faces[idx][1] = idx + 1
	faces[idx][2] = 1

#
# circle radius
radius = 15

# circle by divisions
divisions = 8
angle = 360 / divisions # 360 / 8 = 45 deg

# cicle by division length in angle degrees
angle = 5
divisions = 360 / angle

vertsDim = 3 # x , y , z

vertsLen = int ( divisions + 1 ) # 9: 0,1...8

verts = np.zeros( ( vertsLen , vertsDim ) , dtype = float )

setVerts4triangleFanCircle( verts , vertsLen , radius , angle )


#
facesDim = 3 # 3 vert triangles - not 4 vert quads
facesLen = int( divisions )
faces = np.zeros( ( facesLen , facesDim ) , dtype = int )


setFaces4triangleFanCircle( faces, facesLen )

#printArray( 0 , vertsLen , verts )
#printArray( 0 , facesLen , faces )


#
makeMeshByNameVertsAndFaces ( "mesh01" , verts , faces )

#setVertZ( 0 , vertsLen , verts , 1.0 )
#makeMeshByNameVertsAndFaces ( "mesh02" , verts , faces )



