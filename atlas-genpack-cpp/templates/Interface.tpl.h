{% set class_name = interface.name %}
{{ notice_cpp }}

#pragma once

#include <IServiceServer.h>
{{ interface | includes }}

{{ cpp_namespace_begin }}

class {{ class_name }} : public IServiceServer {
public:
    {{ class_name }}();
    ~{{ class_name }}();

private:
    {% for property in interface.properties %}
    {{ property | member_declaration}}
    {% endfor %}
};

{{ cpp_namespace_end }}
