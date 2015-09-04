import bpy

class Gunbuilder():
    pass

class Picrail(Gunbuilder):
    def railmaker(self):
        for x in range(0,10):
            x = x*2
            
            bpy.ops.mesh.primitive_cube_add(radius=1)
            bpy.ops.transform.resize(value=(1, 0.5, 1))
            bpy.ops.transform.translate(value=(0,x,0))
            bpy.ops.object.select_pattern(pattern='Cube*')
            bpy.ops.object.join()
    
    def contextswitcher(self):
        bpy.ops.object.editmode_toggle()
    
    def cursorSwitch(self):
        bpy.context.scene.cursor_location=(0.0, 0.0, 0.0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        
    def movetoOrigin(self):
        bpy.context.object.location[1] = 0
        
            
rail = Picrail()
rail.cursorSwitch()
rail.railmaker()
rail.movetoOrigin()
