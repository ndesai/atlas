def get_filters():
    return {
        'type_name': type_name,
        'variable_name': variable_name,
        'initial_value': initial_value,
        'member_declaration': member_declaration,
        'initializers': initializers,
        'includes': includes,
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
    for prop in s.properties:
        if prop.type.is_complex:
            pass
        else:
            statement = f", {variable_name(prop)}({initial_value(prop)})"
            statements.append(statement)
    return '\n'.join(statements)

def includes(s):
    """ Return include statements for an interface """
    include_statements = list()
    for prop in s.properties:
        if prop.type.is_complex:
            include_path = '/'.join(prop.type.name.split('.'))
            statement = f"#include <{include_path}.h>"
            include_statements.append(statement)
        if prop.type.is_list:
            include_statements.append("#include <vector>")
        if prop.type.is_map:
            include_statements.append("#include <map>")
    include_statements = list(set(include_statements))
    return '\n'.join(sorted(include_statements))
