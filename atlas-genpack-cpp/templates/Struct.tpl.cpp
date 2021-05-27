{% set class_name = struct.name %}
{{ notice_cpp }}

#include "{{ class_name }}.h"

{{ cpp_namespace_begin }}

{{ class_name }}::{{ class_name }}()
    : IStruct()
    {{ struct | initializers }}
{

}

{{ class_name }}::~{{ class_name }}()
{

}

{{ cpp_namespace_end }}
