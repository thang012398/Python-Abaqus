# -*- coding: utf-8 -*-
from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class myUtilsDB(AFXDataDialog):
    

    [
	ID_CREATE_GEO,
    ID_CREATE_PRO,
    ID_GENERATE_MSH,
    ID_GEN_PROP,
    ID_ASSIGN,
    ID_HIDE,
    ID_SHOW,
    ID_ABOUT,
    ID_TABLE
    ]=range(AFXDataDialog.ID_LAST, AFXDataDialog.ID_LAST+9)
    #
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'FGM Modeler',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            
        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
        
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CREATE_GEO, myUtilsDB.OnCreateGeo)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CREATE_PRO, myUtilsDB.OnCreatePro)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_GENERATE_MSH, myUtilsDB.OnGenerateMsh)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_GEN_PROP, myUtilsDB.OnGenProp)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_ASSIGN, myUtilsDB.OnAssign)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_HIDE, myUtilsDB.OnHide)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_SHOW, myUtilsDB.OnShow)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_ABOUT, myUtilsDB.OnAbout)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_TABLE, myUtilsDB.OnTable)
        #
            
        GroupBox_1 = FXGroupBox(p=self, text='Create FGM', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        HFrame_1 = FXHorizontalFrame(p=GroupBox_1, opts=LAYOUT_FILL_X, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        VFrame_3 = FXVerticalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        fileName = os.path.join(thisDir,'FGM.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=VFrame_3, text='', ic=icon)       
        VFrame_1 = FXVerticalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VFrame_1, ncols=14, labelText='Geometry Name: ', tgt=form.geo_nameKw, sel=0)
        
        
        
        GroupBox_2 = FXGroupBox(p=VFrame_1, text='Geometry definition', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        VFrame_4 = FXVerticalFrame(p=GroupBox_2, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        HFrame_3 = FXHorizontalFrame(p=VFrame_4, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_3, ncols=6, labelText='width: ', tgt=form.widthKw, sel=0)
        HFrame_4 = FXHorizontalFrame(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0, pl=4, pr=4, pt=0, pb=0)
        AFXTextField(p=HFrame_3, ncols=6, labelText='height: ', tgt=form.heightKw, sel=0)
        HFrame_5 = FXHorizontalFrame(p=VFrame_4, opts=LAYOUT_FILL_X, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_5, ncols=6, labelText='depth: ', tgt=form.depthKw, sel=0)
        HFrame_6 = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0, pl=4, pr=4, pt=0, pb=0)
        AFXTextField(p=HFrame_5, ncols=6, labelText='ncut: ', tgt=form.ncutKw, sel=0)
        hf_as=FXHorizontalFrame(p=VFrame_1, opts=LAYOUT_RIGHT, x=0, y=0, w=0, h=0, pl=5, pr=0, pt=0, pb=0)
        FXButton(p=hf_as, text='Create', ic=None, tgt=self, sel=self.ID_CREATE_GEO, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)


        GroupBox_3 = FXGroupBox(p=VFrame_1, text='Properties definition', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        
        VFrame_4 = FXVerticalFrame(p=GroupBox_3, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        HFrame_3 = FXHorizontalFrame(p=VFrame_4, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_3, ncols=6, labelText='E0: ', tgt=form.E0Kw, sel=0)
        HFrame_4 = FXHorizontalFrame(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0, pl=4, pr=4, pt=0, pb=0)
        AFXTextField(p=HFrame_3, ncols=6, labelText='nu0: ', tgt=form.nu0Kw, sel=0)
        HFrame_5 = FXHorizontalFrame(p=VFrame_4, opts=LAYOUT_FILL_X, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=HFrame_5, ncols=6, labelText='E_func: ', tgt=form.E_funcKw, sel=0)
        HFrame_6 = FXHorizontalFrame(p=HFrame_5, opts=0, x=0, y=0, w=0, h=0, pl=4, pr=4, pt=0, pb=0)
        AFXTextField(p=HFrame_5, ncols=6, labelText='nu_func: ', tgt=form.nu_funcKw, sel=0)
        hf_as=FXHorizontalFrame(p=VFrame_1, opts=LAYOUT_RIGHT, x=0, y=0, w=0, h=0, pl=5, pr=0, pt=0, pb=0)
        
        VFrame_5 = FXVerticalFrame(p=GroupBox_3, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)             
        self.table = AFXTable(VFrame_5, 4, 3, 9999, 3,None,0,AFXTABLE_RESIZE|AFXTABLE_EDITABLE)
        self.table.setLeadingColumns(1)
        self.table.setLeadingRows(1)
        self.table.setItemText(0, 0, 'Layers')
        self.table.setLeadingRowLabels('E\tnu')
        self.table.showHorizontalGrid(True)
        self.table.showVerticalGrid(True)
        self.table.setColumnWidth(0, 40)
        self.table.setColumnJustify(-1, AFXTable.CENTER)
        self.table.appendClientPopupItem('My Button', None, self,self.ID_TABLE)
        self.table.setPopupOptions( 
         AFXTable.POPUP_CUT
        |AFXTable.POPUP_COPY \
        |AFXTable.POPUP_PASTE \
        |AFXTable.POPUP_INSERT_ROW \
        |AFXTable.POPUP_DELETE_ROW \
        |AFXTable.POPUP_CLEAR_CONTENTS \
        |AFXTable.POPUP_READ_FROM_FILE)
        
        HFrame_6 = FXHorizontalFrame(p=GroupBox_3, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        FXButton(p=HFrame_6, text='Generate', ic=None, tgt=self, sel=self.ID_GEN_PROP, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)  
        FXButton(p=HFrame_6, text='Update', ic=None, tgt=self, sel=self.ID_TABLE, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)
        hf_as1=FXHorizontalFrame(p=VFrame_1, opts=LAYOUT_RIGHT, x=0, y=0, w=0, h=0, pl=5, pr=0, pt=0, pb=0)
        FXButton(p=hf_as1, text='Assign', ic=None, tgt=self, sel=self.ID_ASSIGN, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)
 
 
        GroupBox_4 = FXGroupBox(p=VFrame_1, text='Mesh Setting', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        VFrame_5 = FXVerticalFrame(p=GroupBox_4, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VFrame_1, ncols=8, labelText='Seed Size:      ', tgt=form.seed_sizeKw, sel=0)
        ComboBox_2 = AFXComboBox(p=VFrame_5, ncols=0, nvis=1, text='Element Type: ', tgt=form.elem_typeKw, sel=0)
        ComboBox_2.setMaxVisible(10)
        ComboBox_2.appendItem(text='C3D8R')
        ComboBox_2.appendItem(text='C3D8I')

        hf_as1=FXHorizontalFrame(p=VFrame_1, opts=LAYOUT_RIGHT, x=0, y=0, w=0, h=0, pl=5, pr=0, pt=0, pb=0)
        FXButton(p=hf_as1, text='Mesh', ic=None, tgt=self, sel=self.ID_GENERATE_MSH, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)

        
        GroupBox_4 = FXGroupBox(p=VFrame_1, text='Datums', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        hf_as1=FXHorizontalFrame(p=VFrame_1, opts=LAYOUT_RIGHT, x=0, y=0, w=0, h=0, pl=5, pr=0, pt=0, pb=0)
        VFrame_6 = FXHorizontalFrame(p=GroupBox_4, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        FXButton(p=VFrame_6, text='Hide', ic=None, tgt=self, sel=self.ID_HIDE, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)
        FXButton(p=VFrame_6, text='Show', ic=None, tgt=self, sel=self.ID_SHOW, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)      
        FXButton(p=VFrame_1, text='About', ic=None, tgt=self, sel=self.ID_ABOUT, x=0, y=0, w=0, h=0, pl=5, pr=5, pt=1, pb=1)

        self.form = form  
    

    def OnCreateGeo(self, sender, sel, ptr):
        self.form.cmd.setMethod('creatGeometry')
        self.form.issueCommands()
        return None
        
    def OnCreatePro(self, sender, sel, ptr):
        self.form.cmd.setMethod('createProperties')
        self.form.issueCommands()
        return None
    
    def OnGenerateMsh(self, sender, sel, ptr):
        self.form.cmd.setMethod('generateMsh')
        self.form.issueCommands()
        return None
        
    def OnGenProp(self, sender, sel, ptr):

        self.form.cmd.setMethod('createProperties')
        self.form.issueCommands()
        return None
    
    def OnTable(self,sender, sel, ptr):
        ncut=int(self.form.ncutKw.getValue())
        depth=float(self.form.depthKw.getValue())
        E=float(self.form.E0Kw.getValue())
        nu=float(self.form.nu0Kw.getValue())      
        E_func=self.form.E_funcKw.getValue()
        nu_func=self.form.nu_funcKw.getValue()
        MatFile=open('MatFile.txt','w')
        for i in range(ncut):
            Z=i*float(depth)/ncut            
            try:
                E_idx=eval(E_func)
                nu_idx=eval(nu_func)
                self.table.setItemFloatValue(i+1 , 1 , E_idx)
                self.table.setItemFloatValue(i+1,2,nu_idx)
                MatFile.write(str(E_idx)+','+str(nu_idx)+'\n')
            except:
                pass
        
        MatFile.close()
        return None
    
    def OnAssign(self, sender, sel, ptr):        
        self.form.cmd.setMethod('Assign')
        self.form.issueCommands()
        # E=[]
        # nu=[]
        # ncut=int(self.form.ncutKw.getValue())
        # for i in range(ncut):
            # E[i]=self.table.getItemFloatValue(i+1,1)
            # nu[i]=self.table.getItemFloatValue(i+1,2) 
        # partName=self.form.geo_nameKw.getValue()
        # mdb.models['Model-1'].parts[partName]
        pass

        
        return None
        
    def OnShow(self, sender, sel, ptr):
        self.form.cmd.setMethod('Show')
        self.form.issueCommands()
        return None
    def OnAbout(self, sender, sel, ptr):
        self.form.cmd.setMethod('About')
        self.form.issueCommands()
        return None

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def OnHide(self, sender, sel, ptr):
        self.form.cmd.setMethod('Hide')
        self.form.issueCommands()
        return None
        
    
    
    # def updateCurrentObj(self):
        # modelName = self.form.modelNameKw.getValue()
        # partName=self.form.partNameKw.getValue()
        # p = mdb.models[modelName].parts[partName]
        # vpName = session.currentViewportName
        # session.viewports[vpName].setValues(displayedObject=p)
        
class myUtilsDBPickHandler(AFXProcedure):

        count = 0

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def __init__(self, form, keyword, prompt, entitiesToPick, numberToPick):
            self.form = form
            self.keyword = keyword
            self.prompt = prompt
            self.numberToPick = ONE # Enum value
            self.entitiesToPick = entitiesToPick

            
            AFXProcedure.__init__(self, form.getOwner())
            
            
            
            myUtilsDBPickHandler.count += 1
            self.setModeName('myUtilsDBPickHandler%d' % (myUtilsDBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

            self.node1.setValueToDefault()
            self.node2.setValueToDefault()
            self.node3.setValueToDefault()

            
            myUtilsDBPickHandler.count=1
            self.prompt='Pick the first node'
            self.step1=AFXPickStep(self, self.node1, self.prompt, 
            AFXPickStep.NODES,self.numberToPick, sequenceStyle=TUPLE)
            return self.step1            
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):
                if previousStep == self.step1:
                    myUtilsDBPickHandler.count+=1
                    self.prompt='Pick the second node'
                    self.step2=AFXPickStep(self, self.node2, self.prompt, 
                    AFXPickStep.NODES,self.numberToPick, sequenceStyle=TUPLE)
                    return self.step2
                elif previousStep == self.step2:
                    myUtilsDBPickHandler.count+=1
                    self.prompt='Pick the third node'
                    self.step3=AFXPickStep(self, self.node3, self.prompt, 
                    AFXPickStep.NODES,self.numberToPick, sequenceStyle=TUPLE)
                    return self.step3
                elif previousStep == self.step3:
                    self.makeDecision()
                    return None
        def getLoopStep(self):
            return self.step1
        
        def makeDecision(self):
            self.verifyCurrentKeywordValues()
            self.form.cmd.setMethod('modiPos')
            self.form.issueCommands()
            self.getLoopStep()
        
        def deactivate(self):

            #AFXProcedure.deactivate(self)
            #if  self.numberToPick == ONE and self.keyword.getValue() and self.keyword.getValue()[0]!='<':
                #sendCommand(self.keyword.getSetupCommands() + '\nhighlight(%s)' % self.keyword.getValue() )
            #if self.node!=None:
               #AFXProcedure.deactivate(self)
            #writemessage('ok',1)
            #self.form.cmd.setMethod('mainFunc')
            #self.form.issueCommands()
            AFXProcedure.deactivate(self)


def writemessage(text,box):
    mw=getAFXApp().getAFXMainWindow()
    if box:
        mw.writeToMessageArea('/'+len(text)*'-'+8*'-'+'\\')
        mw.writeToMessageArea('|'+(len(text)+8)*' '+'|')
        mw.writeToMessageArea('|'+4*' '+text+4*' '+'|')
        mw.writeToMessageArea('|'+(len(text)+8)*' '+'|')
        mw.writeToMessageArea('\\'+len(text)*'-'+8*'-'+'/')
    else:
        mw.writeToMessageArea(text)
def getdir(name):
    fo = open("dir_info_202019.txt", "w")
    seq = dir(name)
    for i in seq:
        fo.write( i+'\n' )
    fo.close()
    return None  