
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
def print3Darray( start , lim , arr ) :
	idx = start  

	while idx < lim :

		print ( idx , ":" , arr[idx][0] , arr[idx][1] , arr[idx][2]  )

		idx += 1
#
def print4Darray( start , lim , arr ) :
	idx = start  

	while idx < lim :

		print ( idx , ":" , arr[idx][0] , arr[idx][1] , arr[idx][2] , arr[idx][3] )

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

def setVerts4triangleFanCircleDisc( verts , start , lim , radius , angle ) :

	nextAngle = angle
	idx = start  

	while idx < lim :
		#print( "angle: " , nextAngle)
		setPointXY0( idx , verts , radius , nextAngle )
		nextAngle += angle
		idx += 1

def setFaces4triangleFanCircleDisc( faces , facesLen ) :
	# facesLen = divisions for a circle disc - see diagram

	idx = 0
	lim = facesLen - 1

	while idx < lim :

		faces[idx][0] = idx
		faces[idx][1] = idx + facesLen
		faces[idx][2] = idx + facesLen + 1
		faces[idx][3] = idx + 1

		idx += 1
	
	faces[idx][0] = idx
	faces[idx][1] = idx + facesLen
	faces[idx][2] = facesLen
	faces[idx][3] = 0


# circle by divisions
divisions = 24 
angle = 360 / divisions # 360 / 8 = 45 deg

# cicle by division length in angle degrees
#angle = 45
#divisions = 360 / angle

vertsDim = 3 # x , y , z

vertsLen = int ( divisions * 2 ) 

verts = np.zeros( ( vertsLen , vertsDim ) , dtype = float )

radius = 5
start = 0 
lim = divisions # 0 , 1 , 2 , 3
setVerts4triangleFanCircleDisc( verts , start , lim , radius , angle )

radius = 7
start = int( divisions )
lim = vertsLen # 4 , 5 , 6 , 7
setVerts4triangleFanCircleDisc( verts , start , lim , radius , angle )

#
facesDim = 4 # 3 vert triangles - 4 vert quads
facesLen = int( divisions )
faces = np.zeros( ( facesLen , facesDim ) , dtype = int )

setFaces4triangleFanCircleDisc( faces, facesLen )
#print4Darray( 0 , facesLen , faces)


makeMeshByNameVertsAndFaces ( "mesh01" , verts , faces )




#setVertZ( 0 , vertsLen , verts , 1.0 )
#makeMeshByNameVertsAndFaces ( "mesh02" , verts , faces )



