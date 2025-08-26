bl_info = {
    "name": "EZ-Unwrap",
    "author": "Joseph Richardson",
    "version": (1, 1),
    "blender": (3, 0, 0),
    "location": "UV > Unwrap > EZ-Unwrap",
    "description": "EZ Unwrap helper: Lightmap Pack, Follow Active Quads, Pack Islands, assign cyan random-named material",
    "category": "UV",
}

import bpy
import random
import string
from bpy.types import Operator
from bpy.props import BoolProperty


def random_material_name(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


class UV_OT_ez_unwrap(Operator):
    bl_idname = "uv.ez_unwrap"
    bl_label = "EZ-Unwrap"
    bl_options = {'REGISTER', 'UNDO'}

    try_follow_quads: BoolProperty(
        name="Try Follow Active Quads",
        default=True,
        description="Try using Follow Active Quads before Lightmap Pack"
    )

    def execute(self, context):
        obj = context.object

        if obj.type != 'MESH':
            self.report({'ERROR'}, "Selected object is not a mesh")
            return {'CANCELLED'}

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.uv.select_all(action='SELECT')

        follow_active_success = False

        if self.try_follow_quads:
            try:
                bpy.ops.uv.follow_active_quads(mode='LENGTH_AVERAGE')
                follow_active_success = True
            except Exception as e:
                self.report({'WARNING'}, f"Follow Active Quads failed: {e}")

        if not follow_active_success:
            bpy.ops.uv.lightmap_pack(PREF_CONTEXT='ALL_FACES', PREF_PACK_IN_ONE=True)

        bpy.ops.uv.pack_islands(margin=0.001)

        # Create new material with random name
        mat_name = random_material_name()
        new_mat = bpy.data.materials.new(name=mat_name)
        new_mat.use_nodes = True

        # Make the material cyan
        nodes = new_mat.node_tree.nodes
        links = new_mat.node_tree.links
        nodes.clear()

        output_node = nodes.new(type='ShaderNodeOutputMaterial')
        output_node.location = (300, 0)

        bsdf_node = nodes.new(type='ShaderNodeBsdfPrincipled')
        bsdf_node.location = (0, 0)
        bsdf_node.inputs['Base Color'].default_value = (0.0, 1.0, 1.0, 1.0)  # Cyan RGBA

        links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])

        # Clear existing materials and assign only the new one
        obj.data.materials.clear()
        obj.data.materials.append(new_mat)
        mat_index = 0

        # Assign material to selected faces
        bpy.ops.object.mode_set(mode='OBJECT')
        mesh = obj.data
        selected_faces = [p for p in mesh.polygons if p.select]

        for face in selected_faces:
            face.material_index = mat_index

        bpy.ops.object.mode_set(mode='EDIT')
        self.report({'INFO'}, f"Unwrapped and assigned cyan material '{mat_name}'")
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(UV_OT_ez_unwrap.bl_idname)


def register():
    bpy.utils.register_class(UV_OT_ez_unwrap)
    bpy.types.VIEW3D_MT_uv_map.append(menu_func)


def unregister():
    bpy.utils.unregister_class(UV_OT_ez_unwrap)
    bpy.types.VIEW3D_MT_uv_map.remove(menu_func)


if __name__ == "__main__":
    register()
