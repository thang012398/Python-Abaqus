# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *
from caeModules import *
import sys
import numpy as np
from math import *
from regionToolset import *


class RectangleGeo():
    __model_name='Model-1'
    
    def __init__(self,prt_name='',width=30,height=15,depth=2,ncut=1):

        try:
            type(width).__name__=='int' or type(width).__name__=='float'
            type(height).__name__=='int' or type(height).__name__=='float'
            type(depth).__name__=='int' or type(depth).__name__=='float'
            type(ncut).__name__=='int'
        except:
            raise Exception,'Input ValueError'
            
        self.width=width
        self.height=height
        self.depth=depth
        self.ncut=ncut

        if prt_name=='':
            self.prt_name='geo_{}_{}_{}'.format(width,height,depth)
        else:
            self.prt_name=prt_name
        return None
    
    @staticmethod
    def queryInfo():

        return None
    
    @property
    def detailInfo():

        return None
        
    
    
    def createGeom(self):

        m=mdb.models[RectangleGeo.__model_name]

        s=m.ConstrainedSketch(name='__profile__', sheetSize=200.0)
        g,v,d,c=s.geometry,s.vertices,s.dimensions,s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.rectangle(point1=(0.0, 0.0), point2=(self.width, self.height))

        try:
            p = m.Part(name=self.prt_name
                       ,dimensionality=THREE_D
                       ,type=DEFORMABLE_BODY)
        except:
            p = m.Part(name=self.prt_name+'_copy1'
                       ,dimensionality=THREE_D
                       ,type=DEFORMABLE_BODY)
            self.prt_name=self.prt_name+'_copy1'
        p = m.parts[self.prt_name]

        p.BaseSolidExtrude(sketch=s, depth=self.depth)
        s.unsetPrimaryObject()
        del m.sketches['__profile__']
      
        return None
        
    def createProperty(self):
        m=mdb.models[RectangleGeo.__model_name]
        p=m.parts[self.prt_name]
        # fields = (('E0:','0'), ('nu0:', '0'), ('E_func:', ''),('nu_func:', ''))
        # E, nu, E1,nu1 = getInputs(fields=fields, label='Specify block dimensions:',
                    # dialogTitle='Properties defination', )  
        ncount=int(self.ncut)
        data=open('MatFile.txt','r+')
        for i in range(ncount):
            mat=data.readline()
            mat=mat.split(',')
            print(mat)
            E_idx=mat[0]
            nu_idx=mat[1]
            matName='Mat'+str(i)
            m.Material(name=matName)
            m.materials[matName].Elastic(table=((float(E_idx), float(nu_idx)), ))
            m.HomogeneousSolidSection(name=matName , material=matName, thickness=None)
            
        data.close()
        return None
    def AssignMat(self):
        m=mdb.models[RectangleGeo.__model_name]
        p=m.parts[self.prt_name]
        for i in range(self.ncut):
            zPos=float(self.depth)/(2.0*self.ncut)+i*float(self.depth)/self.ncut
            c=p.cells.findAt(((0, 0, zPos),))
            region = regionToolset.Region(cells=c)
            secName='Mat'+str(i)
            p.SectionAssignment(region=region, sectionName=secName, offset=0.0, 
                                offsetType=MIDDLE_SURFACE, offsetField='', 
                                thicknessAssignment=FROM_SECTION)
        
        
    def makePartion(self):

        m=mdb.models[RectangleGeo.__model_name]
        p=m.parts[self.prt_name]
        
        for i in range(1,self.ncut):
            p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=i*float(self.depth)/self.ncut)
        
        for i in range(0,self.ncut-1):
            c=p.cells.findAt(((0, 0, self.depth),))
            d1=p.datums
            p.PartitionCellByDatumPlane(datumPlane=d1[d1.keys()[i]], cells=c)
        return None
    
    def getSurfSet(self):
        #solid set
        m=mdb.models[RectangleGeo.__model_name]
        p=m.parts[self.prt_name]
        c=p.cells
        p.Set(cells=c, name='solid')
        
        
       
        return None        
    
    def generateMesh(self,elem_type=C3D8I,sed_size='auto'):
                    
        m=mdb.models[RectangleGeo.__model_name]
        p=m.parts[self.prt_name]
        c=p.cells
        solid_set=p.sets['solid']
        p.setMeshControls(regions=c, technique=SWEEP, algorithm=MEDIAL_AXIS)
        elemType1 = mesh.ElemType(elemCode=elem_type
                                 ,elemLibrary=STANDARD
                                 ,secondOrderAccuracy=OFF
                                 ,distortionControl=DEFAULT)
        p.setElementType(regions=solid_set,elemTypes=(elemType1,))

        if sed_size=='auto':
            calculated_size=p.getPartSeeds(DEFAULT_SIZE)
        else:
            calculated_size=sed_size
            
        if calculated_size > 2.7*float(self.depth)/self.ncut:
            reply=getWarningReply(message='Your Global seed size may be got Aspect ratio Error!!!\nContinue?', buttons=(YES,NO))
            if reply==YES:
                p.seedPart(size=calculated_size, deviationFactor=0.1, minSizeFactor=0.1)
                p.generateMesh()
            elif reply==NO:
                return
        else:
            p.seedPart(size=calculated_size, deviationFactor=0.1, minSizeFactor=0.1)
            p.generateMesh()
        return None
        
        
    def showDatum(self):
        vpName = session.currentViewportName
        session.viewports[vpName].partDisplay.geometryOptions.setValues(datumPlanes=ON)
        session.viewports[vpName].assemblyDisplay.geometryOptions.setValues(datumPlanes=ON)
    
    def hideDatum(self):
        vpName = session.currentViewportName
        session.viewports[vpName].partDisplay.geometryOptions.setValues(datumPlanes=OFF)
        session.viewports[vpName].assemblyDisplay.geometryOptions.setValues(datumPlanes=OFF)
    
    
    

#the codes below will be running if this file is used as a script       
if __name__=='__main__':
    pass  # <- try to modify this




