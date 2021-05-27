def get_filters():
    return {
        'type_name': type_name,
        'variable_name': variable_name,
        'initial_value': initial_value,
        'member_declaration': member_declaration,
        'initializers': initializers,
        'include_statements': include_statements,
        'includes': includes,
        'format_name': format_name,
        'target_name': target_name,
        'target_link_libraries': target_link_libraries,
    }

def type_name(s):
    if s.type.is_int:
        return 'int'
    if s.type.is_real:
        return 'float'
    if s.type.is_bool:
        return 'bool'
    if s.type.is_string:
        return 'std::string'
    if s.type.is_list:
        return f"std::vector<{type_name(s.type.nested)}>"
    if s.type.is_map:
        return f"std::map<nullptr, nullptr>"
    if s.type.is_complex:
        return '::'.join(s.type.name.split('.'))
    return None

def variable_name(s):
    return f"m_{s.name}"

def initial_value(s):
    if s.type.is_int:
        return '0'
    if s.type.is_real:
        return '0.f'
    if s.type.is_bool:
        return 'false'
    if s.type.is_string:
        return 'std::string()'
    if s.type.is_list:
        return '{}'
    if s.type.is_map:
        return '{}'
    return None

def member_declaration(s):
    return f"{type_name(s)} {variable_name(s)};"

def initializers(s):
    """ Return initializer statements for an interface """
    statements = list()
    properties = get_properties(s)
    for prop in properties:
        if prop.type.is_complex:
            pass
        else:
            statement = f", {variable_name(prop)}({initial_value(prop)})"
            statements.append(statement)
    return '\n'.join(statements)

def include_statements(s):
    _include_statements = list()
    if s.type.is_complex:
        include_path = '/'.join(s.type.name.split('.'))
        statement = f"#include <{include_path}.h>"
        _include_statements.append(statement)
    if s.type.is_string:
        _include_statements.append("#include <string>")
    if s.type.is_list:
        _include_statements.append("#include <vector>")
        _include_statements.extend(include_statements(s.type.nested))
    if s.type.is_map:
        _include_statements.append("#include <map>")
    return _include_statements

def includes(s):
    """ Return include statements for an interface """
    _include_statements = list()
    properties = get_properties(s)
    for prop in properties:
        _include_statements.extend(include_statements(prop))
    _include_statements = list(set(_include_statements))
    return '\n'.join(sorted(_include_statements))

def format_name(s, delimiter='-'):
    name = s if not hasattr(s, 'name') else s.name
    return delimiter.join(name.split('.'))

def target_name(s):
    """ CMake target name """
    return format_name(s, '-')

def target_link_libraries(s):
    """ CMake target dependencies """
    statements = list()
    for module_import in s.imported_modules:
        statements.append(target_name(module_import.name))
    statements = list(set(statements))
    return '\n\t'.join(sorted(statements))

def get_properties(s):
    """ Disambiguate the properties between an interface, struct, enum """
    properties = list()
    properties = list()
    if hasattr(s, 'properties'):
        properties = s.properties
    elif hasattr(s, 'fields'):
        properties = s.fields
    elif hasattr(s, 'members'):
        properties = s.members
    return properties
