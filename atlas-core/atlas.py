from path import Path
from qface.generator import FileSystem, Generator
import qface.idl.domain as domain
import typing

class AtlasFormatter:
    """ Atlas Formatter """

    @staticmethod
    def format_module_name(name: str, delimiter: str, prefix: str = '', suffix: str = ''):
        return f"{prefix}{delimiter.join(name.split('.'))}{suffix}"

class AtlasSystem():
    """ Atlas System """
    def __init__(self, qface_system: domain.System):
        # Initialize properties
        self.qface_system = qface_system
        self.atlas_modules = list()
        self._is_system_initialized = False
        self.process_modules()

    @property
    def is_system_initialized(self):
        return self._is_system_initialized

    def lookup(self, name: str):
        """ Lookup a symbol in the qface_system """
        return self.qface_system.lookup(name)

    def process_modules(self):
        if not self.qface_system:
            self._is_system_initialized = False
            return

        for module in self.qface_system.modules:
            self.atlas_modules.append(AtlasModule(self, module))
        self.order_modules_by_dependencies()

        self._is_system_initialized = True

    def get_module_dependencies(self, module_name: str):
        """ Return the module dependencies for a module identified by module_name """
        dependencies = list()
        qface_module = self.lookup(module_name)

        if not self.is_system_initialized:
            print(f"ERROR: System is not initialized")
            return dependencies

        if qface_module is None:
            print(f"WARNING: qface module not found: {module_name}")
            return dependencies

        for atlas_import_w_version in qface_module.imports:
            atlas_import = atlas_import_w_version.split(' ')[0]
            dependencies.append(atlas_import)

        return dependencies

    def order_modules_by_dependencies(self):
        """ Order modules based on their dependencies to ensure proper processing order """
        # Get list of all the modules
        module_list = list()
        for atlas_module in self.atlas_modules:
            module_list.append(atlas_module.qface_module.name)

        # Create dependency map
        dependency_map = dict()
        for atlas_module in self.atlas_modules:
            dependency_map[atlas_module.name] = self.get_module_dependencies(atlas_module.name)

        ordered_module_list = module_list.copy()
        for module in module_list:
            dependency_list = dependency_map[module]
            if len(dependency_list) == 0:
                # Module has no dependencies, move it to the beginning
                ordered_module_list.insert(0, ordered_module_list.pop(ordered_module_list.index(module)))
            else:
                # Module has dependencies, walk the list and add the element there
                highest_index = 0
                for dependency in dependency_list:
                    dependency_index = ordered_module_list.index(dependency)
                    if dependency_index > highest_index:
                        highest_index = dependency_index
                ordered_module_list.insert(highest_index, ordered_module_list.pop(ordered_module_list.index(module)))

        ordered_atlas_modules = list()
        for ordered_module in ordered_module_list:
            for atlas_module in self.atlas_modules:
                if atlas_module.name == ordered_module:
                    ordered_atlas_modules.append(atlas_module)

        self.atlas_modules = ordered_atlas_modules

class AtlasModule():
    """ Atlas Module """
    def __init__(self, atlas_system: AtlasSystem, qface_module: domain.Module):
        # Initialize properties
        self.atlas_system = atlas_system
        self.qface_module = qface_module

    def __repr__(self):
        return f"AtlasModule:name={self.name}"

    def __str__(self):
        return self.__repr__()

    def lookup(self, name: str, fragment: str = None):
        return self.qface_module.lookup(name, fragment)

    @property
    def name(self):
        return self.qface_module.name

    def formatted_name(self, delimiter: str, prefix: str = '', suffix: str = ''):
        return AtlasFormatter.format_module_name(self.qface_module.name, delimiter, prefix, suffix)

    @property
    def imported_modules(self):
        modules = list()
        for imported_module_name, imported_module_str in self.qface_module._importMap.items():
            imported_module_symbol = self.atlas_system.lookup(imported_module_name)
            if imported_module_symbol:
                modules.append(imported_module_symbol)
        return modules

class AtlasInterface(object):
    pass

class AtlasStruct(object):
    pass

class AtlasEnum(object):
    pass

class AtlasGen:
    """ AtlasGen """

    def __init__(self, interface_path):
        self._interface_path = interface_path
        self.atlas_system = AtlasSystem(None)

    @property
    def interface_path(self):
        return self._interface_path

    @property
    def system(self):
        return self.atlas_system

    def generate(self):
        print(f"generate interfaces from path: {self.interface_path}")
        self.atlas_system = AtlasSystem(FileSystem.parse(self.interface_path))
        # self.log_system(self.atlas_system)

    def log_system(self, system):
        print(f"postprocessing...")

        for module in system.atlas_modules:
            print(f"module: {module.name}")
            print(f"\t formatted with :: { module.formatted_name('::') }")
            print(f"\t formatted with _ { module.formatted_name('_') }")
            print(f"\t formatted with 'prefix(', ')suffix', delimiter '|' { module.formatted_name('|', 'prefix(', ')suffix') }")

            for imported_module in module.imported_modules:
                print(f"imported_module: {imported_module}")

        for atlas_module in system.atlas_modules:
            module = atlas_module.qface_module
            print(f"module: {module}")
            for interface in module.interfaces:
                print(f"\tinterface: {interface}")
                for _property in interface.properties:
                    print(f"\t\t_property: {_property.type.name} {_property.name} (qualified_name: {_property.qualified_name})")
                for _operation in interface.operations:
                    parameters = _operation.parameters
                    parameters_str = parameters if len(parameters) > 0 else ""
                    print(f"\t\t_operation: {_operation.type.name} {_operation.name}({ parameters_str }) (qualified_name: {_operation.qualified_name})")
                for _signal in interface.signals:
                    print(f"\t\t_signal: {_signal.name}")
            for struct in module.structs:
                print(f"\tstruct: {struct}")
                for _field in struct.fields:
                    print(f"\t\t_field: {_field.type.name} {_field.name} (qualified_name: {_field.qualified_name})")

        pass

