{% set class_name = struct.name %}
{{ notice_cpp }}

#pragma once

#include <IStruct.h>
{{ struct | includes }}

{{ cpp_namespace_begin }}

class {{ class_name }} : public IStruct {
public:
    {{ class_name }}();
    ~{{ class_name }}();

private:
    {% for property in struct.fields %}
    {{ property | member_declaration}}
    {% endfor %}
};

{{ cpp_namespace_end }}
