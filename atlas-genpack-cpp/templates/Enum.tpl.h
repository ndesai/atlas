{% set class_name = enum.name %}
#pragma once

class {{ class_name }}Class {
public:
    enum class {{ class_name }}
    {
    {% for member in enum.members %}
        {{ member.name }} = {{ member.value }},
    {% endfor %}
    };
};

typedef {{ class_name }}Class::{{ class_name }};