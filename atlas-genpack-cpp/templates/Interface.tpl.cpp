{% set class_name = interface.name %}
{{ notice_cpp }}

#include "{{ class_name }}.h"

{{ cpp_namespace_begin }}

{{ class_name }}::{{ class_name }}()
    : IServiceServer()
    {{ interface | initializers }}
{

}

{{ class_name }}::~{{ class_name }}()
{

}

{{ cpp_namespace_end }}
