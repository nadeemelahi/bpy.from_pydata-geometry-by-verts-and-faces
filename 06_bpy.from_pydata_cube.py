
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

def duplicateAtZ( cnt , atz , verts ):

	# ex) copy 0,1,2,3 -> 4=0, 5=1, 6=2, 7=3
	idx = 0

	while idx < cnt :

		verts[idx + cnt][0] = verts[idx][0]
		verts[idx + cnt][1] = verts[idx][1]
		verts[idx + cnt][2] = atz

		idx += 1

def setSidesBetweenParallelFaces( div , faces ):

	start = 0 # first index
	end = div*2 - 1 # div divisions

	idx = end
	jdx = 0
	lim = div - 1

	while jdx < lim :

		faces[jdx][0] = idx
		faces[jdx][1] = idx - 1
		faces[jdx][2] = idx - div - 1
		faces[jdx][3] = idx - div

		idx -= 1
		jdx += 1

	# last
	faces[jdx][0] = idx
	faces[jdx][1] = end
	faces[jdx][2] = end - div
	faces[jdx][3] = start

	#bottom 
	jdx += 1

	idx = 0
	while idx < div :
		faces[jdx][idx] = idx

		idx += 1

	#top
	jdx += 1
	
	idx = 0
	kdx = 7
	while idx < div :
		faces[jdx][idx] = kdx

		kdx -= 1
		idx += 1



		



# circle by divisions
divisions = 4 
angle = 360 / divisions # 360 / 8 = 45 deg

# cicle by division length in angle degrees
#angle = 45
#divisions = 360 / angle

vertsDim = 3 # x , y , z

vertsLen = int ( divisions * 2 ) 

verts = np.zeros( ( vertsLen , vertsDim ) , dtype = float )

verts[0] = [  2.0 ,  2.0 , 1.0 ]
verts[1] = [ -2.0 ,  2.0 , 1.0 ]
verts[2] = [ -2.0 , -2.0 , 1.0 ]
verts[3] = [  2.0 , -2.0 , 1.0 ]

duplicateAtZ( 4 , -1.0 , verts)
print3Darray( 0 , vertsLen , verts)

#
facesDim = 4 # 3 vert triangles - 4 vert quads
facesLen = int( divisions + 2 ) # +2 top and bottom
faces = np.zeros( ( facesLen , facesDim ) , dtype = int )

setSidesBetweenParallelFaces( divisions , faces )
print4Darray( 0 , facesLen , faces )


makeMeshByNameVertsAndFaces ( "mesh01" , verts , faces )




#setVertZ( 0 , vertsLen , verts , 1.0 )
#makeMeshByNameVertsAndFaces ( "mesh02" , verts , faces )



