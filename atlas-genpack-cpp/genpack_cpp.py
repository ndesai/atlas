import atlas
from genpack import GenPack
import pathlib
import filters

class CppGenPack(GenPack):
    """ Generate C++ """
    def __init__(self, atlas_system: atlas.AtlasSystem):
        super().__init__(atlas_system)

        # Set up configuration
        script_path = pathlib.Path(__file__).parent.absolute()
        self.template_path = f"{script_path}/templates"
        self.filters = filters.get_filters()

        self.setup()
        pass

    def __repr__(self):
        return f"CppGenPack"

    def __str__(self):
        return self.__repr__()

    def start_generation(self):
        ctx = self.context.copy()
        self.gen("CMakeLists.tpl.txt", "output/cpp/CMakeLists.txt", ctx)
        for module in self.atlas_system.atlas_modules:
            self.prepare_module_context(module, ctx)
            for interface in module.qface_module.interfaces:
                self.prepare_interface_context(interface, ctx)
                self.gen("Interface.tpl.h", "output/cpp/{{ module_as_folder_path }}/{{ interface.name }}.h", ctx)
                self.gen("Interface.tpl.cpp", "output/cpp/{{ module_as_folder_path }}/{{ interface.name }}.cpp", ctx)
            for struct in module.qface_module.structs:
                self.prepare_struct_context(struct, ctx)
                self.gen("Struct.tpl.h", "output/cpp/{{ module_as_folder_path }}/{{ struct.name }}.h", ctx)
                self.gen("Struct.tpl.cpp", "output/cpp/{{ module_as_folder_path }}/{{ struct.name }}.cpp", ctx)
            for enum in module.qface_module.enums:
                self.prepare_enum_context(enum, ctx)
                self.gen("Enum.tpl.h", "output/cpp/{{ module_as_folder_path }}/{{ enum.name }}.h", ctx)
                self.gen("Enum.tpl.cpp", "output/cpp/{{ module_as_folder_path }}/{{ enum.name }}.cpp", ctx)
        pass

    def finish_generation(self):
        pass

    def clean_context(self, ctx):
        # Clean up properties
        if 'interface' in ctx: ctx.pop('interface')
        if 'struct' in ctx: ctx.pop('struct')
        if 'enum' in ctx: ctx.pop('enum')
        pass

    def prepare_module_context(self, element, ctx):
        ctx.update({'module': element})
        ctx.update({'module_as_folder_path': element.formatted_name('/')})
        ctx.update({'cpp_namespace': element.formatted_name('::')})
        namespace_begin = list()
        for name in element.name_split:
            namespace_begin.append(f"namespace {name} {{")
        ctx.update({'cpp_namespace_begin': '\n'.join(namespace_begin)})
        namespace_end = list()
        for name in reversed(element.name_split):
            namespace_end.append(f"}} // end namespace \"{name}\"")
        ctx.update({'cpp_namespace_end': '\n'.join(namespace_end)})
        pass

    def prepare_interface_context(self, element, ctx):
        self.clean_context(ctx)
        ctx.update({'interface': element})
        pass

    def prepare_struct_context(self, element, ctx):
        self.clean_context(ctx)
        ctx.update({'struct': element})
        pass

    def prepare_enum_context(self, element, ctx):
        self.clean_context(ctx)
        ctx.update({'enum': element})
        pass
