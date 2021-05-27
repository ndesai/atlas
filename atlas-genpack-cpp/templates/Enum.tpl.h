{% set class_name = enum.name %}
{{ notice_cpp }}

#pragma once

{{ cpp_namespace_begin }}

class {{ class_name }}Class {
public:
    enum Value
    {
    {% for member in enum.members %}
        {{ member.name }} = {{ member.value }},
    {% endfor %}
    };
};

typedef {{ class_name }}Class::Value {{ class_name }};

{{ cpp_namespace_end }}