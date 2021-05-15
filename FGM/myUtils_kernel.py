# -*- coding: utf-8 -*-

from abaqus import *
from abaqusConstants import *
from caeModules import *
from function import *
import numpy as np
import os

modelName='Model-1'

def mainFunc(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):
    return None
    
    
def creatGeometry(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):

    geo=RectangleGeo(geo_name,width,height,depth,ncut)
    print('Step1: initialization...')
    geo.createGeom()
    print('Step2: generate 3D geometry...')
    geo.makePartion()
    print('Step3: make the partition...')
    geo.getSurfSet()
    print('Step4: define the surfaces and sets...')

    p = mdb.models[modelName].parts[geo_name]
    vpName = session.currentViewportName
    session.viewports[vpName].setValues(displayedObject=p)
    print('Complete geometric setup!')
    return None

def createProperties(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):
    geo=RectangleGeo(geo_name,width,height,depth,ncut)
    geo.createProperty()
                 

    return None

def generateMsh(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):

    e_type=SymbolicConstant(elem_type)
    geo=RectangleGeo(geo_name,width,height,depth,ncut)
    geo.generateMesh(elem_type=e_type,sed_size=seed_size)
    vpName = session.currentViewportName
    session.viewports[vpName].partDisplay.setValues(mesh=ON)
    return None  
    

def Assign(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):
               
    geo=RectangleGeo(geo_name,width,height,depth,ncut)          
    geo.AssignMat()
    return None

def Show(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):
    geo=RectangleGeo(geo_name,width,height,depth,ncut)          
    geo.showDatum()
    return None
    
def Hide(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):
    geo=RectangleGeo(geo_name,width,height,depth,ncut)          
    geo.hideDatum()
    return None      
   
   
def About(geo_name
            ,width
            ,height
            ,depth
            ,ncut
            ,E0
            ,nu0
            ,E_func
            ,nu_func
            ,seed_size
            ,elem_type):
    reply = getWarningReply('This Plug-in was developed by\nThang Nguyen Huu\nApplied Sciences\nBach Khoa University', (YES,NO))
               