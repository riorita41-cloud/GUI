#include <pybind11/pybind11.h>
#include <stack>
#include <string>

namespace py = pybind11;

struct TElement {
    std::string name;
    int age;
};

static std::stack<TElement> g_stack;

PYBIND11_MODULE(stack_stl, m) {

    m.doc() = "STL stack module";

    m.def("init", []() {
        while (!g_stack.empty()) {
            g_stack.pop();
        }
    });

    m.def("push", [](const std::string& name, int age) -> bool {
        if (name.empty() || age < 0) {
            return false;
        }
        TElement elem;
        elem.name = name;
        elem.age = age;
        g_stack.push(elem);
        return true;
    });

    m.def("pop", []() -> bool {
        if (g_stack.empty()) {
            return false;
        }
        g_stack.pop();
        return true;
    });

    m.def("peek_name", []() -> std::string {
        if (g_stack.empty()) {
            return "__EMPTY__";
        }
        return g_stack.top().name;
    });

    m.def("peek_age", []() -> int {
        if (g_stack.empty()) {
            return -1;
        }
        return g_stack.top().age;
    });

    m.def("get_size", []() -> int {
        return (int)g_stack.size();
    });

    m.def("get_all", []() {
        py::list result;
        std::stack<TElement> temp = g_stack;
        while (!temp.empty()) {
            TElement elem = temp.top();
            result.append(py::make_tuple(elem.name, elem.age));
            temp.pop();
        }
        return result;
    });

    m.def("clear_stack", []() {
        while (!g_stack.empty()) {
            g_stack.pop();
        }
    });
}