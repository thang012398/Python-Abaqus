from abaqusGui import *
from abaqusConstants import ALL
import osutils, os

class MyForm(AFXForm):
    def __init__(self,owner):
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='mainFunc',objectName='myUtils_kernel', registerQuery=False)
        pickedDefault = ''
        self.geo_nameKw = AFXStringKeyword(self.cmd, 'geo_name', True, '')
        self.widthKw = AFXFloatKeyword(self.cmd, 'width', True)
        self.heightKw = AFXFloatKeyword(self.cmd, 'height', True)
        self.depthKw = AFXFloatKeyword(self.cmd, 'depth', True)
        self.ncutKw = AFXFloatKeyword(self.cmd, 'ncut', True)
        self.E0Kw= AFXFloatKeyword(self.cmd, 'E0', True)
        self.nu0Kw= AFXFloatKeyword(self.cmd, 'nu0', True)
        self.E_funcKw = AFXStringKeyword(self.cmd, 'E_func', True)
        self.nu_funcKw = AFXStringKeyword(self.cmd, 'nu_func', True)
        self.seed_sizeKw = AFXFloatKeyword(self.cmd, 'seed_size', True)
        self.elem_typeKw = AFXStringKeyword(self.cmd, 'elem_type', True)
        
    def getFirstDialog(self):

        import myUtilsDB
        return myUtilsDB.myUtilsDB(self)


    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):
    
        return False
        

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='FGM Modeler', 
    object=MyForm(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import myUtils_kernel',
    applicableModules=ALL,
    version='1.0',
    author='Thang Nguyen Huu',
    description='Bach Khoa University',
    helpUrl='https://www.facebook.com/thang199801666'
)


